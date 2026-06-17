#!/usr/bin/env python3
"""node_catalog — registry of all graph-ai node types with port specs + doc."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from packages.graph_ir import PortDef, NODE_TYPES

@dataclass
class NodeSpec:
    type: str
    category: str
    label: str
    description: str
    inputs: list[PortDef]
    outputs: list[PortDef]
    can_have_children: bool = False

class NodeCatalog:
    _registry: dict[str, NodeSpec] = {}

    @classmethod
    def register(cls, spec: NodeSpec):
        cls._registry[spec.type] = spec

    @classmethod
    def get(cls, type_name: str) -> NodeSpec | None:
        return cls._registry.get(type_name)

    @classmethod
    def list(cls, category: str | None = None) -> list[NodeSpec]:
        if category:
            return [s for s in cls._registry.values() if s.category == category]
        return list(cls._registry.values())

    @classmethod
    def to_markdown(cls) -> str:
        lines = ["# Node Catalog — graph-ai IR", ""]
        for cat in ("control", "structure", "action", "data", "escape"):
            items = cls.list(cat)
            if not items:
                continue
            lines.append(f"## {cat.upper()}")
            for s in items:
                ins = ", ".join(f"{p.name}: {p.type}" for p in s.inputs) or "—"
                outs = ", ".join(f"{p.name}: {p.type}" for p in s.outputs) or "—"
                lines.append(f"- **`{s.type}`** — {s.description}")
                lines.append(f"  - inputs=[{ins}]  outputs=[{outs}]  children={s.can_have_children}")
            lines.append("")
        return "\n".join(lines)
