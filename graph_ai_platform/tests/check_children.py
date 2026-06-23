"""Check if backend IR JSON omits children when empty."""
import sys, json
sys.path.insert(0, '.')
from packages.parser import parse_source
ir = parse_source('x = 42\ny = x + 1')
for n in ir['graph']['nodes']:
    has = 'children' in n
    print(f'{n["id"]:20s} type={n["type"]:12s} children={n.get("children", "MISSING!")}')
