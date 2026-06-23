import { useState, useCallback, useRef, useEffect } from 'react'
import { GraphView } from './components/GraphView'
import { BlocklyEditor } from './components/BlocklyEditor'
import { CodeView } from './components/CodeView'
import { FileTree } from './components/FileTree'
import { Toolbar } from './components/Toolbar'
import type { IRGraph } from './types/ir'
import { sampleCode, sampleIR } from './data/samples'
import './App.css'

const PARSE_DEBOUNCE_MS = 600

function App() {
  const [code, setCode] = useState(sampleCode)
  const codeRef = useRef(sampleCode)
  const [ir, setIr] = useState<IRGraph>(sampleIR)
  const [view, setView] = useState<'code' | 'graph' | 'split'>('split')
  const [viewMode, setViewMode] = useState<'blueprint' | 'puzzle'>('blueprint')
  const [status, setStatus] = useState({ nodeCount: 0, edgeCount: 0, error: '' })
  const [output, setOutput] = useState('')
  const [running, setRunning] = useState(false)
  const [workspaceName] = useState('my_project')
  const [currentFile, setCurrentFile] = useState('main.py')
  const [showFileTree, setShowFileTree] = useState(true)
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const abortRef = useRef<AbortController | null>(null)

  const updateStatus = useCallback((newIr: IRGraph) => {
    setStatus({
      nodeCount: newIr.graph.nodes.length,
      edgeCount: newIr.graph.edges.length,
      error: '',
    })
  }, [])

  // Code → Graph: debounced auto-parse
  const doParse = useCallback(async (source: string) => {
    if (abortRef.current) abortRef.current.abort()
    const controller = new AbortController()
    abortRef.current = controller
    try {
      const res = await fetch('/api/parse', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ source, filename: 'untitled.py' }),
        signal: controller.signal,
      })
      const data = await res.json()
      if (data.ir) {
        setIr(data.ir)
        updateStatus(data.ir)
        setStatus(s => ({ ...s, error: '' }))
      }
    } catch (e: any) {
      if (e.name !== 'AbortError') {
        setStatus(s => ({ ...s, error: 'Parse failed' }))
        console.error('Parse error:', e)
      }
    }
  }, [updateStatus])

  const handleCodeChange = useCallback((newCode: string) => {
    setCode(newCode)
    // Skip if code hasn't actually changed (prevents circular loop)
    if (newCode === codeRef.current) return
    codeRef.current = newCode
    if (timerRef.current) clearTimeout(timerRef.current)
    timerRef.current = setTimeout(() => doParse(newCode), PARSE_DEBOUNCE_MS)
  }, [doParse])

  // Graph → Code
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

  // ▶ Run — execute code, show output
  const handleRun = useCallback(async () => {
    setRunning(true)
    setOutput('')
    try {
      const res = await fetch('/api/execute', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ir }),
      })
      const data = await res.json()
      if (data.status === 'ok') {
        setOutput(JSON.stringify(data.variables, null, 2))
      } else {
        setOutput(`Error: ${data.status}`)
      }
    } catch (e: any) {
      setOutput(`Runtime error: ${e.message || e}`)
    }
    setRunning(false)
  }, [ir])

  // File selection → load file into editor
  const handleFileSelect = useCallback(async (path: string) => {
    setCurrentFile(path)
    try {
      const res = await fetch('/api/workspace/read', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: workspaceName, path }),
      })
      const data = await res.json()
      if (data.content) {
        setCode(data.content)
        codeRef.current = data.content
        doParse(data.content)
      }
    } catch (e) {
      console.error('File read error:', e)
    }
  }, [workspaceName, doParse])

  // Initial parse
  useEffect(() => {
    doParse(sampleCode)
    updateStatus(sampleIR)
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  // Cleanup
  useEffect(() => {
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current)
      if (abortRef.current) abortRef.current.abort()
    }
  }, [])

  return (
    <div className="app">
      <Toolbar
        view={view}
        viewMode={viewMode}
        onViewChange={setView}
        onViewModeChange={setViewMode}
        onGenerate={handleGenerate}
        onRun={handleRun}
        onToggleFileTree={() => setShowFileTree(s => !s)}
        showFileTree={showFileTree}
        running={running}
        status={status}
      />
      <div className={`main-area view-${view}`}>
        <div className="editor-area">
          {view !== 'graph' && (
            <div className="panel panel-code">
              <CodeView value={code} onChange={handleCodeChange} />
            </div>
          )}
          {view !== 'code' && (
            <div className="panel panel-graph">
              {viewMode === 'blueprint' ? <GraphView ir={ir} /> : <BlocklyEditor ir={ir} onCodeChange={handleCodeChange} />}
            </div>
          )}
        </div>
        {showFileTree && (
          <FileTree
            workspaceName={workspaceName}
            onFileSelect={handleFileSelect}
            onFileCreate={(p) => console.log('Create:', p)}
            selectedPath={currentFile}
          />
        )}
      </div>
      {output && (
        <div className="output-panel">
          <div className="output-header">
            <span>Output</span>
            <button onClick={() => setOutput('')}>✕</button>
          </div>
          <pre className="output-body">{output}</pre>
        </div>
      )}
    </div>
  )
}

export default App
