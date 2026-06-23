import { useEffect, useRef } from 'react'
import * as Blockly from 'blockly'
import 'blockly/blocks'
import { pythonGenerator } from 'blockly/python'
import type { IRGraph } from '../types/ir'

interface BlocklyEditorProps {
  ir: IRGraph
  onCodeChange?: (code: string) => void
}

// ── Blockly Dark Theme ──
const darkTheme = Blockly.Theme.defineTheme('dark', {
  base: Blockly.Themes.Classic,
  name: 'dark',
  componentStyles: {
    workspaceBackgroundColour: '#1a1a2e',
    toolboxBackgroundColour: '#0d0d1a',
    toolboxForegroundColour: '#ccc',
    flyoutBackgroundColour: '#1a1a2e',
    flyoutForegroundColour: '#ccc',
    flyoutOpacity: 0.9,
    scrollbarColour: '#333',
    insertionMarkerColour: '#6366f1',
  },
  blockStyles: {
    logic_blocks: { colourPrimary: '#5B80A5', colourSecondary: '#4A6F94', colourTertiary: '#6B90B5' },
    math_blocks: { colourPrimary: '#5B67A5', colourSecondary: '#4A5694', colourTertiary: '#6B77B5' },
    loop_blocks: { colourPrimary: '#5BA55B', colourSecondary: '#4A944A', colourTertiary: '#6BB56B' },
    procedure_blocks: { colourPrimary: '#9A5BA5', colourSecondary: '#894A94', colourTertiary: '#AA6BB5' },
    variable_blocks: { colourPrimary: '#5BA58B', colourSecondary: '#4A947A', colourTertiary: '#6BB59B' },
  },
  categoryStyles: {
    logic_category: { colour: '#5B80A5' },
    math_category: { colour: '#5B67A5' },
    loop_category: { colour: '#5BA55B' },
    procedure_category: { colour: '#9A5BA5' },
    variable_category: { colour: '#5BA58B' },
  },
})

// ── Custom Python blocks ──
Blockly.Blocks['py_import'] = {
  init: function () {
    this.appendDummyInput().appendField('import').appendField(new Blockly.FieldTextInput('os'), 'MODULE')
    this.setPreviousStatement(true, null)
    this.setNextStatement(true, null)
    this.setColour(120, '#3A7A3A', '#2A5A2A')
  },
}
Blockly.Blocks['py_function_def'] = {
  init: function () {
    this.appendDummyInput().appendField('def').appendField(new Blockly.FieldTextInput('func'), 'NAME').appendField('(').appendField(new Blockly.FieldTextInput('args'), 'ARGS').appendField(')').appendField(':')
    this.appendStatementInput('BODY').setCheck(null)
    this.setPreviousStatement(true, null)
    this.setNextStatement(true, null)
    this.setColour(290, '#7A3A8A', '#5A2A6A')
  },
}
Blockly.Blocks['py_return'] = {
  init: function () {
    this.appendValueInput('VALUE').setCheck(null).appendField('return')
    this.setPreviousStatement(true, null)
    this.setNextStatement(true, null)
    this.setColour(60, '#8A8A3A', '#6A6A2A')
  },
}
Blockly.Blocks['py_while'] = {
  init: function () {
    this.appendValueInput('TEST').setCheck(null).appendField('while')
    this.appendStatementInput('BODY').setCheck(null)
    this.setPreviousStatement(true, null)
    this.setNextStatement(true, null)
    this.setColour(120, '#3A7A3A', '#2A5A2A')
  },
}
Blockly.Blocks['py_assign'] = {
  init: function () {
    this.appendDummyInput().appendField(new Blockly.FieldTextInput('x'), 'VAR').appendField('=')
    this.appendValueInput('VALUE').setCheck(null)
    this.setPreviousStatement(true, null)
    this.setNextStatement(true, null)
    this.setColour(210, '#3A5A8A', '#2A4A6A')
  },
}

// ── Custom generators ──
pythonGenerator.forBlock['py_import'] = (block) => [`import ${block.getFieldValue('MODULE')}\n`, 0]
pythonGenerator.forBlock['py_function_def'] = (block) => {
  const name = block.getFieldValue('NAME')
  const args = block.getFieldValue('ARGS')
  const body = pythonGenerator.statementToCode(block, 'BODY')
  return [`def ${name}(${args}):\n${body}`, 0 as any]
}
pythonGenerator.forBlock['py_return'] = (block) => {
  const val = pythonGenerator.valueToCode(block, 'VALUE', 99) || ''
  return [`return ${val}\n`, 0]
}
pythonGenerator.forBlock['py_while'] = (block) => {
  const test = pythonGenerator.valueToCode(block, 'TEST', 99) || 'True'
  const body = pythonGenerator.statementToCode(block, 'BODY')
  return [`while ${test}:\n${body}`, 0 as any]
}
pythonGenerator.forBlock['py_assign'] = (block) => {
  const varName = block.getFieldValue('VAR')
  const val = pythonGenerator.valueToCode(block, 'VALUE', 99) || '?'
  return [`${varName} = ${val}\n`, 0]
}

// ── IR tree → Blockly XML (with proper <next> chaining) ──
function buildXML(ir: IRGraph): string {
  const nodeMap = new Map(ir.graph.nodes.map(n => [n.id, n]))
  const allChildren = new Set<string>()
  for (const n of ir.graph.nodes) for (const c of n.children || []) allChildren.add(c)

  // Helper: find value node from edge
  function valueNode(nodeId: string, port: string) {
    const e = ir.graph.edges.find(e => e.target === nodeId && e.targetPort === port)
    return e ? nodeMap.get(e.source) : null
  }

  // Expression → Block XML
  function emitExpr(node: typeof ir.graph.nodes[0]): string {
    switch (node.type) {
      case 'literal':
        return `<block type="math_number" id="${node.id}"><field name="NUM">${node.value ?? 0}</field></block>`
      case 'name':
        return `<block type="variables_get" id="${node.id}"><field name="VAR">${node.label}</field></block>`
      case 'binop': {
        const opMap: Record<string, string> = { Add: 'ADD', Sub: 'MINUS', Mult: 'MULTIPLY', Div: 'DIVIDE' }
        const left = valueNode(node.id, 'left')
        const right = valueNode(node.id, 'right')
        const lx = left ? emitExpr(left) : '<shadow type="math_number"><field name="NUM">0</field></shadow>'
        const rx = right ? emitExpr(right) : '<shadow type="math_number"><field name="NUM">0</field></shadow>'
        return `<block type="math_arithmetic" id="${node.id}"><field name="OP">${opMap[node.label] || 'ADD'}</field><value name="A">${lx}</value><value name="B">${rx}</value></block>`
      }
      case 'call':
        return `<block type="procedures_callnoreturn" id="${node.id}"><mutation name="${node.label}"/></block>`
      case 'compare':
        return `<block type="logic_compare" id="${node.id}"><field name="OP">GT</field></block>`
      default:
        return `<block type="math_number" id="${node.id}"><field name="NUM">0</field></block>`
    }
  }

  // Statement → Block XML, with optional next chain
  function emitStmt(node: typeof ir.graph.nodes[0]): string {
    switch (node.type) {
      case 'assign': {
        const val = valueNode(node.id, 'value')
        const vx = val ? emitExpr(val) : '<shadow type="math_number"><field name="NUM">0</field></shadow>'
        return `<block type="py_assign" id="${node.id}"><field name="VAR">${node.label}</field><value name="VALUE">${vx}</value></block>`
      }
      case 'return': {
        const val = valueNode(node.id, 'value')
        const vx = val ? emitExpr(val) : ''
        return `<block type="py_return" id="${node.id}"><value name="VALUE">${vx}</value></block>`
      }
      case 'if': {
        const bodyBlocks = node.children.map(c => nodeMap.get(c)).filter(Boolean) as typeof ir.graph.nodes
        const bodyXML = chain(bodyBlocks.map(b => emitStmt(b)))
        return `<block type="controls_if" id="${node.id}"><value name="IF0"><shadow type="logic_boolean"><field name="BOOL">TRUE</field></shadow></value><statement name="DO0">${bodyXML}</statement></block>`
      }
      case 'while': {
        const bodyBlocks = node.children.map(c => nodeMap.get(c)).filter(Boolean) as typeof ir.graph.nodes
        const bodyXML = chain(bodyBlocks.map(b => emitStmt(b)))
        return `<block type="py_while" id="${node.id}"><value name="TEST"><shadow type="logic_boolean"><field name="BOOL">TRUE</field></shadow></value><statement name="BODY">${bodyXML}</statement></block>`
      }
      case 'for': {
        const bodyBlocks = node.children.map(c => nodeMap.get(c)).filter(Boolean) as typeof ir.graph.nodes
        const bodyXML = chain(bodyBlocks.map(b => emitStmt(b)))
        return `<block type="controls_for" id="${node.id}"><field name="VAR">${node.label}</field><value name="TO"><shadow type="math_number"><field name="NUM">10</field></shadow></value><statement name="DO">${bodyXML}</statement></block>`
      }
      case 'function_def': {
        const bodyBlocks = node.children.map(c => nodeMap.get(c)).filter(Boolean) as typeof ir.graph.nodes
        const bodyXML = chain(bodyBlocks.map(b => emitStmt(b)))
        return `<block type="py_function_def" id="${node.id}"><field name="NAME">${node.label}</field><field name="ARGS"></field><statement name="BODY">${bodyXML}</statement></block>`
      }
      case 'import':
        return `<block type="py_import" id="${node.id}"><field name="MODULE">${node.label}</field></block>`
      case 'call':
        return `<block type="procedures_callnoreturn" id="${node.id}"><mutation name="${node.label}"/></block>`
      default:
        return ''
    }
  }

  // Chain multiple block XML strings via DOM manipulation
  function chain(blocks: string[]): string {
    if (blocks.length === 0) return ''
    if (blocks.length === 1) return blocks[0]
    const xml = `<xml xmlns="https://developers.google.com/blockly/xml">${blocks.join('')}</xml>`
    const parser = new DOMParser()
    const doc = parser.parseFromString(xml, 'text/xml')
    const allBlocks = Array.from(doc.querySelectorAll('block'))
    for (let i = 0; i < allBlocks.length - 1; i++) {
      const nextEl = doc.createElement('next')
      // The next block is always at index 1 in the CURRENT doc tree
      // (after removing the previous next block from the root level)
      const remaining = doc.querySelectorAll('block')
      if (remaining.length > 1) {
        const target = remaining[1]
        nextEl.appendChild(target)
        allBlocks[i].appendChild(nextEl)
      }
    }
    // Only serialize the top-level blocks (direct children of <xml>)
    const serializer = new XMLSerializer()
    const topBlocks = Array.from(doc.documentElement.children)
      .filter(el => el.tagName === 'block')
    return topBlocks.map(el => serializer.serializeToString(el)).join('')
  }

  // Top-level (non-child) nodes
  const topLevel = ir.graph.nodes.filter(n => !allChildren.has(n.id))
  const topXML = topLevel.map(n => emitStmt(n)).filter(Boolean)
  return chain(topXML)
}

export function BlocklyEditor({ ir, onCodeChange }: BlocklyEditorProps) {
  const containerRef = useRef<HTMLDivElement>(null)
  const workspaceRef = useRef<Blockly.WorkspaceSvg | null>(null)
  const updatingRef = useRef(false)
  const cbRef = useRef(onCodeChange)
  cbRef.current = onCodeChange

  useEffect(() => {
    const container = containerRef.current
    if (!container || workspaceRef.current) return

    const workspace = Blockly.inject(container, {
      theme: darkTheme,
      toolbox: {
        kind: 'categoryToolbox',
        contents: [
          { kind: 'category', name: 'Variables', colour: '#5BA58B', custom: 'VARIABLE' },
          { kind: 'category', name: 'Functions', colour: '#9A5BA5', custom: 'PROCEDURE' },
          { kind: 'category', name: 'Logic', colour: '#5B80A5', contents: [
            { kind: 'block', type: 'controls_if' },
            { kind: 'block', type: 'logic_boolean' },
            { kind: 'block', type: 'logic_compare' },
          ]},
          { kind: 'category', name: 'Loops', colour: '#5BA55B', contents: [
            { kind: 'block', type: 'controls_while' },
            { kind: 'block', type: 'controls_for' },
          ]},
          { kind: 'category', name: 'Math', colour: '#5B67A5', contents: [
            { kind: 'block', type: 'math_number' },
            { kind: 'block', type: 'math_arithmetic' },
          ]},
          { kind: 'category', name: 'Python', colour: '#3572A5', contents: [
            { kind: 'block', type: 'py_function_def' },
            { kind: 'block', type: 'py_return' },
            { kind: 'block', type: 'py_while' },
            { kind: 'block', type: 'py_import' },
            { kind: 'block', type: 'py_assign' },
          ]},
        ],
      },
      zoom: { controls: true, wheel: true, startScale: 0.9 },
      trashcan: true,
      move: { scrollbars: true, drag: true, wheel: true },
      grid: { spacing: 20, length: 3, colour: '#ffffff08', snap: true },
    })

    workspaceRef.current = workspace

    // Blockly → Code change listener
    workspace.addChangeListener((e: Blockly.Events.Abstract) => {
      if (updatingRef.current) return
      if (e.isUiEvent) return
      if (!cbRef.current) return
      // Debounce: wait for edit to complete
      setTimeout(() => {
        try {
          const code = pythonGenerator.workspaceToCode(workspace)
          if (code.trim()) cbRef.current!(code)
        } catch { /* ignore */ }
      }, 100)
    })
  }, [])

  useEffect(() => {
    const ws = workspaceRef.current
    if (!ws) return

    try {
      Blockly.Events.disable()
      updatingRef.current = true
      ws.clear()
      const xmlStr = buildXML(ir)
      if (xmlStr) {
        const fullXml = `<xml xmlns="https://developers.google.com/blockly/xml">${xmlStr}</xml>`
        const dom = Blockly.utils.xml.textToDom(fullXml)
        Blockly.Xml.domToWorkspace(dom, ws)
      }
    } catch (e) {
      console.error('Blockly update error:', e)
    } finally {
      updatingRef.current = false
      Blockly.Events.enable()
    }
  }, [ir])

  return <div ref={containerRef} style={{ width: '100%', height: '100%' }} />
}
