/* ── IR type definitions ── */

export interface PortDef {
  name: string
  type?: string
  optional?: boolean
}

export interface IRNode {
  id: string
  category: 'control' | 'structure' | 'action' | 'data' | 'escape'
  type: string
  label: string
  value?: unknown
  inputs: PortDef[]
  outputs: PortDef[]
  children: string[]
  codeBlock?: string
}

export interface IREdge {
  id: string
  source: string
  target: string
  sourcePort?: string
  targetPort?: string
  label?: string
}

export interface IRGraph {
  graph: {
    nodes: IRNode[]
    edges: IREdge[]
    variables?: Record<string, string>
    scopes?: Array<{ id: string; parent?: string; nodes: string[] }>
  }
  view?: { nodePositions: Record<string, { x: number; y: number }>; theme?: string }
  sourceMap?: Record<string, unknown>
  metadata?: { irVersion: string; pythonSubset: string }
}
