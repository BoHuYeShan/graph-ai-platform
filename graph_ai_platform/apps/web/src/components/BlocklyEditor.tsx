import { useEffect, useRef } from 'react'
import * as Blockly from 'blockly'
import 'blockly/blocks'
import { pythonGenerator, Order } from 'blockly/python'
import type { IRGraph } from '../types/ir'

interface BlocklyEditorProps {
  ir: IRGraph
}

// ── Custom block definitions ──

const PY_BLOCKS = {
  import_block: {
    init: function (this: Blockly.Block) {
      this.appendDummyInput().appendField('import').appendField(new Blockly.FieldTextInput('os'), 'MODULE')
      this.setPreviousStatement(true, null)
      this.setNextStatement(true, null)
      this.setColour(120)
    },
  },
  from_import_block: {
    init: function (this: Blockly.Block) {
      this.appendDummyInput()
        .appendField('from')
        .appendField(new Blockly.FieldTextInput('os'), 'MODULE')
        .appendField('import')
        .appendField(new Blockly.FieldTextInput('path'), 'NAME')
      this.setPreviousStatement(true, null)
      this.setNextStatement(true, null)
      this.setColour(120)
    },
  },
  function_def: {
    init: function (this: Blockly.Block) {
      this.appendDummyInput()
        .appendField('def')
        .appendField(new Blockly.FieldTextInput('func'), 'NAME')
        .appendField('(')
        .appendField(new Blockly.FieldTextInput('args'), 'ARGS')
        .appendField(')')
        .appendField(':')
      this.appendStatementInput('BODY').setCheck(null)
      this.setOutput(false)
      this.setColour(290)
    },
  },
  class_def: {
    init: function (this: Blockly.Block) {
      this.appendDummyInput()
        .appendField('class')
        .appendField(new Blockly.FieldTextInput('MyClass'), 'NAME')
        .appendField(':')
      this.appendStatementInput('BODY').setCheck(null)
      this.setColour(210)
    },
  },
  return_block: {
    init: function (this: Blockly.Block) {
      this.appendValueInput('VALUE').setCheck(null).appendField('return')
      this.setPreviousStatement(true, null)
      this.setNextStatement(true, null)
      this.setColour(60)
    },
  },
  while_block: {
    init: function (this: Blockly.Block) {
      this.appendValueInput('TEST').setCheck(null).appendField('while').appendField('')
      this.appendStatementInput('BODY').setCheck(null)
      this.setPreviousStatement(true, null)
      this.setNextStatement(true, null)
      this.setColour(120)
    },
  },
}

// ── Register custom blocks ──
Object.entries(PY_BLOCKS).forEach(([name, config]) => {
  Blockly.Blocks[name] = config
})

// ── Python generator for custom blocks ──
pythonGenerator.forBlock['import_block'] = (block: Blockly.Block) => {
  const module = block.getFieldValue('MODULE')
  return [`import ${module}\n`, 0]
}
pythonGenerator.forBlock['from_import_block'] = (block: Blockly.Block) => {
  const module = block.getFieldValue('MODULE')
  const name = block.getFieldValue('NAME')
  return [`from ${module} import ${name}\n`, 0]
}
pythonGenerator.forBlock['function_def'] = (block: Blockly.Block) => {
  const name = block.getFieldValue('NAME')
  const args = block.getFieldValue('ARGS')
  const body = pythonGenerator.statementToCode(block, 'BODY')
  return [`def ${name}(${args}):\n${body}`, 0 as any]
}
pythonGenerator.forBlock['class_def'] = (block: Blockly.Block) => {
  const name = block.getFieldValue('NAME')
  const body = pythonGenerator.statementToCode(block, 'BODY')
  return [`class ${name}:\n${body}`, 0 as any]
}
pythonGenerator.forBlock['return_block'] = (block: Blockly.Block) => {
  const value = pythonGenerator.valueToCode(block, 'VALUE', Order.NONE) || ''
  return [`return ${value}\n`, 0]
}
pythonGenerator.forBlock['while_block'] = (block: Blockly.Block) => {
  const test = pythonGenerator.valueToCode(block, 'TEST', Order.NONE) || 'True'
  const body = pythonGenerator.statementToCode(block, 'BODY')
  return [`while ${test}:\n${body}`, 0 as any]
}

// ── Map IR to Blockly workspace ──
function irToBlocks(workspace: Blockly.WorkspaceSvg, ir: IRGraph) {
  workspace.clear()
  const xmlBlocks: string[] = []

  for (const n of ir.graph.nodes) {
    switch (n.type) {
      case 'assign': {
        // assign: `<block type="variables_set"><field name="VAR">${n.label}</field><value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value></block>`
        xmlBlocks.push(`<block type="variables_set" id="${n.id}"><field name="VAR">${n.label}</field><value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow></value></block>`)
        break
      }
      case 'if': {
        xmlBlocks.push(`<block type="controls_if" id="${n.id}"><value name="IF0"><shadow type="logic_boolean"><field name="BOOL">TRUE</field></shadow></value></block>`)
        break
      }
      case 'while': {
        xmlBlocks.push(`<block type="while_block" id="${n.id}"><value name="TEST"><shadow type="logic_boolean"><field name="BOOL">TRUE</field></shadow></value></block>`)
        break
      }
      case 'for': {
        xmlBlocks.push(`<block type="controls_for" id="${n.id}"><field name="VAR">i</field><value name="FROM"><shadow type="math_number"><field name="NUM">1</field></shadow></value><value name="TO"><shadow type="math_number"><field name="NUM">10</field></shadow></value></block>`)
        break
      }
      case 'function_def': {
        xmlBlocks.push(`<block type="function_def" id="${n.id}"><field name="NAME">${n.label}</field><field name="ARGS"></field></block>`)
        break
      }
      case 'class_def': {
        xmlBlocks.push(`<block type="class_def" id="${n.id}"><field name="NAME">${n.label}</field></block>`)
        break
      }
      case 'return': {
        xmlBlocks.push(`<block type="return_block" id="${n.id}"></block>`)
        break
      }
      case 'import': {
        xmlBlocks.push(`<block type="import_block" id="${n.id}"><field name="MODULE">${n.label}</field></block>`)
        break
      }
      case 'import_from': {
        xmlBlocks.push(`<block type="from_import_block" id="${n.id}"><field name="MODULE">${n.label}</field><field name="NAME">${n.value || '*'}</field></block>`)
        break
      }
      case 'call': {
        xmlBlocks.push(`<block type="procedures_callnoreturn" id="${n.id}"><mutation name="${n.label}"/></block>`)
        break
      }
      case 'literal': {
        xmlBlocks.push(`<block type="math_number" id="${n.id}"><field name="NUM">${n.value ?? 0}</field></block>`)
        break
      }
      case 'name': {
        xmlBlocks.push(`<block type="variables_get" id="${n.id}"><field name="VAR">${n.label}</field></block>`)
        break
      }
      case 'binop': {
        xmlBlocks.push(`<block type="math_arithmetic" id="${n.id}"><field name="OP">ADD</field><value name="A"><shadow type="math_number"><field name="NUM">0</field></shadow></value><value name="B"><shadow type="math_number"><field name="NUM">0</field></shadow></value></block>`)
        break
      }
    }
  }

  if (xmlBlocks.length > 0) {
    const xmlStr = `<xml xmlns="https://developers.google.com/blockly/xml">${xmlBlocks.join('')}</xml>`
    const dom = Blockly.utils.xml.textToDom(xmlStr)
    Blockly.Xml.domToWorkspace(dom, workspace)
  }
}

export function BlocklyEditor({ ir }: BlocklyEditorProps) {
  const containerRef = useRef<HTMLDivElement>(null)
  const workspaceRef = useRef<Blockly.WorkspaceSvg | null>(null)

  useEffect(() => {
    const container = containerRef.current
    if (!container || workspaceRef.current) return

    const workspace = Blockly.inject(container, {
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
            { kind: 'block', type: 'function_def' },
            { kind: 'block', type: 'class_def' },
            { kind: 'block', type: 'return_block' },
            { kind: 'block', type: 'import_block' },
            { kind: 'block', type: 'from_import_block' },
            { kind: 'block', type: 'while_block' },
          ]},
        ],
      },
      zoom: { controls: true, wheel: true, startScale: 0.9 },
      trashcan: true,
      move: { scrollbars: true, drag: true, wheel: true },
    })

    workspaceRef.current = workspace
  }, [])

  useEffect(() => {
    if (!workspaceRef.current) return
    irToBlocks(workspaceRef.current, ir)
  }, [ir])

  return (
    <div
      ref={containerRef}
      style={{ width: '100%', height: '100%' }}
    />
  )
}
