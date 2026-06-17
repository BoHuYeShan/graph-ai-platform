import { useState, useCallback } from 'react'
import { GraphView } from './components/GraphView'
import { CodeView } from './components/CodeView'
import { Toolbar } from './components/Toolbar'
import type { IRGraph } from './types/ir'
import { sampleCode, sampleIR } from './data/samples'
import './App.css'

function App() {
  const [code, setCode] = useState(sampleCode)
  const [ir, setIr] = useState<IRGraph>(sampleIR)
  const [view, setView] = useState<'code' | 'graph' | 'split'>('split')
  const [isDirty, setIsDirty] = useState(false)

  // Code → Graph sync
  const handleCodeChange = useCallback(async (newCode: string) => {
    setCode(newCode)
    setIsDirty(true)
  }, [])

  const handleParse = useCallback(async () => {
    try {
      const res = await fetch('/api/parse', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ source: code }),
      })
      const data = await res.json()
      if (data.ir) setIr(data.ir)
      setIsDirty(false)
    } catch (e) {
      console.error('Parse error:', e)
    }
  }, [code])

  // Graph → Code sync
  const handleGenerate = useCallback(async () => {
    try {
      const res = await fetch('/api/codegen', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ir }),
      })
      const data = await res.json()
      if (data.code) setCode(data.code)
    } catch (e) {
      console.error('Codegen error:', e)
    }
  }, [ir])

  // AI Edit
  const handleAIEdit = useCallback(async (instruction: string) => {
    try {
      const res = await fetch('/api/ai/apply', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ir, instruction }),
      })
      const data = await res.json()
      if (data.ir) setIr(data.ir)
    } catch (e) {
      console.error('AI edit error:', e)
    }
  }, [ir])

  // Layout
  const codePanel = view === 'graph' ? null : (
    <div className="panel panel-code">
      <div className="panel-header">
        <span>Python Source</span>
        <button onClick={handleParse} disabled={!isDirty}>▶ Parse</button>
      </div>
      <CodeView value={code} onChange={handleCodeChange} />
    </div>
  )

  const graphPanel = view === 'code' ? null : (
    <div className="panel panel-graph">
      <div className="panel-header">
        <span>Graph IR</span>
        <button onClick={handleGenerate}>▶ Generate</button>
      </div>
      <GraphView ir={ir} />
    </div>
  )

  return (
    <div className="app">
      <Toolbar
        view={view}
        onViewChange={setView}
        onAIEdit={handleAIEdit}
      />
      <div className={`main-area view-${view}`}>
        {codePanel}
        {graphPanel}
      </div>
    </div>
  )
}

export default App
