#!/usr/bin/env python3
"""ai_editor — LLM-based IR editing: natural language → graph-ai edits."""

from __future__ import annotations
from typing import Any, Optional
import json, os, sys

_here = os.path.dirname(__file__)
_platform = os.path.abspath(os.path.join(_here, "..", ".."))
if _platform not in sys.path:
    sys.path.insert(0, _platform)

from services.core.normalize_service import validate_ir, auto_fix


class AIEditor:
    """Apply LLM-suggested edits to a graph-ai IR.

    The LLM returns structured 'patches' (add/update/delete node/edge operations).
    This class applies them safely.
    """

    def __init__(self, ir: dict):
        self.ir = ir

    def apply_patch(self, patch: dict) -> dict:
        """Apply one structured patch to IR.

        Patch format:
          {"op": "add_node", "node": {...}}
          {"op": "update_node", "id": "...", "updates": {...}}
          {"op": "delete_node", "id": "..."}
          {"op": "add_edge", "edge": {...}}
          {"op": "delete_edge", "id": "..."}
        """
        op = patch.get("op")
        if op == "add_node":
            node = patch["node"]
            if "id" not in node:
                node["id"] = f"node_ai_{len(self.ir['graph']['nodes'])}"
            self.ir["graph"]["nodes"].append(node)

        elif op == "update_node":
            nid = patch["id"]
            for n in self.ir["graph"]["nodes"]:
                if n["id"] == nid:
                    n.update(patch.get("updates", {}))
                    break

        elif op == "delete_node":
            nid = patch["id"]
            self.ir["graph"]["nodes"] = [n for n in self.ir["graph"]["nodes"] if n["id"] != nid]
            self.ir["graph"]["edges"] = [e for e in self.ir["graph"]["edges"]
                                          if e["source"] != nid and e["target"] != nid]

        elif op == "add_edge":
            edge = patch["edge"]
            if "id" not in edge:
                edge["id"] = f"edge_ai_{len(self.ir['graph']['edges'])}"
            self.ir["graph"]["edges"].append(edge)

        elif op == "delete_edge":
            eid = patch["id"]
            self.ir["graph"]["edges"] = [e for e in self.ir["graph"]["edges"] if e["id"] != eid]

        # Validate and fix after patch
        issues = validate_ir(self.ir)
        if issues:
            self.ir = auto_fix(self.ir, issues)

        return self.ir

    def apply_patches(self, patches: list[dict]) -> dict:
        for p in patches:
            self.apply_patch(p)
        return self.ir


# ── Prompt templates for LLM calls ──

SYSTEM_PROMPT = """You are a graph-ai IR editor. You receive a graph-ai.json IR and a user request.
You respond with a JSON array of patch operations that modify the IR to match the user's intent.

Available patch operations:
  {"op": "add_node", "node": {"category": "data|action|control|structure", "type": "...", "label": "...", "inputs": [...], "outputs": [...]}}
  {"op": "update_node", "id": "...", "updates": {"label": "...", ...}}
  {"op": "delete_node", "id": "..."}
  {"op": "add_edge", "edge": {"source": "...", "target": "...", "sourcePort": "out", "targetPort": "in"}}
  {"op": "delete_edge", "id": "..."}

Node types: literal, name, binop, unaryop, compare, call, attribute, subscr, list_literal
            assign, augassign, return, if, for, while, break, continue
            import, import_from, function_def, class_def
            CodeBlockNode (fallback)

Respond ONLY with the JSON array, no other text."""


def build_edit_prompt(ir: dict, user_request: str) -> str:
    """Build the full prompt for the LLM."""
    ir_str = json.dumps(ir, indent=2, ensure_ascii=False)
    return f"""Current IR:
```json
{ir_str}
```

User request:
{user_request}

Respond with patch operations:"""


def parse_llm_response(response: str) -> list[dict]:
    """Extract patch operations from LLM response."""
    content = response.strip()
    if content.startswith("```"):
        lines = content.split("\n")
        # Remove code fence
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        content = "\n".join(lines)
    try:
        patches = json.loads(content)
        return patches if isinstance(patches, list) else [patches]
    except json.JSONDecodeError:
        return [{"op": "error", "message": f"Could not parse LLM response: {response[:200]}"}]
