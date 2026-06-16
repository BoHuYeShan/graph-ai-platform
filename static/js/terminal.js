/**
 * B.A.I.T. Terminal Emulator — v0
 * Minimal pseudo-terminal with predefined command set.
 * All "hidden" commands are in this file; this is a narrative feature, not a security boundary.
 */
(function() {
  const TERM = document.getElementById('terminal');
  if (!TERM) return;

  // ── command definitions ──
  const cmds = {
    help: {
      desc: 'Available commands: ls, cat, who, status, ping, cd, access, decrypt, help, clear, exit',
      exec: () => 'Available: <span class="term-info">ls</span> <span class="term-info">cat</span> <span class="term-info">who</span> <span class="term-info">status</span> <span class="term-info">ping</span> <span class="term-info">cd</span> <span class="term-info">access</span> <span class="term-info">decrypt</span> <span class="term-info">help</span> <span class="term-info">clear</span> <span class="term-info">exit</span>'
    },
    ls: {
      desc: 'List directory contents',
      exec: (args) => {
        if (args.includes('quarantine')) return '<span class="term-error">Permission denied: quarantine/ requires CLEARANCE-3</span>';
        if (args.includes('/')) return '<span class="term-warn">logs/  quarantine/  papers/  home/  memos/</span>';
        return '<span class="term-output">notes.txt  draft.txt  .secret/  anomalies/</span>';
      }
    },
    'cat notes.txt': {
      desc: '',
      exec: () => 'DIMENSIONAL STABILITY REPORT #47\nLeak rate: 0.0042 TB/s [INCREASING]\nSource: UNKNOWN // COSMOS-MIX-001\nRecommendation: escalate to H.A.D.A.L. archive.\n\n<span class="term-warn">[WARN] Baseline integrity compromised.</span>'
    },
    'cat draft.txt': {
      desc: '',
      exec: () => 'The Thucydides Trap extension to galactic civilizations is<br>not entirely fictional. There were ... signals.<br><br><span class="term-output">[Document truncated — see /archive/records/AR-2025-0001]</span>'
    },
    'cat .secret/readme': {
      desc: '',
      exec: () => '<span class="term-highlight">To those reading source code:</span><br>Yes, all "hidden" commands are in terminal.js.<br>That is not a bug. This is a narrative layer, not a security layer.<br>You bypassed nothing — you simply read the script.<br>Welcome to the Archive.<br><br>→ <a href="/archive/" style="color:#88ccff">/archive/</a>'
    },
    who: {
      desc: 'Show logged-in users',
      exec: () => '<span class="term-output">dr_null     pts/0  192.168.7.42<br>anonymous   pts/1  10.0.0.1<br><span class="term-warn">[UNKNOWN]   pts/?  █.█.█.█</span></span>'
    },
    status: {
      desc: 'System status',
      exec: () => '<span class="term-output">Dimensional Stability: <span class="term-warn">87.3%</span> [████████░░]<br>Leak Rate: <span class="term-critical">0.0042 TB/s</span><br>Active Cosmos Nodes: 3<br>Quarantined Records: 7</span>'
    },
    ping: {
      desc: 'Ping baseline reality',
      exec: () => '<span class="term-output">PING baseline-reality.local (::1)<br>64 bytes from ::1: time=<span class="term-warn">847ms</span><br>64 bytes from ::1: time=<span class="term-critical">1204ms</span><br>--- baseline-reality.local ping statistics ---<br>2 packets, 2 received, <span class="term-warn">50% packet loss</span></span>'
    },
    cd: {
      desc: 'Change directory',
      exec: (args) => {
        const dir = args[0] || '';
        if (dir === 'quarantine') return '<span class="term-error">cd: quarantine/: Permission denied (CLEARANCE-3 required)</span>';
        if (dir === '.secret') return '<span class="term-output">Entered .secret/ — use <span class="term-info">ls</span> and <span class="term-info">cat readme</span></span>';
        return '<span class="term-output">Changed to ' + (dir || '/') + '</span>';
      }
    },
    access: {
      desc: 'Request clearance escalation',
      exec: (args) => {
        if (args[0] === 'MIRROR') return '<span class="term-highlight">ACCESS GRANTED: CLEARANCE-3<br>You may now access quarantine/.<br>DIO key: DIO:B.A.I.T.2025.0001 → verify at /terminal/</span>';
        return '<span class="term-error">access: Invalid clearance key. Try harder.</span>';
      }
    },
    decrypt: {
      desc: 'Decrypt dimensional data',
      exec: (args) => {
        if (args.includes('logs/dimensional_leak/quarantine/')) {
          return '<span class="term-highlight">DECRYPTING...<br>Result: /archive/records/AR-2025-0001<br>Hash path: /d3e7f1a9b2c4/</span>';
        }
        return '<span class="term-error">decrypt: No target specified or invalid path.</span>';
      }
    },
    clear: {
      desc: 'Clear terminal',
      exec: () => { TERM.innerHTML = ''; return null; }
    },
    exit: {
      desc: 'Exit terminal session',
      exec: () => '<span class="term-output">Session terminated. <a href="/archive/" style="color:#88ccff">Return to Archive</a></span>'
    }
  };

  // ── easter eggs ──
  const eggs = {
    'sudo': '<span class="term-error">sudo: This system does not use sudo. It uses 神权 (divine authority). You do not have it.</span>',
    'rm -rf /': '<span class="term-error">rm: Dimensional containment protocols prevent recursive deletion.</span>',
    'whoami': '<span class="term-output">anonymous // or are you?</span>',
    'bait': '<span class="term-highlight">Bureau of Advanced Interdisciplinary Theories.<br>You already know what this is. Keep digging.</span>'
  };

  // ── terminal state ──
  let history = [];
  let histIdx = -1;
  let promptPrefix = 'anonymous@archive:~$ ';

  function print(html) {
    const line = document.createElement('div');
    line.className = 'term-line';
    line.innerHTML = html;
    TERM.appendChild(line);
    TERM.scrollTop = TERM.scrollHeight;
  }

  function showPrompt() {
    const line = document.createElement('div');
    line.className = 'term-input-line';
    line.innerHTML = '<span class="term-prompt">' + promptPrefix + '</span>';
    const input = document.createElement('input');
    input.className = 'term-cmd';
    input.setAttribute('spellcheck', 'false');
    input.setAttribute('autocomplete', 'off');
    line.appendChild(input);
    TERM.appendChild(line);
    input.focus();
    TERM.scrollTop = TERM.scrollHeight;

    input.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        const cmd = input.value.trim();
        input.disabled = true;
        // Echo the command
        const echoLine = document.createElement('div');
        echoLine.className = 'term-line';
        echoLine.innerHTML = '<span class="term-prompt">' + promptPrefix + '</span>' + escapeHtml(cmd);
        TERM.insertBefore(echoLine, line);
        TERM.removeChild(line);

        if (cmd) {
          history.push(cmd);
          histIdx = history.length;
          processCommand(cmd);
        }
        showPrompt();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (histIdx > 0) {
          histIdx--;
          input.value = history[histIdx];
        }
      } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (histIdx < history.length - 1) {
          histIdx++;
          input.value = history[histIdx];
        } else {
          histIdx = history.length;
          input.value = '';
        }
      }
    });
  }

  function processCommand(raw) {
    const parts = raw.split(/\s+/);
    const main = parts[0].toLowerCase();
    const args = parts.slice(1);

    // Exact match first
    if (cmds[raw]) {
      const result = cmds[raw].exec(args);
      if (result !== null) print(result);
      return;
    }
    // Easter eggs
    if (eggs[raw]) {
      print(eggs[raw]);
      return;
    }
    // Command match
    if (cmds[main]) {
      const result = cmds[main].exec(args);
      if (result !== null) print(result);
      return;
    }
    // Partial match — check if raw starts with a known multi-word command
    for (const key of Object.keys(cmds)) {
      if (key.includes(' ') && raw.startsWith(key)) {
        const result = cmds[key].exec(raw.substring(key.length).trim().split(/\s+/));
        if (result !== null) print(result);
        return;
      }
    }
    // Fallback
    print('<span class="term-error">bash: ' + escapeHtml(main) + ': command not found. Type <span class="term-info">help</span> for available commands.</span>');
  }

  function escapeHtml(str) {
    return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }

  // ── init ──
  print('<span class="term-highlight">B.A.I.T. Archive Terminal v4.0</span>');
  print('<span class="term-output">Dimensional containment: ACTIVE</span>');
  print('<span class="term-warn">[WARN] Baseline integrity at 87.3% — leakage detected</span>');
  print('<span class="term-output">Type <span class="term-info">help</span> for available commands.</span>');
  print('');
  showPrompt();
})();
