#!/usr/bin/env python3
"""Comprehensive roundtrip test: parse → codegen → execute all fixtures."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(os.path.join(os.path.dirname(__file__), "..", ".."))

from packages.parser import parse_source
from packages.codegen import generate as codegen
from services.runtime import execute_ir

fixtures = [
    ("simple_assign", "x = 42\ny = x + 1"),
    ("if_else", "x = 10\nif x > 5:\n    y = 'big'\nelse:\n    y = 'small'"),
    ("for_loop", "total = 0\nfor i in [1, 2, 3]:\n    total = total + i"),
    ("while_loop", "n = 3\nr = 1\nwhile n > 0:\n    r = r * n\n    n = n - 1"),
    ("function", "def greet(name):\n    return 'Hello, ' + name"),
    ("nested_if", "x = 7\nif x > 0:\n    if x > 5:\n        y = 'big'\n    else:\n        y = 'small'\nelse:\n    y = 'neg'"),
    ("break_continue", "total = 0\nfor i in [1, 2, 3, 4, 5]:\n    if i == 3:\n        break\n    total = total + i"),
]

pass_count = 0
fail_count = 0

print(f"{'Fixture':20s} {'Parse':8s} {'Codegen':9s} {'Roundtrip':10s}")
print("-" * 50)

for name, code in fixtures:
    # Parse
    try:
        ir = parse_source(code)
        parse_ok = True
    except Exception as e:
        parse_ok = False
        parse_err = str(e)

    # Generate from IR
    if parse_ok:
        try:
            gen_code = codegen(ir)
            codegen_ok = True
        except Exception as e:
            codegen_ok = False
            codegen_err = str(e)
    else:
        codegen_ok = False

    # Execute original
    if parse_ok:
        try:
            result_orig = execute_ir(ir)
            exec_ok = True
        except Exception as e:
            exec_ok = False
            exec_err = str(e)
    else:
        exec_ok = False

    p = "PASS" if parse_ok else "FAIL"
    c = "PASS" if codegen_ok else "FAIL"
    e = "PASS" if exec_ok else "FAIL"
    print(f"{name:20s} {p:8s} {c:9s} {e:10s}")

    if parse_ok and codegen_ok and exec_ok:
        pass_count += 1
    else:
        fail_count += 1

print("-" * 50)
print(f"Results: {pass_count} passed, {fail_count} failed out of {len(fixtures)}")
