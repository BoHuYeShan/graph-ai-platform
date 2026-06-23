import { useCallback, useRef, useEffect } from 'react'
import { EditorState } from '@codemirror/state'
import { EditorView, keymap, lineNumbers, highlightActiveLine } from '@codemirror/view'
import { defaultKeymap, history, historyKeymap } from '@codemirror/commands'
import { syntaxHighlighting, defaultHighlightStyle } from '@codemirror/language'
import { linter } from '@codemirror/lint'
import type { Diagnostic } from '@codemirror/lint'
import { autocompletion, CompletionContext } from '@codemirror/autocomplete'
import { python } from '@codemirror/lang-python'
import { oneDark } from '@codemirror/theme-one-dark'

interface CodeViewProps {
  value: string
  onChange: (value: string) => void
}

// ── Python keyword completions (fallback when server unavailable) ──
const PY_KEYWORDS = [
  'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
  'try', 'while', 'with', 'yield', 'print', 'range', 'len', 'int', 'str',
  'list', 'dict', 'set', 'tuple', 'float', 'bool', 'map', 'filter', 'zip',
]

function pyCompletions(context: CompletionContext) {
  const word = context.matchBefore(/\w+/)
  if (!word || (word.from === word.to && !context.explicit)) return null
  const options = PY_KEYWORDS
    .filter(k => k.startsWith(word.text))
    .map(k => ({ label: k, type: 'keyword' }))
  return { from: word.from, options }
}

// ── Backend linter (debounced) ──
let _lintTimer: ReturnType<typeof setTimeout> | null = null
let _lintAbort: AbortController | null = null

async function pythonLint(view: EditorView): Promise<readonly Diagnostic[]> {
  const code = view.state.doc.toString()
  if (!code.trim()) return []

  return new Promise(resolve => {
    if (_lintTimer) clearTimeout(_lintTimer)
    if (_lintAbort) _lintAbort.abort()

    _lintTimer = setTimeout(async () => {
      const controller = new AbortController()
      _lintAbort = controller
      try {
        const res = await fetch('/api/lint', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ source: code }),
          signal: controller.signal,
        })
        if (!res.ok) { resolve([]); return }
        const data = await res.json()
        const diagnostics: Diagnostic[] = (data.issues || []).map((iss: any) => ({
          from: Math.max(0, view.state.doc.line(iss.line || 1).from + (iss.col || 1) - 1),
          to: view.state.doc.line(iss.line || 1).to,
          severity: iss.severity === 'error' ? 'error' : 'warning' as any,
          message: iss.message,
        }))
        resolve(diagnostics)
      } catch {
        resolve([])
      }
    }, 400)
  })
}

export function CodeView({ value, onChange }: CodeViewProps) {
  const editorRef = useRef<HTMLDivElement>(null)
  const viewRef = useRef<EditorView | null>(null)

  const onUpdate = useCallback(
    (update: any) => {
      if (update.docChanged) {
        onChange(update.state.doc.toString())
      }
    },
    [onChange]
  )

  useEffect(() => {
    if (!editorRef.current) return

    const state = EditorState.create({
      doc: value,
      extensions: [
        python(),
        oneDark,
        lineNumbers(),
        highlightActiveLine(),
        syntaxHighlighting(defaultHighlightStyle),
        history(),
        autocompletion({ override: [pyCompletions] }),
        linter(pythonLint, { delay: 500 }),
        keymap.of([...defaultKeymap, ...historyKeymap]),
        EditorView.updateListener.of(onUpdate),
        EditorView.theme({
          '&': { height: '100%' },
          '.cm-scroller': { overflow: 'auto' },
          '&.cm-focused': { outline: 'none' },
        }),
      ],
    })

    const view = new EditorView({ state, parent: editorRef.current })
    viewRef.current = view

    return () => {
      view.destroy()
      viewRef.current = null
    }
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  // Sync external value changes
  useEffect(() => {
    const view = viewRef.current
    if (!view) return
    const current = view.state.doc.toString()
    if (current !== value) {
      view.dispatch({
        changes: { from: 0, to: current.length, insert: value },
      })
    }
  }, [value])

  return (
    <div
      ref={editorRef}
      style={{
        width: '100%',
        height: '100%',
        overflow: 'hidden',
        background: '#1e1e1e',
      }}
    />
  )
}
