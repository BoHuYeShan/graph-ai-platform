#!/usr/bin/env python3
"""codegen — graph-ai.json IR → canonical Python source."""

from pathlib import Path
from packages.graph_ir import Node, Edge, Graph, CATEGORY_ESCAPE

_INDENT = "    "

class PythonGenerator:
    """Convert a Graph IR back into canonical Python source."""

    def __init__(self, ir: dict):
        self.ir = ir
        self.graph = Graph.from_dict(ir)
        self._node_map = {n.id: n for n in self.graph.nodes}
        self._edge_map: dict[str, list[Edge]] = {}
        for e in self.graph.edges:
            self._edge_map.setdefault(e.source, []).append(e)
        self._out: list[str] = []
        self._indent = 0

    def _p(self, line="", indent_delta=0):
        if indent_delta < 0: self._indent += indent_delta
        if line or line == "":
            self._out.append(_INDENT * max(0, self._indent) + line)
        if indent_delta > 0: self._indent += indent_delta

    def _targets_of(self, node_id: str) -> list[Edge]:
        return self._edge_map.get(node_id, [])

    def _value_from_edge(self, edges: list[Edge], port="in") -> str:
        """Find an incoming edge to this node/port and emit the expression."""
        for e in edges:
            if e.targetPort == port:
                return self._emit_expr(e.source)
        return "?"

    # ── Expression emitter ──

    def _emit_expr(self, node_id: str) -> str:
        n = self._node_map.get(node_id)
        if not n: return "?"
        edges = self._targets_of(node_id)

        if n.type == "literal": return repr(n.value) if n.value is not None else "None"
        if n.type == "name": return str(n.value) if n.value else n.label
        if n.type == "attribute":
            obj = self._value_from_edge(edges, "object")
            return f"{obj}.{n.label}"
        if n.type == "binop":
            left = self._value_from_edge(edges, "left")
            op = n.label  # Add, Sub, Mult, Div...
            op_map = {"Add":"+","Sub":"-","Mult":"*","Div":"/","FloorDiv":"//","Mod":"%","Pow":"**"}
            return f"{left} {op_map.get(op,'?')} {self._value_from_edge(edges,'right')}"
        if n.type == "unaryop":
            op_map = {"UAdd":"+","USub":"-","Not":"not "}
            return f"{op_map.get(n.label,'?')}{self._value_from_edge(edges,'operand')}"
        if n.type == "call":
            fn = self._value_from_edge(edges, "callable")
            args = []
            for e in sorted(edges, key=lambda x: x.targetPort):
                if e.targetPort.startswith("arg_"):
                    args.append(self._emit_expr(e.source))
            return f"{fn}({', '.join(args)})"
        if n.type == "subscr":
            value = self._value_from_edge(edges, "value")
            index = self._value_from_edge(edges, "index")
            return f"{value}[{index}]"
        if n.type == "list_literal":
            elts = [self._emit_expr(e.source) for e in sorted(edges, key=lambda x: x.targetPort)]
            return f"[{', '.join(elts)}]"
        if n.type == "CodeBlockNode":
            code = n.codeBlock or ""
            return f"  # CodeBlockNode: {code.strip()[:50]}...  "
        return "?"

    # ═══════════════════════════════════════════
    #  Statement generator
    # ═══════════════════════════════════════════

    def _emit_stmt(self, node_id: str, body_only=False):
        n = self._node_map.get(node_id)
        if not n: return
        edges = self._targets_of(node_id)

        if n.type == "assign":
            val = self._value_from_edge(edges, "value")
            self._p(f"{n.label.lstrip('= ')} = {val}")
        elif n.type == "return":
            val = self._value_from_edge(edges, "value") if edges else ""
            self._p(f"return {val}" if val else "return")
        elif n.type == "if":
            test = self._value_from_edge(edges, "test")
            self._p(f"if {test}:", indent_delta=1)
            for child in self._children_of(n): self._emit_stmt(child)
            self._p("", indent_delta=-1)
        elif n.type == "for":
            target_expr = self._value_from_edge(edges, "target")
            iter_expr = self._value_from_edge(edges, "iter")
            self._p(f"for {target_expr} in {iter_expr}:", indent_delta=1)
            for child in self._children_of(n): self._emit_stmt(child)
            self._p("", indent_delta=-1)
        elif n.type == "while":
            test = self._value_from_edge(edges, "test")
            self._p(f"while {test}:", indent_delta=1)
            for child in self._children_of(n): self._emit_stmt(child)
            self._p("", indent_delta=-1)
        elif n.type == "break":
            self._p("break")
        elif n.type == "continue":
            self._p("continue")
        elif n.type == "import":
            asname = f" as {n.value}" if n.value else ""
            self._p(f"import {n.label}{asname}")
        elif n.type == "import_from":
            names = ", ".join(n.value) if isinstance(n.value, list) else n.label
            self._p(f"from {n.label} import {names}")
        elif n.type == "function_def":
            args = [f"a_{i}" for i in range(len(n.inputs))]
            self._p(f"def {n.label}({', '.join(args)}):", indent_delta=1)
            for child in self._children_of(n): self._emit_stmt(child)
            self._p("", indent_delta=-1)
        elif n.type == "class_def":
            self._p(f"class {n.label}:", indent_delta=1)
            for child in self._children_of(n): self._emit_stmt(child)
            self._p("", indent_delta=-1)
        elif n.type == "CodeBlockNode":
            code = n.codeBlock or ""
            for line in code.split("\n"):
                self._p(f"# FB: {line}")
        else:
            # expression statement
            pass

    def _children_of(self, n: Node) -> list[str]:
        """Return IDs of child nodes (body of if/for/function/class)."""
        children = []
        for edge in self.graph.edges:
            if edge.source == n.id and edge.targetPort in ("body",):
                children.append(edge.target)
        return children

    # ═══════════════════════════════════════════
    #  Main entry
    # ═══════════════════════════════════════════

    def generate(self) -> str:
        # Emit module-level statements in order of appearance (sourceMap-based)
        nodes_by_line = []
        for n in self.graph.nodes:
            sm = self.ir.get("sourceMap", {}).get(n.id, {})
            line = sm.get("lineStart", 999999)
            if n.type in ("literal","name","binop","unaryop","attribute","subscr",
                          "list_literal","call"):
                continue  # skip expression nodes (embedded in statements)
            nodes_by_line.append((line, n.id))
        nodes_by_line.sort()

        for _, nid in nodes_by_line:
            self._emit_stmt(nid)

        return "\n".join(self._out)


def generate(ir: dict) -> str:
    return PythonGenerator(ir).generate()


def generate_file(in_path, out_path) -> str:
    import json
    ir = json.loads(Path(in_path).read_text(encoding="utf-8"))
    code = generate(ir)
    Path(out_path).write_text(code, encoding="utf-8")
    return code
