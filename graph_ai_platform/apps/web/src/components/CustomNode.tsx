import { memo } from 'react'
import { Handle, Position, type NodeProps } from '@xyflow/react'

function CustomNodeComponent({ data, selected }: NodeProps) {
  const d = data as { label: string; category: string; nodeType: string; color: string }
  return (
    <div
      className={`custom-node custom-node-${d.category}`}
      style={{
        border: `2px solid ${d.color}`,
        background: selected ? 'rgba(255,255,255,0.12)' : 'rgba(255,255,255,0.06)',
        borderRadius: 6,
        padding: '8px 14px',
        color: '#e0e0e0',
        fontFamily: 'monospace',
        fontSize: 12,
        minWidth: 80,
        textAlign: 'center',
      }}
    >
      <Handle type="target" position={Position.Left} style={{ background: d.color }} />
      <div style={{ fontWeight: 600, marginBottom: 2 }}>{d.label}</div>
      <div style={{ fontSize: 10, opacity: 0.6 }}>{d.nodeType}</div>
      <Handle type="source" position={Position.Right} style={{ background: d.color }} />
    </div>
  )
}

export const CustomNode = memo(CustomNodeComponent)
