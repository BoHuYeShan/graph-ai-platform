#!/usr/bin/env python3
"""parser — Python source code → graph-ai.json IR (MVP subset)."""

import ast
from pathlib import Path
from packages.graph_ir import (
    Graph, Node, Edge, PortDef, Scope,
    NODE_TYPES, CATEGORY_ESCAPE, generate_id,
    build_ir,
)

# ── Helper: create an expression/data node ──
def _make_expr(node_id: str, label: str, pytype: str, value=None) -> Node:
    return Node(id=node_id, category=NODE_TYPES.get(pytype, CATEGORY_ESCAPE),
                type=pytype, label=label, value=value,
                inputs=[PortDef("in")], outputs=[PortDef("out")])

def _make_code_block(node_id: str, code: str) -> Node:
    return Node(id=node_id, category=CATEGORY_ESCAPE, type="CodeBlockNode",
                label="Code Block (fallback)", codeBlock=code,
                inputs=[], outputs=[PortDef("out")])


class PythonParser:
    """Convert Python ast.Module → Graph IR."""

    def __init__(self, source: str, filename="<unknown>"):
        self.source = source
        self.filename = filename
        self.graph = Graph()
        self.source_map = {}
        self._expr_counter = 0
        self._last_stmt_id = None

    def _new_id(self, prefix="n") -> str:
        self._expr_counter += 1
        return f"node_{prefix}_{self._expr_counter}"

    def _record_source(self, node_id: str, ast_node: ast.AST):
        if hasattr(ast_node, 'lineno'):
            self.source_map[node_id] = {
                "lineStart": ast_node.lineno, "lineEnd": getattr(ast_node, 'end_lineno', ast_node.lineno),
                "colStart": ast_node.col_offset, "colEnd": getattr(ast_node, 'end_col_offset', ast_node.col_offset),
                "sourceFile": self.filename,
            }

    # ═══════════════════════════════════════════
    #  Expression visitors (return Node)
    # ═══════════════════════════════════════════

    def visit_Constant(self, n: ast.Constant) -> Node:
        node = _make_expr(self._new_id("lit"), repr(n.value), "literal", n.value)
        self._record_source(node.id, n)
        self.graph.add_node(node)
        return node

    def visit_Name(self, n: ast.Name) -> Node:
        node = _make_expr(self._new_id("name"), n.id, "name", n.id)
        self._record_source(node.id, n)
        self.graph.add_node(node)
        return node

    def visit_Attribute(self, n: ast.Attribute) -> Node:
        obj = self.visit_expr(n.value)
        node_id = self._new_id("attr")
        node = Node(id=node_id, category="data", type="attribute", label=n.attr,
                    inputs=[PortDef("object")], outputs=[PortDef("out")])
        self._record_source(node_id, n)
        self.graph.add_node(node)
        self.graph.add_edge(obj.id, node_id, "out", "object")
        return node

    def visit_BinOp(self, n: ast.BinOp) -> Node:
        left = self.visit_expr(n.left)
        right = self.visit_expr(n.right)
        op_name = type(n.op).__name__
        node_id = self._new_id("binop")
        node = Node(id=node_id, category="data", type="binop", label=op_name,
                    inputs=[PortDef("left"), PortDef("right")], outputs=[PortDef("out")])
        self._record_source(node_id, n)
        self.graph.add_node(node)
        self.graph.add_edge(left.id, node_id, "out", "left")
        self.graph.add_edge(right.id, node_id, "out", "right")
        return node

    def visit_UnaryOp(self, n: ast.UnaryOp) -> Node:
        operand = self.visit_expr(n.operand)
        node_id = self._new_id("unaryop")
        node = Node(id=node_id, category="data", type="unaryop",
                    label=f"{type(n.op).__name__}", inputs=[PortDef("operand")], outputs=[PortDef("out")])
        self._record_source(node_id, n)
        self.graph.add_node(node)
        self.graph.add_edge(operand.id, node_id, "out", "operand")
        return node

    def visit_Call(self, n: ast.Call) -> Node:
        func = self.visit_expr(n.func)
        node_id = self._new_id("call")
        inputs = [PortDef(f"arg_{i}") for i in range(len(n.args))]
        node = Node(id=node_id, category="action", type="call", label="call",
                    inputs=inputs, outputs=[PortDef("result")])
        self._record_source(node_id, n)
        self.graph.add_node(node)
        self.graph.add_edge(func.id, node_id, "out", "callable")
        for i, arg in enumerate(n.args):
            arg_node = self.visit_expr(arg)
            self.graph.add_edge(arg_node.id, node_id, f"arg_{i}")
        return node

    def visit_Subscript(self, n: ast.Subscript) -> Node:
        value = self.visit_expr(n.value)
        sl = self.visit_expr(n.slice) if isinstance(n.slice, ast.expr) else None
        node_id = self._new_id("subscr")
        node = Node(id=node_id, category="data", type="subscr", label="[]",
                    inputs=[PortDef("value"), PortDef("index")], outputs=[PortDef("out")])
        self._record_source(node_id, n)
        self.graph.add_node(node)
        self.graph.add_edge(value.id, node_id, "out", "value")
        if sl: self.graph.add_edge(sl.id, node_id, "out", "index")
        return node

    def visit_List(self, n: ast.List) -> Node:
        node_id = self._new_id("list")
        inputs = [PortDef(f"elt_{i}") for i in range(len(n.elts))]
        node = Node(id=node_id, category="data", type="list_literal", label="list",
                    inputs=inputs, outputs=[PortDef("out")])
        self._record_source(node_id, n)
        self.graph.add_node(node)
        for i, elt in enumerate(n.elts):
            elt_node = self.visit_expr(elt)
            self.graph.add_edge(elt_node.id, node_id, "out", f"elt_{i}")
        return node

    # Fallback: unsupported expression → CodeBlockNode
    def _fallback_expr(self, n: ast.expr) -> Node:
        code = ast.get_source_segment(self.source, n) or "?"
        node = _make_code_block(self._new_id("fb"), code)
        self._record_source(node.id, n)
        self.graph.add_node(node)
        return node

    def visit_expr(self, n: ast.expr) -> Node:
        if isinstance(n, ast.Constant): return self.visit_Constant(n)
        if isinstance(n, ast.Name): return self.visit_Name(n)
        if isinstance(n, ast.BinOp): return self.visit_BinOp(n)
        if isinstance(n, ast.UnaryOp): return self.visit_UnaryOp(n)
        if isinstance(n, ast.Call): return self.visit_Call(n)
        if isinstance(n, ast.Attribute): return self.visit_Attribute(n)
        if isinstance(n, ast.Subscript): return self.visit_Subscript(n)
        if isinstance(n, ast.List): return self.visit_List(n)
        if isinstance(n, ast.Tuple): return self._fallback_expr(n)  # TODO
        if isinstance(n, ast.Dict): return self._fallback_expr(n)   # TODO
        return self._fallback_expr(n)

    # ═══════════════════════════════════════════
    #  Statement visitors (return node ID or None)
    # ═══════════════════════════════════════════

    def _add(self, node: Node) -> str:
        self.graph.add_node(node)
        self._last_stmt_id = node.id
        return node.id

    def visit_Expr(self, n: ast.Expr) -> str | None:
        return self.visit_expr(n.value).id if self.visit_expr(n.value) else None

    def visit_Assign(self, n: ast.Assign) -> str | None:
        value = self.visit_expr(n.value)
        for target in n.targets:
            if isinstance(target, ast.Name):
                node_id = self._new_id("assign")
                node = Node(id=node_id, category="action", type="assign", label=target.id,
                            inputs=[PortDef("value")], outputs=[])
                self._record_source(node_id, n)
                self._add(node)
                self.graph.add_edge(value.id, node_id, "out", "value")
                self.graph.variables[target.id] = f"var_{self._expr_counter}"
                return node_id
            else:
                return self._fallback_stmt(n)
        return None

    def visit_AugAssign(self, n: ast.AugAssign) -> str | None:
        target = self.visit_expr(n.target)
        value = self.visit_expr(n.value)
        node_id = self._new_id("augassign")
        op_name = type(n.op).__name__
        node = Node(id=node_id, category="action", type="assign", label=f"{op_name}=",
                    inputs=[PortDef("target"), PortDef("value")], outputs=[])
        self._record_source(node_id, n)
        self.graph.add_node(node)
        self.graph.add_edge(target.id, node_id, "out", "target")
        self.graph.add_edge(value.id, node_id, "out", "value")

    def visit_Return(self, n: ast.Return) -> str | None:
        if n.value:
            val = self.visit_expr(n.value)
            node_id = self._new_id("return")
            node = Node(id=node_id, category="control", type="return", label="return",
                        inputs=[PortDef("value")], outputs=[])
            self._record_source(node_id, n)
            self._add(node)
            self.graph.add_edge(val.id, node_id, "out", "value")
            return node_id
        node_id = self._new_id("return")
        node = Node(id=node_id, category="control", type="return", label="return",
                    inputs=[], outputs=[])
        self._record_source(node_id, n)
        self._add(node)
        return node_id

    def visit_If(self, n: ast.If):
        test = self.visit_expr(n.test)
        if_id = self._new_id("if")
        if_node = Node(id=if_id, category="control", type="if", label="if",
                       inputs=[PortDef("test", type="bool")],
                       children=[], outputs=[PortDef("body"), PortDef("orelse")])
        self._record_source(if_id, n)
        self.graph.add_node(if_node)
        self.graph.add_edge(test.id, if_id, "out", "test")
        for stmt in n.body:
            sid = self.visit_stmt(stmt)
            if sid: if_node.children.append(sid)
        for stmt in n.orelse:
            sid = self.visit_stmt(stmt)
            if sid: if_node.children.append(sid)

    def visit_For(self, n: ast.For):
        target = self.visit_expr(n.target)
        iter_val = self.visit_expr(n.iter)
        for_id = self._new_id("for")
        for_node = Node(id=for_id, category="control", type="for", label="for",
                        inputs=[PortDef("target"), PortDef("iter")],
                        children=[], outputs=[])
        self._record_source(for_id, n)
        self._add(for_node)
        self.graph.add_edge(target.id, for_id, "out", "target")
        self.graph.add_edge(iter_val.id, for_id, "out", "iter")
        for stmt in n.body:
            sid = self.visit_stmt(stmt)
            if sid: for_node.children.append(sid)

    def visit_While(self, n: ast.While):
        test = self.visit_expr(n.test)
        while_id = self._new_id("while")
        while_node = Node(id=while_id, category="control", type="while", label="while",
                          inputs=[PortDef("test", type="bool")], children=[], outputs=[])
        self._record_source(while_id, n)
        self._add(while_node)
        self.graph.add_edge(test.id, while_id, "out", "test")
        for stmt in n.body:
            sid = self.visit_stmt(stmt)
            if sid: while_node.children.append(sid)
        for stmt in n.orelse:
            sid = self.visit_stmt(stmt)
            if sid: while_node.children.append(sid)

    def visit_Break(self, n: ast.Break):
        node = Node(id=self._new_id("break"), category="control", type="break", label="break", inputs=[], outputs=[])
        self._record_source(node.id, n)
        self._add(node)
        return node.id

    def visit_Continue(self, n: ast.Continue):
        node = Node(id=self._new_id("continue"), category="control", type="continue", label="continue", inputs=[], outputs=[])
        self._record_source(node.id, n)
        self._add(node)

    def visit_FunctionDef(self, n: ast.FunctionDef):
        fn_id = self._new_id("fn")
        fn_node = Node(id=fn_id, category="structure", type="function_def", label=n.name,
                       inputs=[PortDef(f"arg_{a.arg}") for a in n.args.args],
                       children=[], outputs=[PortDef("result")])
        self._record_source(fn_id, n)
        self._add(fn_node)
        for stmt in n.body:
            sid = self.visit_stmt(stmt)
            if sid: fn_node.children.append(sid)

    def visit_ClassDef(self, n: ast.ClassDef):
        cls_id = self._new_id("cls")
        cls_node = Node(id=cls_id, category="structure", type="class_def", label=n.name,
                        inputs=[], children=[], outputs=[])
        self._record_source(cls_id, n)
        self._add(cls_node)
        for stmt in n.body:
            sid = self.visit_stmt(stmt)
            if sid: cls_node.children.append(sid)

    def visit_Import(self, n: ast.Import):
        for alias in n.names:
            node = Node(id=self._new_id("import"), category="action", type="import",
                        label=alias.name, value=alias.asname, inputs=[], outputs=[])
            self._add(node)

    def visit_ImportFrom(self, n: ast.ImportFrom):
        node = Node(id=self._new_id("import"), category="action", type="import_from",
                    label=n.module or ".", value=[a.name for a in n.names], inputs=[], outputs=[])
        self._add(node)

    def _fallback_stmt(self, n: ast.stmt):
        code = ast.get_source_segment(self.source, n) or "?"
        node = _make_code_block(self._new_id("fb"), code)
        self._record_source(node.id, n)
        self.graph.add_node(node)

    def visit_stmt(self, n: ast.stmt):
        if isinstance(n, ast.Expr): return self.visit_Expr(n)
        if isinstance(n, ast.Assign): return self.visit_Assign(n)
        if isinstance(n, ast.AugAssign): return self.visit_AugAssign(n)
        if isinstance(n, ast.Return): return self.visit_Return(n)
        if isinstance(n, ast.If): return self.visit_If(n)
        if isinstance(n, ast.For): return self.visit_For(n)
        if isinstance(n, ast.While): return self.visit_While(n)
        if isinstance(n, ast.Break): return self.visit_Break(n)
        if isinstance(n, ast.Continue): return self.visit_Continue(n)
        if isinstance(n, ast.FunctionDef): return self.visit_FunctionDef(n)
        if isinstance(n, ast.ClassDef): return self.visit_ClassDef(n)
        if isinstance(n, ast.Import): return self.visit_Import(n)
        if isinstance(n, ast.ImportFrom): return self.visit_ImportFrom(n)
        if isinstance(n, ast.Pass): pass  # skip
        self._fallback_stmt(n)

    # ═══════════════════════════════════════════
    #  Main entry
    # ═══════════════════════════════════════════

    def parse(self) -> dict:
        tree = ast.parse(self.source, filename=self.filename)
        for stmt in tree.body:
            self.visit_stmt(stmt)
        raw = self.graph.to_dict()
        full = build_ir(raw)
        full["sourceMap"] = self.source_map
        full["metadata"]["generatedAt"] = "__NOW__"
        return full


def parse_source(source: str, filename="<unknown>") -> dict:
    return PythonParser(source, filename).parse()


def parse_file(path: str) -> dict:
    p = Path(path)
    return PythonParser(p.read_text(encoding="utf-8"), str(p)).parse()
