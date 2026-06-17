#!/usr/bin/env python3
"""Minimal runtime smoke test to diagnose timeout."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
os.chdir(os.path.join(os.path.dirname(__file__), ".."))

from packages.parser import parse_source
from services.runtime import execute_ir

print("=== 1. simple assign ===")
code = "x = 42\ny = x + 1"
ir = parse_source(code)
import json
print(f"IR: {len(ir['graph']['nodes'])} nodes, {len(ir['graph']['edges'])} edges")
result = execute_ir(ir)
print(f"  x={result.get('x')}, y={result.get('y')}")

print("\n=== 2. for loop ===")
code = "total = 0\nfor i in [1, 2, 3]:\n    total = total + i"
ir = parse_source(code)
print(f"IR: {len(ir['graph']['nodes'])} nodes, {len(ir['graph']['edges'])} edges")
# Print node types
for n in ir['graph']['nodes']:
    print(f"  {n['type']:15s} {n['label']:20s} children={n.get('children',[])}")
result = execute_ir(ir)
print(f"  total={result.get('total')}")

print("\n=== 3. while loop ===")
code = "n = 3\nr = 1\nwhile n > 0:\n    r = r * n\n    n = n - 1"
ir = parse_source(code)
print(f"IR: {len(ir['graph']['nodes'])} nodes, {len(ir['graph']['edges'])} edges")
result = execute_ir(ir)
print(f"  n={result.get('n')}, r={result.get('r')}")

print("\nDONE")
