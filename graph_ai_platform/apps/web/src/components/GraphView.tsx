import { useMemo, useEffect, useRef } from 'react'
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
import dagre from 'dagre'
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

const catColor: Record<string, string> = {
  control: '#f59e0b', structure: '#3b82f6', action: '#10b981',
  data: '#8b5cf6', escape: '#ef4444',
}

// ── Which node types are containers (have body children) ──
const CONTAINER_TYPES = new Set(['function_def', 'class_def', 'if', 'for', 'while', 'module'])

// ── Build a flat list of flow nodes with dagre-computed positions ──
function layoutGraph(ir: IRGraph): { nodes: Node[]; edges: Edge[] } {
  const rawNodes = ir.graph.nodes
  const rawEdges = ir.graph.edges
  const nodeMap = new Map(rawNodes.map(n => [n.id, n]))

  // Separate containers vs leaf nodes
  const containerIds = new Set<string>()
  for (const n of rawNodes) {
    if (CONTAINER_TYPES.has(n.type) && (n.children || []).length > 0) {
      containerIds.add(n.id)
    }
  }

  // Assign each node a parent container (the innermost container it belongs to)
  const childToParent = new Map<string, string>()
  function assignParent(nodeId: string, parentId: string | null) {
    if (parentId) childToParent.set(nodeId, parentId)
    const n = nodeMap.get(nodeId)
    if (!n) return
    if (containerIds.has(nodeId)) {
      // This node IS a container — its children are inside it
      for (const cid of (n.children || [])) {
        assignParent(cid, nodeId)
      }
    } else {
      // leaf
    }
  }
  // Start from top-level nodes (those not in any children list)
  const allChildren = new Set<string>()
  for (const n of rawNodes) {
    for (const cid of (n.children || [])) allChildren.add(cid)
  }
  for (const n of rawNodes) {
    if (!allChildren.has(n.id)) assignParent(n.id, null)
  }

  // ── dagre layout ──
  const g = new dagre.graphlib.Graph()
  g.setDefaultEdgeLabel(() => ({}))
  g.setGraph({ rankdir: 'TB', nodesep: 40, ranksep: 60, marginx: 30, marginy: 30 })

  // Build dagre sub-graphs per container + top-level
  type LayoutGroup = { nodes: string[] }
  const groups = new Map<string, LayoutGroup>()
  groups.set('__root__', { nodes: [] })

  for (const n of rawNodes) {
    const p = childToParent.get(n.id) || '__root__'
    if (!groups.has(p)) groups.set(p, { nodes: [] })
    groups.get(p)!.nodes.push(n.id)
  }

  // Layout each group with dagre
  const positions = new Map<string, { x: number; y: number }>()

  for (const [, group] of groups) {
    if (group.nodes.length === 0) continue
    const sg = new dagre.graphlib.Graph()
    sg.setGraph({ rankdir: 'TB', nodesep: 30, ranksep: 40, marginx: 20, marginy: 20 })
    sg.setDefaultEdgeLabel(() => ({}))

    for (const nid of group.nodes) {
      const n = nodeMap.get(nid)!
      sg.setNode(nid, { width: 120, height: 40, label: n.label })
    }

    for (const e of rawEdges) {
      if (group.nodes.includes(e.source) && group.nodes.includes(e.target)) {
        sg.setEdge(e.source, e.target)
      }
    }

    dagre.layout(sg)

    sg.nodes().forEach(nid => {
      const pos = sg.node(nid)
      positions.set(nid, { x: pos.x - 60, y: pos.y - 20 })
    })
  }

  // Convert positions to absolute (relative to parent)
  function toAbsolute(nodeId: string): { x: number; y: number } {
    const pos = positions.get(nodeId) || { x: 0, y: 0 }
    const parentId = childToParent.get(nodeId)
    if (parentId) {
      const pp = toAbsolute(parentId)
      return { x: pp.x + pos.x + 60, y: pp.y + pos.y + 40 }
    }
    return pos
  }

  // Create React Flow nodes (with parentId for containers)
  const flowNodes: Node[] = []
  const processed = new Set<string>()

  for (const n of rawNodes) {
    if (processed.has(n.id)) continue
    processed.add(n.id)

    const absPos = toAbsolute(n.id)
    const parentId = childToParent.get(n.id) || undefined

    if (containerIds.has(n.id)) {
      // Container node: size based on children bounding box
      const children = (n.children || []).filter(c => nodeMap.has(c))
      let minX = absPos.x, minY = absPos.y, maxX = absPos.x + 160, maxY = absPos.y + 50
      for (const cid of children) {
        const cp = toAbsolute(cid)
        if (cp.x < minX) minX = cp.x
        if (cp.y < minY) minY = cp.y
        if (cp.x + 120 > maxX) maxX = cp.x + 120
        if (cp.y + 40 > maxY) maxY = cp.y + 40
      }
      const pad = 30
      flowNodes.push({
        id: n.id,
        type: n.category,
        position: { x: minX - pad, y: minY - pad },
        data: {
          label: `${n.type}: ${n.label}`,
          category: n.category,
          nodeType: n.type,
          color: catColor[n.category] || '#666',
          isContainer: true,
        },
        style: {
          width: maxX - minX + pad * 2,
          height: maxY - minY + pad * 2,
          borderColor: catColor[n.category] || '#666',
          borderRadius: 8,
          background: '#ffffff08',
        },
        parentId: parentId === '__root__' ? undefined : parentId,
      })

      // Children inside this container
      for (const cid of children) {
        const cp = toAbsolute(cid)
        flowNodes.push({
          id: cid,
          type: nodeMap.get(cid)?.category || 'data',
          position: { x: cp.x - minX + pad, y: cp.y - minY + pad },
          data: {
            label: nodeMap.get(cid)?.label || '',
            category: nodeMap.get(cid)?.category || 'data',
            nodeType: nodeMap.get(cid)?.type || '',
            color: catColor[nodeMap.get(cid)?.category || ''] || '#888',
          },
          parentId: n.id,
          style: { borderColor: catColor[nodeMap.get(cid)?.category || ''] || '#888' },
        })
        processed.add(cid)
      }
    } else if (!childToParent.has(n.id)) {
      // Top-level leaf node
      flowNodes.push({
        id: n.id,
        type: n.category,
        position: absPos,
        data: {
          label: n.label,
          category: n.category,
          nodeType: n.type,
          color: catColor[n.category] || '#666',
        },
        style: { borderColor: catColor[n.category] || '#666' },
      })
    }
    // Leaf nodes inside containers are handled in the container branch above
  }

  // Create edges
  const flowEdges: Edge[] = rawEdges.map((e) => ({
    id: e.id,
    source: e.source,
    target: e.target,
    label: e.label || '',
    animated: true,
    style: { stroke: '#555', strokeWidth: 1.5 },
  }))

  return { nodes: flowNodes, edges: flowEdges }
}


export function GraphView({ ir }: GraphViewProps) {
  const { nodes: flowNodes, edges: flowEdges } = useMemo(() => layoutGraph(ir), [ir])
  const [nodes, setNodes, onNodesChange] = useNodesState(flowNodes)
  const [edges, setEdges, onEdgesChange] = useEdgesState(flowEdges)
  const rfRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    setNodes(flowNodes)
    setEdges(flowEdges)
  }, [flowNodes, flowEdges, setNodes, setEdges])

  return (
    <div ref={rfRef} style={{ width: '100%', height: '100%' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        fitView
        attributionPosition="bottom-left"
        minZoom={0.2}
        maxZoom={3}
      >
        <Background color="#333" gap={20} size={1} />
        <Controls />
        <MiniMap nodeColor={(n) => (n.data as any)?.color || '#666'} style={{ background: '#1a1a1a' }} />
      </ReactFlow>
    </div>
  )
}
