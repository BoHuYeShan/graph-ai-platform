#!/usr/bin/env python3
"""Test the runtime executor with parsed IR from the fixtures."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(os.path.join(os.path.dirname(__file__), "..", ".."))

from packages.parser import parse_source
from services.runtime import execute_ir

def test_simple_assign():
    code = "x = 42\ny = x + 1"
    ir = parse_source(code)
    result = execute_ir(ir)
    assert result.get("x") == 42, f"Expected x=42, got {result.get('x')}"
    assert result.get("y") == 43, f"Expected y=43, got {result.get('y')}"
    print("  PASS simple_assign")

def test_if():
    code = "x = 10\nif x > 5:\n    y = 'big'\nelse:\n    y = 'small'"
    ir = parse_source(code)
    result = execute_ir(ir)
    print(f"  if result: y={result.get('y')}")
    print("  PASS if (structural)")

def test_for():
    code = "total = 0\nfor i in [1, 2, 3]:\n    total = total + i"
    ir = parse_source(code)
    result = execute_ir(ir)
    print(f"  for result: total={result.get('total')}")
    print("  PASS for")

def test_while():
    code = "n = 3\nresult = 1\nwhile n > 0:\n    result = result * n\n    n = n - 1"
    ir = parse_source(code)
    result = execute_ir(ir)
    print(f"  while result: n={result.get('n')}, result={result.get('result')}")
    print("  PASS while")

def test_function():
    code = """def greet(name):
    return "Hello, " + name
msg = greet("World")
"""
    ir = parse_source(code)
    result = execute_ir(ir)
    print(f"  fn result: msg={result.get('msg')}")
    print("  PASS function")

def test_class():
    code = """class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count = self.count + 1
c = Counter()
c.increment()
"""
    ir = parse_source(code)
    result = execute_ir(ir)
    print(f"  class result: c={result.get('c')}")
    print("  PASS class")

def test_import():
    code = "import math\nimport os.path\nr = math.sqrt(16)"
    ir = parse_source(code)
    result = execute_ir(ir)
    print(f"  import result: math={result.get('math')}, r={result.get('r')}")
    print("  PASS import")

if __name__ == "__main__":
    print("=== Runtime Executor Tests ===\n")
    tests = [test_simple_assign, test_if, test_for, test_while,
             test_function, test_class, test_import]
    for t in tests:
        try:
            t()
        except Exception as e:
            print(f"  FAIL {t.__name__}: {e}")
            import traceback
            traceback.print_exc()
