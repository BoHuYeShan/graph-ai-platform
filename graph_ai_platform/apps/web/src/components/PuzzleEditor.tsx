import { useEffect, useRef } from 'react'
import { NodeEditor, ClassicPreset } from 'rete'
import type { GetSchemes } from 'rete'
import { AreaPlugin, AreaExtensions } from 'rete-area-plugin'
import type { ReactArea2D } from 'rete-react-plugin'
import { ConnectionPlugin, Presets as ConnectionPresets } from 'rete-connection-plugin'
import { ReactPlugin, Presets } from 'rete-react-plugin'
import { createRoot } from 'react-dom/client'
import type { IRGraph } from '../types/ir'

interface PuzzleEditorProps {
  ir: IRGraph
}

type Schemes = GetSchemes<
  ClassicPreset.Node,
  ClassicPreset.Connection<ClassicPreset.Node, ClassicPreset.Node>
>
type AreaExtra = ReactArea2D<Schemes>

const anySocket = new ClassicPreset.Socket('any')
const boolSocket = new ClassicPreset.Socket('boolean')

function buildEditor(editor: NodeEditor<Schemes>, _area: AreaPlugin<Schemes, AreaExtra>, ir: IRGraph) {
  const nodeMap = new Map<string, ClassicPreset.Node>()

  // Clear existing nodes
  for (const n of editor.getNodes()) {
    for (const conn of editor.getConnections()) {
      if (conn.source === n.id || conn.target === n.id) {
        editor.removeConnection(conn.id).catch(() => {})
      }
    }
    editor.removeNode(n.id).catch(() => {})
  }

  // Add new nodes
  for (const irn of ir.graph.nodes) {
    const n = new ClassicPreset.Node(irn.label)

    switch (irn.type) {
      case 'literal':
      case 'name':
        n.addOutput('out', new ClassicPreset.Output(anySocket))
        n.addControl('val', new ClassicPreset.InputControl('text', {
          initial: irn.type === 'literal' ? String(irn.value ?? '∅') : `@${irn.label}`,
          readonly: true,
        }))
        break
      case 'binop':
      case 'compare':
        n.addInput('left', new ClassicPreset.Input(anySocket))
        n.addInput('right', new ClassicPreset.Input(anySocket))
        n.addOutput('out', new ClassicPreset.Output(anySocket))
        n.addControl('op', new ClassicPreset.InputControl('text', { initial: irn.label, readonly: true }))
        break
      case 'assign':
      case 'augassign':
        n.addInput('value', new ClassicPreset.Input(anySocket))
        n.addControl('lbl', new ClassicPreset.InputControl('text', { initial: `${irn.label} =`, readonly: true }))
        break
      case 'return':
        n.addInput('value', new ClassicPreset.Input(anySocket))
        break
      case 'call':
        n.addControl('fn', new ClassicPreset.InputControl('text', { initial: `📞 ${irn.label}()`, readonly: true }))
        n.addOutput('result', new ClassicPreset.Output(anySocket))
        break
      case 'if':
        n.addInput('test', new ClassicPreset.Input(boolSocket))
        break
      case 'for':
        n.addInput('iter', new ClassicPreset.Input(anySocket))
        break
      case 'while':
        n.addInput('test', new ClassicPreset.Input(boolSocket))
        break
      case 'function_def':
        n.addControl('def', new ClassicPreset.InputControl('text', { initial: `🔵 def ${irn.label}()`, readonly: true }))
        n.addOutput('out', new ClassicPreset.Output(anySocket))
        break
      case 'class_def':
        n.addControl('def', new ClassicPreset.InputControl('text', { initial: `📦 class ${irn.label}`, readonly: true }))
        n.addOutput('out', new ClassicPreset.Output(anySocket))
        break
      case 'import':
      case 'import_from':
        n.addControl('mod', new ClassicPreset.InputControl('text', { initial: `📥 import ${irn.label}`, readonly: true }))
        n.addOutput('module', new ClassicPreset.Output(anySocket))
        break
      default:
        n.addOutput('out', new ClassicPreset.Output(anySocket))
    }

    editor.addNode(n).then(() => {
      nodeMap.set(irn.id, n)
      // Try to connect this node after adding
      for (const ire of ir.graph.edges) {
        if (ire.target === irn.id) {
          const src = nodeMap.get(ire.source)
          if (!src) continue
          const sk = Object.keys(src.outputs)[0]
          const tk = Object.keys(n.inputs)[0]
          if (sk && tk) {
            editor.addConnection(new ClassicPreset.Connection(src, sk, n, tk)).catch(() => {})
          }
        }
      }
    }).catch(() => {})
  }
}

export function PuzzleEditor({ ir }: PuzzleEditorProps) {
  const containerRef = useRef<HTMLDivElement>(null)
  const editorRef = useRef<NodeEditor<Schemes> | null>(null)
  const areaRef = useRef<AreaPlugin<Schemes, AreaExtra> | null>(null)

  useEffect(() => {
    const container = containerRef.current
    if (!container || editorRef.current) return

    const editor = new NodeEditor<Schemes>()
    const area = new AreaPlugin<Schemes, AreaExtra>(container)
    const connection = new ConnectionPlugin<Schemes, AreaExtra>()
    const render = new ReactPlugin<Schemes, AreaExtra>({ createRoot })

    render.addPreset(Presets.classic.setup())
    connection.addPreset(ConnectionPresets.classic.setup())

    editor.use(area)
    area.use(connection)
    area.use(render)
    AreaExtensions.selectableNodes(area, AreaExtensions.selector(), { accumulating: AreaExtensions.accumulateOnCtrl() })
    AreaExtensions.simpleNodesOrder(area)

    editorRef.current = editor
    areaRef.current = area
  }, [])

  useEffect(() => {
    if (!editorRef.current || !areaRef.current) return
    buildEditor(editorRef.current, areaRef.current, ir)
  }, [ir])

  return (
    <div
      ref={containerRef}
      style={{ width: '100%', height: '100%', background: '#1a1a2e' }}
    />
  )
}
