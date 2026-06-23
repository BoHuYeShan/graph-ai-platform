import { useState, useEffect, useCallback } from 'react'

interface FileEntry {
  name: string
  path: string
  type: 'file' | 'directory'
  size: number
  gitStatus: string
}

interface FileTreeProps {
  workspaceName: string
  onFileSelect: (path: string) => void
  onFileCreate: (path: string) => void
  selectedPath?: string
}

export function FileTree({ workspaceName, onFileSelect, onFileCreate, selectedPath }: FileTreeProps) {
  const [files, setFiles] = useState<FileEntry[]>([])
  const [loading, setLoading] = useState(true)
  const [collapsed, setCollapsed] = useState<Set<string>>(new Set())
  const dirs = files.filter(f => f.type === 'directory')
  const fileItems = files.filter(f => f.type === 'file')

  const loadFiles = useCallback(async () => {
    setLoading(true)
    try {
      const res = await fetch('/api/workspace/files', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: workspaceName }),
      })
      const data = await res.json()
      setFiles(data.files || [])
    } catch { /* ignore */ }
    setLoading(false)
  }, [workspaceName])

  useEffect(() => {
    loadFiles()
  }, [loadFiles])

  const toggleDir = (path: string) => {
    setCollapsed(prev => {
      const next = new Set(prev)
      if (next.has(path)) next.delete(path)
      else next.add(path)
      return next
    })
  }

  const gitIcon = (status: string) => {
    if (!status) return ''
    if (status === 'M') return '🟡'
    if (status === 'A') return '🟢'
    if (status === '?') return '🔵'
    if (status === 'D') return '🔴'
    return status
  }

  return (
    <div className="file-tree">
      <div className="file-tree-header">
        <span>📁 {workspaceName}</span>
        <button className="ft-btn" onClick={loadFiles} title="Refresh">⟳</button>
        <button className="ft-btn" onClick={() => onFileCreate('new_file.py')} title="New file">+</button>
      </div>
      <div className="file-tree-body">
        {loading && <div className="ft-loading">Loading...</div>}
        {!loading && dirs.length === 0 && fileItems.length === 0 && (
          <div className="ft-empty">Empty workspace</div>
        )}
        {dirs.map(d => (
          <div key={d.path}>
            <div
              className={`ft-item ft-dir ${collapsed.has(d.path) ? 'collapsed' : ''}`}
              onClick={() => toggleDir(d.path)}
            >
              <span className="ft-icon">{collapsed.has(d.path) ? '📂' : '📁'}</span>
              <span className="ft-name">{d.name}</span>
            </div>
          </div>
        ))}
        {fileItems.map(f => (
          <div
            key={f.path}
            className={`ft-item ft-file ${selectedPath === f.path ? 'selected' : ''}`}
            onClick={() => onFileSelect(f.path)}
          >
            <span className="ft-icon">
              {f.name.endsWith('.py') ? '🐍' : f.name.endsWith('.md') ? '📝' : '📄'}
            </span>
            <span className="ft-name">{f.name}</span>
            {f.gitStatus && <span className="ft-git">{gitIcon(f.gitStatus)}</span>}
          </div>
        ))}
      </div>
    </div>
  )
}
