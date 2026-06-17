#!/usr/bin/env python3
"""normalize_service — IR validation and auto-fix utilities."""

from __future__ import annotations
from typing import Any


def validate_ir(ir: dict) -> list[dict]:
    """Validate a graph-ai IR, returning a list of issues.

    Each issue: {type, severity, node_id?, edge_id?, message}
    """
    issues = []
    graph = ir.get("graph", {})
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    node_ids = {n["id"] for n in nodes}

    # ── Check edges refer to valid nodes ──
    for e in edges:
        if e["source"] not in node_ids:
            issues.append({
                "type": "dangling_source",
                "severity": "error",
                "edge_id": e["id"],
                "message": f"Edge references source {e['source']} not found in nodes",
            })
        if e["target"] not in node_ids:
            issues.append({
                "type": "dangling_target",
                "severity": "error",
                "edge_id": e["id"],
                "message": f"Edge references target {e['target']} not found in nodes",
            })

    # ── Check children refs are valid ──
    for n in nodes:
        for child_id in n.get("children", []):
            if child_id not in node_ids and child_id != "?":
                issues.append({
                    "type": "dangling_child",
                    "severity": "error",
                    "node_id": n["id"],
                    "message": f"Node {n['id']} references child {child_id} not found",
                })

    # ── Check required fields ──
    required_fields = ["id", "category", "type", "label"]
    for n in nodes:
        for f in required_fields:
            if f not in n or n[f] is None:
                issues.append({
                    "type": "missing_field",
                    "severity": "error",
                    "node_id": n.get("id", "?"),
                    "message": f"Node missing required field '{f}'",
                })

    # ── Metadata checks ──
    meta = ir.get("metadata", {})
    if "irVersion" not in meta:
        issues.append({"type": "missing_metadata", "severity": "warning",
                        "message": "Missing irVersion in metadata"})

    return issues


def auto_fix(ir: dict, issues: list[dict]) -> dict:
    """Apply auto-fixes for known issue types.

    Supported fixes:
      - Remove dangling edges (source or target missing)
      - Remove children refs pointing to nonexistent nodes
    """
    graph = ir.get("graph", {})
    fixed = ir.copy()

    # Collect IDs to remove
    remove_edge_ids = set()
    remove_child_refs = {}  # node_id → [child_id, ...]

    for iss in issues:
        if iss["type"] in ("dangling_source", "dangling_target"):
            remove_edge_ids.add(iss["edge_id"])
        elif iss["type"] == "dangling_child":
            nid = iss["node_id"]
            remove_child_refs.setdefault(nid, []).append(...)
            # Find the actual child_id from the message
            msg = iss.get("message", "")
            for cn in fixed.get("graph", {}).get("nodes", []):
                if cn["id"] == nid:
                    for c in cn.get("children", []):
                        if c not in {n["id"] for n in fixed["graph"]["nodes"]}:
                            remove_child_refs.setdefault(nid, []).append(c)

    # Apply edge removal
    if remove_edge_ids:
        fixed["graph"]["edges"] = [e for e in graph.get("edges", [])
                                    if e["id"] not in remove_edge_ids]

    # Apply child ref cleanup
    for n in fixed["graph"]["nodes"]:
        if n["id"] in remove_child_refs:
            bad = set(remove_child_refs[n["id"]])
            n["children"] = [c for c in n.get("children", []) if c not in bad]

    return fixed
