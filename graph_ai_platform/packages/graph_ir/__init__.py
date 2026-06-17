#!/usr/bin/env python3
"""graph_ir — core data model for graph-ai.json."""

from __future__ import annotations
import json, uuid
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional

# ── Node categories ──
CATEGORY_CONTROL   = "control"
CATEGORY_STRUCTURE = "structure"
CATEGORY_ACTION    = "action"
CATEGORY_DATA      = "data"
CATEGORY_ESCAPE    = "escape"

# ── Node types (by category) ──
NODE_TYPES = {
    # control
    "if": CATEGORY_CONTROL, "elif": CATEGORY_CONTROL, "else": CATEGORY_CONTROL,
    "for": CATEGORY_CONTROL, "while": CATEGORY_CONTROL,
    "break": CATEGORY_CONTROL, "continue": CATEGORY_CONTROL, "return": CATEGORY_CONTROL,
    # structure
    "function_def": CATEGORY_STRUCTURE, "class_def": CATEGORY_STRUCTURE, "module": CATEGORY_STRUCTURE,
    # action
    "assign": CATEGORY_ACTION, "expr": CATEGORY_ACTION, "call": CATEGORY_ACTION,
    "import": CATEGORY_ACTION, "import_from": CATEGORY_ACTION,
    # data
    "literal": CATEGORY_DATA, "name": CATEGORY_DATA, "attribute": CATEGORY_DATA,
    "binop": CATEGORY_DATA, "unaryop": CATEGORY_DATA, "compare": CATEGORY_DATA,
    "subscr": CATEGORY_DATA, "list_literal": CATEGORY_DATA, "dict_literal": CATEGORY_DATA,
    "tuple_literal": CATEGORY_DATA,
}

def generate_id() -> str:
    return f"node_{uuid.uuid4().hex[:8]}"

@dataclass
class PortDef:
    name: str
    type: str = "any"
    optional: bool = False

@dataclass
class Node:
    id: str
    category: str
    type: str
    label: str
    value: object = None
    inputs: list[PortDef] = field(default_factory=list)
    outputs: list[PortDef] = field(default_factory=list)
    children: list[str] = field(default_factory=list)
    codeBlock: Optional[str] = None  # for CodeBlockNode fallback

    def to_dict(self) -> dict:
        d = {"id": self.id, "category": self.category, "type": self.type, "label": self.label,
             "inputs": [asdict(p) for p in self.inputs],
             "outputs": [asdict(p) for p in self.outputs]}
        if self.value is not None: d["value"] = self.value
        if self.children: d["children"] = self.children
        if self.codeBlock: d["codeBlock"] = self.codeBlock
        return d

@dataclass
class Edge:
    id: str
    source: str
    target: str
    sourcePort: str = "out"
    targetPort: str = "in"
    label: str = ""

@dataclass
class Scope:
    id: str
    parent: Optional[str] = None
    nodes: list[str] = field(default_factory=list)

@dataclass
class Graph:
    nodes: list[Node] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
    variables: dict[str, str] = field(default_factory=dict)
    scopes: list[Scope] = field(default_factory=list)

    def add_node(self, node: Node) -> Node:
        self.nodes.append(node)
        return node

    def add_edge(self, source: str, target: str, sourcePort="out", targetPort="in", label="") -> Edge:
        edge = Edge(id=f"edge_{uuid.uuid4().hex[:8]}", source=source, target=target,
                     sourcePort=sourcePort, targetPort=targetPort, label=label)
        self.edges.append(edge)
        return edge

    def to_dict(self) -> dict:
        return {
            "graph": {
                "nodes": [n.to_dict() for n in self.nodes],
                "edges": [asdict(e) for e in self.edges],
                "variables": self.variables,
                "scopes": [asdict(s) for s in self.scopes],
            }
        }

    def to_json(self, indent=2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: dict) -> "Graph":
        g = cls()
        g.nodes = [Node(**n) for n in data.get("graph", {}).get("nodes", [])]
        g.edges = [Edge(**e) for e in data.get("graph", {}).get("edges", [])]
        g.variables = data.get("graph", {}).get("variables", {})
        g.scopes = [Scope(**s) for s in data.get("graph", {}).get("scopes", [])]
        return g


def build_ir(parser_output: dict) -> dict:
    """Wrap parser output + view + sourceMap + metadata into full graph-ai.json."""
    return {
        "graph": parser_output["graph"],
        "view": {
            "nodePositions": {},
            "theme": "default",
        },
        "sourceMap": parser_output.get("sourceMap", {}),
        "metadata": {
            "irVersion": "0.1.0",
            "pythonSubset": "mvp-0.1",
            "generatedAt": "__NOW__",
            "generatedBy": "parser",
        },
    }
