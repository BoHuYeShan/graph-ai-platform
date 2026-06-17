#!/usr/bin/env python3
"""Quick smoke test: parse → generate → compare."""
import sys, json
sys.path.insert(0, "graph_ai_platform")
from packages.parser import parse_source
from packages.codegen import generate

source = open("graph_ai_platform/tests/fixtures/python_subset/01_basics.py").read()
ir = parse_source(source, "01_basics.py")

# Check children
for n in ir["graph"]["nodes"]:
    if n["type"] in ("if","for","while","function_def","class_def","assign"):
        ch = n.get("children",[])
        print(f'  {n["type"]:15s} {n["label"]:20s} children={ch}')

print(f"\nTotal nodes: {len(ir['graph']['nodes'])}")
print(f"Total edges: {len(ir['graph']['edges'])}")

# Generate code
code = generate(ir)
print(f"\n=== Generated Code ===\n{code}")
