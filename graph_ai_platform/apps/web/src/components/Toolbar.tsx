import { useState } from 'react'

interface ToolbarProps {
  view: 'code' | 'graph' | 'split'
  onViewChange: (view: 'code' | 'graph' | 'split') => void
  onAIEdit: (instruction: string) => void
}

export function Toolbar({ view, onViewChange, onAIEdit }: ToolbarProps) {
  const [aiInput, setAiInput] = useState('')
  const [showAI, setShowAI] = useState(false)

  const handleSubmit = () => {
    if (aiInput.trim()) {
      onAIEdit(aiInput.trim())
      setAiInput('')
    }
  }

  return (
    <div className="toolbar">
      <div className="toolbar-left">
        <span className="toolbar-title">🕸️ graph-ai</span>
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
      </div>
      <div className="toolbar-right">
        <button onClick={() => setShowAI(!showAI)}>
          🤖 AI Edit
        </button>
        <a
          href="http://localhost:8765/docs"
          target="_blank"
          rel="noopener noreferrer"
          className="toolbar-link"
        >
          API
        </a>
      </div>
      {showAI && (
        <div className="toolbar-ai-bar">
          <input
            type="text"
            value={aiInput}
            onChange={(e) => setAiInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSubmit()}
            placeholder="Describe the edit you want to make..."
            className="ai-input"
          />
          <button onClick={handleSubmit}>Apply</button>
        </div>
      )}
    </div>
  )
}
