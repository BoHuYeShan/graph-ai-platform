interface ToolbarProps {
  view: 'code' | 'graph' | 'split'
  onViewChange: (view: 'code' | 'graph' | 'split') => void
  onGenerate: () => void
  onRun: () => void
  running: boolean
  status: { nodeCount: number; edgeCount: number; error: string }
}

export function Toolbar({ view, onViewChange, onGenerate, onRun, running, status }: ToolbarProps) {
  return (
    <div className="toolbar">
      <div className="toolbar-left">
        <span className="toolbar-title">🧩 PyGraph</span>
        <div className="toolbar-views">
          <button className={view === 'code' ? 'active' : ''} onClick={() => onViewChange('code')}>
            Code
          </button>
          <button className={view === 'split' ? 'active' : ''} onClick={() => onViewChange('split')}>
            Split
          </button>
          <button className={view === 'graph' ? 'active' : ''} onClick={() => onViewChange('graph')}>
            Graph
          </button>
        </div>
        <span className="toolbar-status">
          {status.error ? (
            <span className="status-error">{status.error}</span>
          ) : (
            <span className="status-ok">
              {status.nodeCount} nodes · {status.edgeCount} edges
            </span>
          )}
        </span>
      </div>
      <div className="toolbar-right">
        <button onClick={onGenerate}>Generate →</button>
        <button className="btn-run" onClick={onRun} disabled={running}>
          {running ? '⏳' : '▶'} Run
        </button>
      </div>
    </div>
  )
}
