import { useMemo } from 'react'
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState,
} from '@xyflow/react'
import type { Node, Edge } from '@xyflow/react'
import '@xyflow/react/dist/style.css'
import type { IRGraph } from '../types/ir'
import { CustomNode } from './CustomNode'

interface GraphViewProps {
  ir: IRGraph
}

const nodeTypes = {
  control: CustomNode,
  structure: CustomNode,
  action: CustomNode,
  data: CustomNode,
  escape: CustomNode,
}

const categoryColors: Record<string, string> = {
  control: '#f59e0b',
  structure: '#3b82f6',
  action: '#10b981',
  data: '#8b5cf6',
  escape: '#ef4444',
}

function irToFlowNodes(ir: IRGraph): Node[] {
  const positions = ir.view?.nodePositions || {}
  return ir.graph.nodes.map((n) => ({
    id: n.id,
    type: n.category,
    position: positions[n.id] || { x: Math.random() * 400, y: Math.random() * 400 },
    data: {
      label: n.label,
      category: n.category,
      nodeType: n.type,
      color: categoryColors[n.category] || '#666',
      children: n.children,
    },
    style: { borderColor: categoryColors[n.category] || '#666' },
  }))
}

function irToFlowEdges(ir: IRGraph): Edge[] {
  return ir.graph.edges.map((e) => ({
    id: e.id,
    source: e.source,
    target: e.target,
    sourceHandle: e.sourcePort || 'out',
    targetHandle: e.targetPort || 'in',
    label: e.label || '',
    animated: true,
    style: { stroke: '#555' },
  }))
}

export function GraphView({ ir }: GraphViewProps) {
  const initialNodes = useMemo(() => irToFlowNodes(ir), [ir])
  const initialEdges = useMemo(() => irToFlowEdges(ir), [ir])
  const [_nodes, _edges, onNodesChange] = useNodesState(initialNodes)
  const [, , onEdgesChange] = useEdgesState(initialEdges)

  return (
    <div style={{ width: '100%', height: '100%' }}>
      <ReactFlow
        nodes={initialNodes}
        edges={initialEdges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        fitView
        attributionPosition="bottom-left"
      >
        <Background color="#333" gap={20} />
        <Controls />
        <MiniMap
          nodeColor={(n) => (n.data as any)?.color || '#666'}
          style={{ background: '#1a1a1a' }}
        />
      </ReactFlow>
    </div>
  )
}
