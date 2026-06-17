# Architecture Decision Record

## Context
This directory starts a new project: a Python-first visual AI programming platform.
- Python ↔ Graph bidirectional editing
- IR: `graph-ai.json`
- Web frontend (React + React Flow)
- Self-built core logic (no fork of GPL/AGPL repos)

## Scope of MVP
- **Must**: module-level statements, if/elif/else, for, while, function def, class def, variable assign, function call, return, import
- **Defer**: list/dict comprehensions, try/except, decorators, async, generators
- **Exclude**: metaprogramming, monkey patching, arbitrary eval/exec

## License Boundaries
- **MIT** for all new code
- **No** code copy from GPL/AGPL/NOASSERTION-licensed repositories
- Reference repos may only inspire design patterns, not source lines

## Execution Order
1. IR schema → fixtures → parser → codegen → roundtrip → runtime → web editor → AI protocol

## Contact
Plan document: `.opencode/extendai-lab/plans/python-first-visual-ai-platform.md`
