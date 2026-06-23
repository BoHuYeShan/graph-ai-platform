"""Verify visit_Call label is the function name, not hardcoded 'call'."""
import sys
sys.path.insert(0, '.')
from packages.parser import parse_source

ir = parse_source('print(123)')
for n in ir['graph']['nodes']:
    info = f'  {n["id"]} type={n["type"]:12s} label={n["label"]}'
    print(info)
print(f'Total: {len(ir["graph"]["nodes"])} nodes')

# Check that call node has label "print", not "call"
call_nodes = [n for n in ir['graph']['nodes'] if n['type'] == 'call']
assert len(call_nodes) == 1, f'Expected 1 call node, got {len(call_nodes)}'
assert call_nodes[0]['label'] == 'print', f"Expected 'print', got '{call_nodes[0]['label']}'"
print('\nPASS: call label correctly shows function name')
