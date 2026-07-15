#!/usr/bin/env python3
"""runtime — Execute a graph-ai IR graph by walking nodes & resolving edges."""

from __future__ import annotations
import importlib
import operator, sys
from typing import Any
from packages.graph_ir import Graph, Node, Edge, NODE_TYPES
from packages.node_catalog import NodeCatalog, NodeSpec

# ── Operator mapping ──
BINOPS = {
    "Add": operator.add, "Sub": operator.sub, "Mult": operator.mul,
    "Div": operator.truediv, "FloorDiv": operator.floordiv, "Mod": operator.mod,
    "Pow": operator.pow, "LShift": operator.lshift, "RShift": operator.rshift,
    "BitOr": operator.or_, "BitXor": operator.xor, "BitAnd": operator.and_,
}
UNOPS = {"UAdd": operator.pos, "USub": operator.neg, "Not": operator.not_,
         "Invert": operator.inv}
CMPS = {
    "Eq": operator.eq, "NotEq": operator.ne, "Lt": operator.lt,
    "LtE": operator.le, "Gt": operator.gt, "GtE": operator.ge,
    "Is": operator.is_, "IsNot": operator.is_not, "In": operator.contains,
    "NotIn": lambda a, b: not operator.contains(a, b),
}

class ExpressionEvaluator:
    """Evaluate an expression sub-graph rooted at a data node."""

    def __init__(self, graph: Graph, variables: dict[str, Any]):
        self.graph = graph
        self.vars = variables
        self._node_map = {n.id: n for n in graph.nodes}
        self._edge_map: dict[str, list[Edge]] = {}
        for e in graph.edges:
            self._edge_map.setdefault(e.target, []).append(e)

    def resolve(self, node_id: str) -> Any:
        node = self._node_map[node_id]
        handler = getattr(self, f"eval_{node.type}", self.eval_CodeBlockNode)
        return handler(node)

    def _get_incoming(self, node_id: str, port: str) -> Any:
        """Get the value arriving on a specific input port."""
        for e in self._edge_map.get(node_id, []):
            if e.targetPort == port:
                # If the source is a CodeBlockNode, return the node itself for exec_assign to handle
                src_node = self._node_map.get(e.source)
                if src_node and src_node.type == "CodeBlockNode":
                    return src_node.codeBlock or f"<CodeBlock:{src_node.label}>"
                return self.resolve(e.source)
        raise RuntimeError(f"Node {node_id} missing input on port {port}")

    def eval_literal(self, n: Node) -> Any:
        return n.value

    def eval_name(self, n: Node) -> Any:
        return self.vars.get(n.value)

    def eval_binop(self, n: Node) -> Any:
        left = self._get_incoming(n.id, "left")
        right = self._get_incoming(n.id, "right")
        op_fn = BINOPS.get(n.label)
        if op_fn is None:
            raise RuntimeError(f"Unknown binary op: {n.label}")
        return op_fn(left, right)

    def eval_unaryop(self, n: Node) -> Any:
        operand = self._get_incoming(n.id, "operand")
        op_fn = UNOPS.get(n.label)
        if op_fn is None:
            raise RuntimeError(f"Unknown unary op: {n.label}")
        return op_fn(operand)

    def eval_compare(self, n: Node) -> Any:
        left = self._get_incoming(n.id, "left")
        right = self._get_incoming(n.id, "right")
        op_fn = CMPS.get(n.label)
        if op_fn is None:
            raise RuntimeError(f"Unknown compare op: {n.label}")
        return op_fn(left, right)

    def eval_call(self, n: Node) -> Any:
        callable_val = self._get_incoming(n.id, "callable")
        # Collect arg values from edges sorted by targetPort (arg_0, arg_1, ...)
        args = []
        for e in sorted(self._edge_map.get(n.id, []), key=lambda x: x.targetPort):
            if e.targetPort.startswith("arg_"):
                args.append(self.resolve(e.source))
        return callable_val(*args)

    def eval_attribute(self, n: Node) -> Any:
        obj = self._get_incoming(n.id, "object")
        return getattr(obj, n.label)

    def eval_subscr(self, n: Node) -> Any:
        val = self._get_incoming(n.id, "value")
        idx = self._get_incoming(n.id, "index")
        return val[idx]

    def eval_list_literal(self, n: Node) -> Any:
        elts = []
        for e in sorted(self._edge_map.get(n.id, []), key=lambda x: x.targetPort):
            if e.targetPort.startswith("elt_"):
                elts.append(self.resolve(e.source))
        return elts

    def eval_dict_literal(self, n: Node) -> Any:
        d = {}
        for e in self._edge_map.get(n.id, []):
            if e.targetPort.startswith("key_"):
                key = self.resolve(e.source)
                val_port = e.targetPort.replace("key_", "val_")
                val = self._get_incoming(n.id, val_port)
                d[key] = val
        return d

    def eval_tuple_literal(self, n: Node) -> Any:
        return tuple(self.eval_list_literal(n))

    def eval_CodeBlockNode(self, n: Node) -> Any:
        """Fallback: return the raw code string."""
        return n.codeBlock or f"<CodeBlock:{n.label}>"

    # ── Control nodes return sentinel values ──

    def eval_if(self, n: Node) -> bool:
        return bool(self._get_incoming(n.id, "test"))

    def eval_for(self, n: Node) -> tuple:
        target = self._get_incoming(n.id, "target")
        iter_val = self._get_incoming(n.id, "iter")
        return (target, iter_val)

    def eval_while(self, n: Node) -> Any:
        return self._get_incoming(n.id, "test")


class NameNotFound:
    """Sentinel for undefined variable access."""
    def __init__(self, name: str):
        self.name = name
    def __repr__(self):
        return f"<undefined:{self.name}>"


# ── Safe builtins injected into every execution scope ──
_SAFE_BUILTINS: dict[str, Any] = {
    "print": print,
    "len": len,
    "range": range,
    "list": list,
    "dict": dict,
    "tuple": tuple,
    "set": set,
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "type": type,
    "isinstance": isinstance,
    "abs": abs,
    "min": min,
    "max": max,
    "sum": sum,
    "sorted": sorted,
    "reversed": reversed,
    "enumerate": enumerate,
    "zip": zip,
    "map": map,
    "filter": filter,
    "hasattr": hasattr,
    "getattr": getattr,
    "setattr": setattr,
    "round": round,
    "hex": hex,
    "oct": oct,
    "chr": chr,
    "ord": ord,
    "id": id,
    "repr": repr,
    "input": input,
}


class NodeExecutor:
    """Execute statement/control nodes in sequence."""

    def __init__(self, graph: Graph):
        self.graph = graph
        self.variables: dict[str, Any] = dict(_SAFE_BUILTINS)
        self._node_map = {n.id: n for n in graph.nodes}
        self._expr_ev = ExpressionEvaluator(graph, self.variables)
        self._outgoing_body: dict[str, list[str]] = {}
        self._outgoing_orelse: dict[str, list[str]] = {}
        for e in graph.edges:
            if e.label == "body":
                self._outgoing_body.setdefault(e.source, []).append(e.target)
            elif e.label == "orelse":
                self._outgoing_orelse.setdefault(e.source, []).append(e.target)
        self._loop_break = False
        self._loop_continue = False
        self._return_value: Any = None
        self._captured_return = False

    def _body_children(self, node_id: str, fallback_children: list[str]) -> list[str]:
        return self._outgoing_body.get(node_id, fallback_children)

    def _orelse_children(self, node_id: str) -> list[str]:
        return self._outgoing_orelse.get(node_id, [])

    def reset(self):
        self.variables.clear()
        self.variables.update(_SAFE_BUILTINS)
        self._loop_break = False
        self._loop_continue = False
        self._return_value = None
        self._captured_return = False

    def execute_node(self, node_id: str) -> Any:
        node = self._node_map[node_id]
        handler = getattr(self, f"exec_{node.type}", self.exec_CodeBlockNode)
        return handler(node)

    def exec_assign(self, n: Node) -> Any:
        value = self._expr_ev._get_incoming(n.id, "value")
        # CodeBlockNode fallback: exec the code block in current scope
        if isinstance(value, str) and ("CodeBlock" in value or value.startswith("<")):
            # Get the codeBlock from the source node via edges
            code = None
            for e in self._expr_ev._edge_map.get(n.id, []):
                if e.targetPort == "value":
                    src = self._node_map.get(e.source)
                    if src and src.codeBlock:
                        code = src.codeBlock
                    break
            if code:
                try:
                    exec(f"{n.label} = {code}", self.variables)
                    return self.variables.get(n.label)
                except Exception:
                    pass
            self.variables[n.label] = value
        else:
            self.variables[n.label] = value
        return self.variables.get(n.label)

    def exec_augassign(self, n: Node) -> Any:
        """Augmented assign: x += 1, etc."""
        target_val = self._expr_ev._get_incoming(n.id, "target")
        value = self._expr_ev._get_incoming(n.id, "value")
        op_name = n.label.replace("=", "")  # "Add=" → "Add"
        if " " in op_name:
            target_name, op_name = op_name.split(" ", 1)
        else:
            target_name = n.label
        op_fn = BINOPS.get(op_name)
        if op_fn is None:
            raise RuntimeError(f"Unknown augassign op: {op_name}")
        result = op_fn(target_val, value)
        self.variables[target_name] = result
        return result

    def exec_return(self, n: Node) -> Any:
        if n.inputs:
            self._return_value = self._expr_ev._get_incoming(n.id, "value")
        else:
            self._return_value = None
        self._captured_return = True
        return self._return_value

    def exec_if(self, n: Node) -> Any:
        test_val = self._expr_ev._get_incoming(n.id, "test")
        # Handle CodeBlockNode fallback: exec the code and check result var
        if isinstance(test_val, str) and ("CodeBlock" in test_val or test_val.startswith("<")):
            test_val = False
        body_children = self._body_children(n.id, n.children)
        orelse_children = self._orelse_children(n.id)
        children = body_children if test_val else orelse_children
        for child_id in children:
            self.execute_node(child_id)
            if self._loop_break or self._loop_continue or self._captured_return:
                break
        return None

    def exec_for(self, n: Node) -> Any:
        # Get target name as string (not resolved value)
        target_edges = [e for e in self._expr_ev._edge_map.get(n.id, []) if e.targetPort == "target"]
        if target_edges:
            target_node = self._node_map[target_edges[0].source]
            target_name = target_node.value  # Name node stores the identifier string
        else:
            target_name = None
        iter_val = self._expr_ev._get_incoming(n.id, "iter")
        if iter_val is None:
            return None
        for item in iter_val:
            self.variables[target_name] = item
            for child_id in self._body_children(n.id, n.children):
                self.execute_node(child_id)
                if self._loop_break:
                    self._loop_break = False
                    break
                if self._loop_continue:
                    self._loop_continue = False
                    continue
            if self._captured_return:
                break
        return None

    def exec_while(self, n: Node) -> Any:
        while True:
            test_val = self._expr_ev._get_incoming(n.id, "test")
            # CodeBlockNode fallback: try to evaluate the code block
            if isinstance(test_val, str) and test_val.startswith("<CodeBlock"):
                code = self._node_map[n.id].codeBlock
                if code:
                    try:
                        exec(code, {}, self.variables)
                    except:
                        pass
                break
            if not test_val:
                break
            for child_id in self._body_children(n.id, n.children):
                self.execute_node(child_id)
                if self._loop_break:
                    self._loop_break = False
                    break
                if self._loop_continue:
                    self._loop_continue = False
                    continue
            if self._captured_return:
                break
        return None

    def exec_break(self, n: Node) -> Any:
        self._loop_break = True

    def exec_continue(self, n: Node) -> Any:
        self._loop_continue = True

    def exec_import(self, n: Node) -> Any:
        mod = importlib.import_module(n.label)
        self.variables[n.value or n.label.split(".")[0]] = mod
        return mod

    def exec_import_from(self, n: Node) -> Any:
        mod = __import__(n.label, fromlist=n.value or [])
        names = n.value or []
        for name in names:
            self.variables[name] = getattr(mod, name, None)
        return mod

    def exec_CodeBlockNode(self, n: Node) -> Any:
        """CodeBlockNode: try to exec the raw code in the current scope."""
        if n.codeBlock:
            try:
                exec(n.codeBlock, self.variables)
            except Exception as e:
                return f"<CodeBlock error: {e}>"
        return n.codeBlock or None

    def exec_expr(self, n: Node) -> Any:
        """Standalone expression evaluation."""
        return self._expr_ev.resolve(n.id)

    def exec_function_def(self, n: Node) -> Any:
        """Define a function in the current scope."""
        def _dynamic_fn(*args):
            old_vars = dict(self.variables)
            # Map args
            arg_names = [p.name.replace("arg_", "") for p in n.inputs]
            for an, av in zip(arg_names, args):
                self.variables[an] = av
            self._return_value = None
            self._captured_return = False
            for child_id in n.children:
                self.execute_node(child_id)
                if self._captured_return:
                    break
            result = self._return_value
            self.variables.clear()
            self.variables.update(old_vars)
            return result
        self.variables[n.label] = _dynamic_fn
        return _dynamic_fn

    def exec_class_def(self, n: Node) -> Any:
        """Define a class (simplified: create an empty type)."""
        cls_dict = {}
        for child_id in n.children:
            child = self._node_map[child_id]
            if child.type == "function_def":
                fn = self.exec_function_def(child)
                cls_dict[child.label] = fn
        cls = type(n.label, (), cls_dict)
        self.variables[n.label] = cls
        return cls


class Runtime:
    """Top-level executor. Walk root-level children and orchestrate execution."""

    def __init__(self, graph: Graph):
        self.graph = graph
        self.executor = NodeExecutor(graph)

    def run(self, entry_point="__main__") -> dict[str, Any]:
        self.executor.reset()
        # Find top-level nodes (those without a parent that has children)
        all_children = set()
        for n in self.graph.nodes:
            for c in n.children:
                all_children.add(c)
        # Root level = all nodes minus children
        root_ids = [n.id for n in self.graph.nodes if n.id not in all_children
                    or n.category == "structure"]
        # Sort by top-level children order from structure nodes
        executed = set()
        for n in self.graph.nodes:
            if n.category == "structure" and n.type == "module":
                root_ids = n.children
                break

        for node_id in root_ids:
            if node_id in executed:
                continue
            self.executor.execute_node(node_id)
            executed.add(node_id)

        return dict(self.executor.variables)


def execute_ir(ir: dict) -> dict[str, Any]:
    """Top-level entry: parse IR dict and execute."""
    graph = Graph.from_dict(ir)
    rt = Runtime(graph)
    return rt.run()
