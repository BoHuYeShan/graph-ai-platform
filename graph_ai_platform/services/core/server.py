#!/usr/bin/env python3
"""core — FastAPI backend for graph-ai platform: parse, generate, normalize, execute."""

from __future__ import annotations
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Optional
import os, sys

# ── Ensure parent is on path for imports ──
_here = os.path.dirname(__file__)
_platform = os.path.abspath(os.path.join(_here, "..", ".."))
if _platform not in sys.path:
    sys.path.insert(0, _platform)

from packages.parser import parse_source
from packages.codegen import generate as codegen_generate
from services.runtime import execute_ir
from services.core.normalize_service import validate_ir, auto_fix
from services.core.ai_editor import AIEditor, build_edit_prompt, parse_llm_response, SYSTEM_PROMPT

app = FastAPI(title="graph-ai Platform API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ── Request / Response models ──

class ParseRequest(BaseModel):
    source: str
    filename: str = "<source>"

class IRResponse(BaseModel):
    ir: dict
    status: str = "ok"

class CodegenRequest(BaseModel):
    ir: dict

class ExecuteRequest(BaseModel):
    ir: dict

class NormalizeRequest(BaseModel):
    ir: dict

class AIEditRequest(BaseModel):
    ir: dict
    instruction: str

class PromptRequest(BaseModel):
    ir: dict
    instruction: str

class LintRequest(BaseModel):
    source: str

class LintResult(BaseModel):
    line: int
    col: int
    message: str
    severity: str  # "error" | "warning"

class LintResponse(BaseModel):
    issues: list[LintResult]

# ── Endpoints ──

@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}

@app.post("/parse", response_model=IRResponse)
def parse_endpoint(req: ParseRequest):
    try:
        ir = parse_source(req.source, req.filename)
        return IRResponse(ir=ir)
    except SyntaxError as e:
        raise HTTPException(400, f"Syntax error: {e}")
    except Exception as e:
        raise HTTPException(500, f"Parse error: {e}")

@app.post("/codegen")
def codegen_endpoint(req: CodegenRequest):
    try:
        code = codegen_generate(req.ir)
        return {"code": code, "status": "ok"}
    except Exception as e:
        raise HTTPException(500, f"Codegen error: {e}")

@app.post("/execute")
def execute_endpoint(req: ExecuteRequest):
    try:
        result = execute_ir(req.ir)
        return {"variables": result, "status": "ok"}
    except Exception as e:
        raise HTTPException(500, f"Execute error: {e}")

@app.post("/normalize")
def normalize_endpoint(req: NormalizeRequest):
    """Validate and auto-fix an IR graph."""
    try:
        ir = req.ir
        issues = validate_ir(ir)
        if issues:
            ir = auto_fix(ir, issues)
        return {"ir": ir, "issues": issues, "status": "ok"}
    except Exception as e:
        raise HTTPException(500, f"Normalize error: {e}")

@app.post("/lint")
def lint_endpoint(req: LintRequest):
    """Check Python source for syntax errors."""
    import ast, traceback
    issues = []
    source = req.source
    try:
        ast.parse(source)
    except SyntaxError as e:
        issues.append(LintResult(
            line=e.lineno or 1,
            col=e.offset or 1,
            message=f"SyntaxError: {e.msg}",
            severity="error",
        ))
    except Exception as e:
        issues.append(LintResult(
            line=1, col=1,
            message=f"Parse error: {e}",
            severity="error",
        ))
    return LintResponse(issues=issues)

@app.post("/ai/edit")
def ai_edit_endpoint(req: AIEditRequest):
    """Apply AI-generated patches to IR."""
    try:
        editor = AIEditor(req.ir)
        # In real deployment, call LLM here. For now, return the prompt.
        return {
            "status": "prompt_only",
            "prompt": build_edit_prompt(req.ir, req.instruction),
            "system_prompt": SYSTEM_PROMPT,
        }
    except Exception as e:
        raise HTTPException(500, f"AI edit error: {e}")

@app.post("/ai/prompt")
def ai_prompt_endpoint(req: PromptRequest):
    """Build the full prompt for the LLM (for external AI integration)."""
    return {
        "system_prompt": SYSTEM_PROMPT,
        "user_prompt": build_edit_prompt(req.ir, req.instruction),
    }

@app.post("/ai/apply")
def ai_apply_endpoint(req: AIEditRequest):
    """Directly apply a list of patches (bypass LLM, for testing)."""
    try:
        editor = AIEditor(req.ir)
        patches = parse_llm_response(req.instruction)
        ir = editor.apply_patches(patches)
        return {"ir": ir, "patches_applied": len(patches), "status": "ok"}
    except Exception as e:
        raise HTTPException(500, f"AI apply error: {e}")


# ── Normalization service ──

def validate_ir(ir: dict) -> list[dict]:
    """Return list of issues found in the IR."""
    issues = []
    nodes = ir.get("graph", {}).get("nodes", [])
    edges = ir.get("graph", {}).get("edges", [])
    node_ids = {n["id"] for n in nodes}
    for e in edges:
        if e["source"] not in node_ids:
            issues.append({"type": "dangling_edge", "edge_id": e["id"], "field": "source"})
        if e["target"] not in node_ids:
            issues.append({"type": "dangling_edge", "edge_id": e["id"], "field": "target"})
    return issues

def auto_fix(ir: dict, issues: list[dict]) -> dict:
    """Remove dangling edges and other fixable issues."""
    fixed = {e["id"] for e in issues if e.get("type") == "dangling_edge"}
    ir["graph"]["edges"] = [e for e in ir["graph"].get("edges", []) if e["id"] not in fixed]
    return ir


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8765)
