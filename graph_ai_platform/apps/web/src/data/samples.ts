import type { IRGraph } from '../types/ir'

export const sampleCode = `def greet(name):
    return "Hello, " + name

def factorial(n):
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    result = 1
    i = 2
    while i <= n:
        result = result * i
        i = i + 1
    return result

msg = greet("World")
fact = factorial(5)
print(msg, fact)
`

export const sampleIR: IRGraph = {
  graph: {
    nodes: [
      { id: 'n1', category: 'structure', type: 'function_def', label: 'greet',
        inputs: [{ name: 'arg_name' }], outputs: [{ name: 'result' }], children: ['n2', 'n3'] },
      { id: 'n2', category: 'control', type: 'return', label: 'return',
        inputs: [{ name: 'value' }], outputs: [], children: [] },
      { id: 'n3', category: 'structure', type: 'function_def', label: 'factorial',
        inputs: [{ name: 'arg_n' }], outputs: [{ name: 'result' }], children: ['n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10'] },
      { id: 'n4', category: 'control', type: 'if', label: 'if', inputs: [{ name: 'test' }], outputs: [], children: ['n5'] },
      { id: 'n5', category: 'control', type: 'return', label: 'return', inputs: [{ name: 'value' }], outputs: [], children: [] },
      { id: 'n6', category: 'control', type: 'if', label: 'if', inputs: [{ name: 'test' }], outputs: [], children: ['n7'] },
      { id: 'n7', category: 'control', type: 'return', label: 'return', inputs: [{ name: 'value' }], outputs: [], children: [] },
      { id: 'n8', category: 'action', type: 'assign', label: 'result', inputs: [{ name: 'value' }], outputs: [], children: [] },
      { id: 'n9', category: 'action', type: 'assign', label: 'i', inputs: [{ name: 'value' }], outputs: [], children: [] },
      { id: 'n10', category: 'control', type: 'while', label: 'while', inputs: [], outputs: [], children: ['n11', 'n12'] },
      { id: 'n11', category: 'action', type: 'assign', label: 'result', inputs: [{ name: 'value' }], outputs: [], children: [] },
      { id: 'n12', category: 'action', type: 'assign', label: 'i', inputs: [{ name: 'value' }], outputs: [], children: [] },
      { id: 'n13', category: 'action', type: 'assign', label: 'msg', inputs: [{ name: 'value' }], outputs: [], children: [] },
      { id: 'n14', category: 'action', type: 'assign', label: 'fact', inputs: [{ name: 'value' }], outputs: [], children: [] },
      { id: 'n15', category: 'action', type: 'call', label: 'print',
        inputs: [{ name: 'arg_0' }, { name: 'arg_1' }], outputs: [{ name: 'result' }], children: [] },
    ],
    edges: [
      { id: 'e1', source: 'n1', target: 'n13', sourcePort: 'result', targetPort: 'value' },
      { id: 'e2', source: 'n3', target: 'n14', sourcePort: 'result', targetPort: 'value' },
    ],
    variables: {},
    scopes: [
      { id: 's_global', nodes: ['n1', 'n3', 'n13', 'n14', 'n15'] },
      { id: 's_greet', parent: 's_global', nodes: ['n2'] },
      { id: 's_factorial', parent: 's_global', nodes: ['n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12'] },
    ],
  },
  view: {
    nodePositions: {
      n1: { x: 50, y: 50 }, n2: { x: 200, y: 80 },
      n3: { x: 50, y: 200 }, n4: { x: 200, y: 220 }, n5: { x: 350, y: 240 },
      n6: { x: 200, y: 300 }, n7: { x: 350, y: 320 },
      n8: { x: 200, y: 380 }, n9: { x: 200, y: 420 },
      n10: { x: 200, y: 480 }, n11: { x: 350, y: 500 }, n12: { x: 350, y: 540 },
      n13: { x: 50, y: 600 }, n14: { x: 50, y: 650 }, n15: { x: 50, y: 700 },
    },
    theme: 'default',
  },
  metadata: { irVersion: '0.1.0', pythonSubset: 'mvp-0.1' },
}
