#!/usr/bin/env python3
"""workspace_service — file system CRUD for PyGraph workspaces."""

from __future__ import annotations
from pathlib import Path
from typing import Optional
import os, shutil, json

DEFAULT_WORKSPACE_DIR = Path.home() / ".pygraph" / "workspaces"


class WorkspaceService:
    """Manage PyGraph workspace files on disk."""

    def __init__(self, root: Optional[Path] = None):
        self.root = root or DEFAULT_WORKSPACE_DIR
        self.root.mkdir(parents=True, exist_ok=True)

    def list_files(self, ws_name: str, subpath: str = "") -> list[dict]:
        """Return file tree for a workspace as [{name, path, type, size, gitStatus}]."""
        ws_dir = self.root / ws_name
        if not ws_dir.exists():
            return []
        target = ws_dir / subpath if subpath else ws_dir
        if not target.exists() or not target.is_dir():
            return []

        entries = []
        for f in sorted(target.iterdir()):
            name = f.name
            rel = f.relative_to(ws_dir).as_posix()
            if f.is_dir():
                entries.append({"name": name, "path": rel, "type": "directory", "size": 0, "gitStatus": ""})
            else:
                entries.append({"name": name, "path": rel, "type": "file", "size": f.stat().st_size, "gitStatus": ""})
        return entries

    def read_file(self, ws_name: str, file_path: str) -> Optional[str]:
        """Read a file's content."""
        full = (self.root / ws_name / file_path).resolve()
        # Security: ensure path is within workspace
        if not str(full).startswith(str((self.root / ws_name).resolve())):
            return None
        if not full.exists() or not full.is_file():
            return None
        return full.read_text(encoding="utf-8")

    def write_file(self, ws_name: str, file_path: str, content: str) -> bool:
        """Write content to a file (create or overwrite)."""
        full = (self.root / ws_name / file_path).resolve()
        if not str(full).startswith(str((self.root / ws_name).resolve())):
            return False
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(content, encoding="utf-8")
        return True

    def create_file(self, ws_name: str, file_path: str) -> bool:
        """Create an empty file."""
        return self.write_file(ws_name, file_path, "")

    def delete(self, ws_name: str, path_str: str) -> bool:
        """Delete a file or directory."""
        full = (self.root / ws_name / path_str).resolve()
        if not str(full).startswith(str((self.root / ws_name).resolve())):
            return False
        if not full.exists():
            return False
        if full.is_dir():
            shutil.rmtree(full)
        else:
            full.unlink()
        return True

    def rename(self, ws_name: str, old_path: str, new_path: str) -> bool:
        """Rename/move a file."""
        src = (self.root / ws_name / old_path).resolve()
        dst = (self.root / ws_name / new_path).resolve()
        if not str(src).startswith(str((self.root / ws_name).resolve())):
            return False
        if not str(dst).startswith(str((self.root / ws_name).resolve())):
            return False
        if not src.exists():
            return False
        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)
        return True

    def list_workspaces(self) -> list[str]:
        """List all workspace names."""
        return [d.name for d in self.root.iterdir() if d.is_dir() and not d.name.startswith(".")]
