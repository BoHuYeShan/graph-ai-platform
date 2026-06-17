#!/usr/bin/env python3
"""API integration test — full backend pipeline."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(os.path.join(os.path.dirname(__file__), "..", ".."))

from fastapi.testclient import TestClient
from services.core.server import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
    print("  PASS health")

def test_parse():
    r = client.post("/parse", json={"source": "x = 42\ny = x + 1", "filename": "test.py"})
    assert r.status_code == 200, f"Parse failed: {r.status_code}"
    ir = r.json()["ir"]
    nodes = ir["graph"]["nodes"]
    assert len(nodes) == 6, f"Expected 6 nodes, got {len(nodes)}"
    print(f"  PASS parse ({len(nodes)} nodes)")

def test_codegen():
    r = client.post("/parse", json={"source": "x = 42\ny = x + 1", "filename": "test.py"})
    ir = r.json()["ir"]
    r = client.post("/codegen", json={"ir": ir})
    assert r.status_code == 200
    code = r.json()["code"]
    assert "x" in code and "42" in code
    print(f"  PASS codegen ({len(code.split(chr(10)))} lines)")

def test_execute():
    r = client.post("/parse", json={"source": "x = 42\ny = x + 1", "filename": "test.py"})
    ir = r.json()["ir"]
    r = client.post("/execute", json={"ir": ir})
    assert r.status_code == 200
    vars = r.json()["variables"]
    assert vars.get("x") == 42, f"Expected x=42, got {vars.get('x')}"
    assert vars.get("y") == 43, f"Expected y=43, got {vars.get('y')}"
    print(f"  PASS execute (x={vars.get('x')}, y={vars.get('y')})")

def test_normalize():
    r = client.post("/parse", json={"source": "x = 42", "filename": "test.py"})
    ir = r.json()["ir"]
    r = client.post("/normalize", json={"ir": ir})
    assert r.status_code == 200
    print("  PASS normalize")

if __name__ == "__main__":
    print("=== API Integration Tests ===\n")
    for t in [test_health, test_parse, test_codegen, test_execute, test_normalize]:
        try:
            t()
        except Exception as e:
            print(f"  FAIL {t.__name__}: {e}")
            import traceback
            traceback.print_exc()
    print("\nDONE")
