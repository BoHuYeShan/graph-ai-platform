#!/usr/bin/env python3
"""
B.A.I.T. static site builder v3 — i18n support
Three portals: Academic / Archive / Terminal
Supports Chinese (zh), English (en), extensible to others.
"""
import shutil, re
from pathlib import Path
from markdown import Markdown
from markdown.extensions import extra, codehilite

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PUBLIC = ROOT / "public"
STATIC = ROOT / "static"
POLICIES = ROOT / "policies"
DATA = ROOT / "data"
GITHUB_REPO = "bohuyeshan/bait-core"

# ── i18n loader ────────────────────────────────────────────
def load_i18n():
    """Load i18n.toml → {lang: {key: value}}"""
    i18n = {}
    path = DATA / "i18n.toml"
    if not path.exists():
        return {"zh": {}, "en": {}}
    current_lang = None
    for line in path.read_text(encoding="utf-8").split("\n"):
        line = line.strip()
        if line.startswith("#") or not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            current_lang = line[1:-1]
            i18n[current_lang] = {}
        elif "=" in line and current_lang:
            k, _, v = line.partition("=")
            i18n[current_lang][k.strip()] = v.strip().strip('"')
    return i18n

I18N = load_i18n()

def t(lang, key, fallback=""):
    """Translate a key for a given language."""
    return I18N.get(lang, {}).get(key, I18N.get("en", {}).get(key, fallback))

# ── Markdown ──────────────────────────────────────────────
md_engine = Markdown(extensions=['extra','codehilite'],
    extension_configs={'codehilite':{'css_class':'highlight','guess_lang':False}})

def parse_fm(text):
    fm, body = {}, text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            body = parts[2].strip()
            for line in parts[1].strip().split("\n"):
                line = line.strip()
                if ":" in line:
                    k, _, v = line.partition(":")
                    fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body

def md2html(text):
    blocks, n = {}, [0]
    def save(m):
        n[0] += 1; k = f"\x00M{n[0]}\x00"; blocks[k] = m.group(0); return k
    text = re.sub(r'\$\$(.+?)\$\$', save, text)
    text = re.sub(r'\$(.+?)\$', save, text)
    html = md_engine.convert(text)
    md_engine.reset()
    for k, v in blocks.items():
        html = html.replace(k, v)
    return html

# ── Shells ─────────────────────────────────────────────────

def academic_shell(lang, title, content):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — {t(lang,'site_name')}</title>
<link rel="stylesheet" href="/static/css/academic.css">
<link rel="stylesheet" href="/static/css/code.css">
<script>MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}},svg:{{fontCache:'global'}}}};</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
<div class="journal-bar">
  {t(lang,'journal_bar')}
  · <a href="/about/">About</a>
  · <span style="float:right"><a href="/{'' if lang=='zh' else 'zh/' if lang=='en' else ''}">{t(lang,'lang_switch_to')}</a></span>
</div>
<header class="journal-masthead">
  <div class="journal-name">{t(lang,'site_name')}</div>
  <div class="journal-subtitle">{t(lang,'site_subtitle')}</div>
  <div class="journal-meta">ISSN 2998-0001 (Online) · Established 2025 · Community Editorial Review</div>
</header>
<nav class="journal-nav">
  <a href="/{'' if lang=='zh' else lang+'/'}">{t(lang,'nav_home')}</a>
  <a href="/{'' if lang=='zh' else lang+'/'}papers/">{t(lang,'nav_papers')}</a>
  <a href="/{'' if lang=='zh' else lang+'/'}workshop/">{t(lang,'nav_workshop')}</a>
  <a href="/{'' if lang=='zh' else lang+'/'}about/">{t(lang,'nav_about')}</a>
</nav>
<main class="academic-content">
{content}
</main>
<footer class="journal-footer">
  <div class="footer-disclosure">{t(lang,'footer_disclosure_academic')}</div>
  <div class="footer-links">
    <a href="/policies/disclaimer/">Disclaimer</a>
    <a href="/policies/code-of-conduct/">Code of Conduct</a>
    <a href="/policies/contributing/">Contributing</a>
    <a href="https://github.com/{GITHUB_REPO}/issues/new?template=takedown.yml">Takedown</a>
    <a href="https://github.com/{GITHUB_REPO}">GitHub</a>
  </div>
  <div class="journal-footer-watermark">
    Community Fictional Manuscript · Not a Journal Publication · Fictional Academic Workshop
  </div>
</footer>
</body>
</html>"""

def archive_shell(lang, title, content, classification=""):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>{title} — R.E.E.F. Archive</title>
<link rel="stylesheet" href="/static/css/archive.css">
<link rel="stylesheet" href="/static/css/code.css">
<script>MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}},svg:{{fontCache:'global'}}}};</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
<div class="archive-topbar">
  <span>R.E.E.F. ARCHIVE SYSTEM v4.0 // DIMENSIONAL CONTAINMENT: ACTIVE</span>
  <span><a href="/">→ Academic Portal</a> · <a href="/{'' if lang=='zh' else 'zh/' if lang=='en' else ''}archive/">{t(lang,'lang_switch_to')}</a></span>
</div>
<header class="archive-header">
  <div class="archive-logo">R.E.E.F. ARCHIVE</div>
  <div class="archive-tagline">Research Encyclopedia of Emerging Frontiers · Fictional Records Repository</div>
</header>
<nav class="archive-nav">
  <a href="/{'' if lang=='zh' else lang+'/'}archive/">{t(lang,'nav_archive_home')}</a>
  <a href="/{'' if lang=='zh' else lang+'/'}archive/cosmos/">{t(lang,'nav_cosmos')}</a>
  <a href="/{'' if lang=='zh' else lang+'/'}archive/records/">{t(lang,'nav_records')}</a>
  <a href="/{'' if lang=='zh' else lang+'/'}archive/wiki/">{t(lang,'nav_wiki')}</a>
  <a href="/terminal/">{t(lang,'nav_terminal')}</a>
</nav>
{classification}
<main class="archive-content">
{content}
</main>
<footer class="archive-footer">
  <div class="footer-disclosure">{t(lang,'footer_disclosure_archive')}</div>
  <div>
    <a href="/policies/disclaimer/">Disclaimer</a> ·
    <a href="/policies/code-of-conduct/">Code of Conduct</a> ·
    <a href="/policies/contributing/">Contributing</a> ·
    <a href="https://github.com/{GITHUB_REPO}/issues/new?template=takedown.yml">Takedown</a>
  </div>
</footer>
</body>
</html>"""

def classification_banner(fm, lang="en"):
    grade = fm.get("grade", "FG-0")
    ddi = fm.get("ddi", "0")
    dio = fm.get("dio", "—")
    grade_map = {
        "FG-0": ("F-0", "SURFACE RIPPLE", "fissure-0"),
        "FG-1": ("F-1", "MINOR FISSURE", "fissure-1"),
        "FG-2": ("F-2", "STABLE FISSURE", "fissure-2"),
        "FG-3": ("F-3", "DEEP RIFT", "fissure-3"),
        "TG-1": ("Σ", "STANDARD", "sigma"), "TG-2": ("Σ", "STANDARD", "sigma"), "TG-3": ("Σ", "STANDARD", "sigma"),
    }
    label, desc, css_cls = grade_map.get(grade, ("F-0", "UNCLASSIFIED", "fissure-0"))
    ddi_colors = {"0":"#888","1":"#4a88aa","2":"#cc9944","3":"#cc6644","4":"#cc2222","5":"#000"}
    color = ddi_colors.get(str(ddi), "#888")
    return f"""
<div class="classification-banner">
<div class="classification-card">
  <div class="class-header">{t(lang,'classification_label')} · OBJECT: ONTOLOGICAL FISSURE SIGNAL</div>
  <div class="class-body">
    <div class="class-level class-{css_cls}">{label} — {desc}</div>
    <div class="class-props" style="margin-top:10px">
      <span class="prop-label">DIO:</span><span class="prop-value">{dio} (internal fictional archive identifier)</span>
      <span class="prop-label">FDI:</span><span class="prop-value" style="color:{color}">{ddi} / 5 — FISSURE DEVIATION INDEX</span>
      <span class="prop-label">STATUS:</span><span class="prop-value">ARCHIVED · COMMUNITY SCREENING PASSED</span>
    </div>
    <p style="margin-top:8px;font-size:0.78em;color:#888;">{t(lang,'classification_note')}</p>
  </div>
</div>
</div>"""

# ── Build ──────────────────────────────────────────────────
def build():
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()
    shutil.copytree(STATIC, PUBLIC / "static", dirs_exist_ok=True)
    shutil.copy2(ROOT / "_dev.html", PUBLIC / "_dev.html")

    manuscripts_dir = CONTENT / "manuscripts"
    manuscripts_index = []

    # ── Walk and build manuscript pages ──
    for md_path in sorted(manuscripts_dir.rglob("*.md")):
        rel = md_path.relative_to(manuscripts_dir)
        parts = list(rel.parts)
        filename = parts[-1]  # index.md or index.en.md or index.ja.md

        # Determine language
        if filename == "index.md":
            lang = "zh"  # default original language is zh
        elif filename.startswith("index.") and filename.endswith(".md"):
            lang = filename.rsplit(".", 2)[1]  # index.en.md → en
        else:
            continue

        text = md_path.read_text(encoding="utf-8")
        fm, body = parse_fm(text)
        fm_lang = fm.get("lang", lang)
        title = fm.get("title", "Untitled")

        # Build canonical URL prefix
        # zh: /2025/0001/   en: /en/2025/0001/   ja: /ja/2025/0001/
        url_parts = parts[:-1]  # year/seq
        if fm_lang == "zh":
            url_prefix = "/".join(url_parts)
        else:
            url_prefix = fm_lang + "/" + "/".join(url_parts)

        body_html = md2html(body)

        # Academic page
        academic_page = academic_shell(fm_lang, title, body_html)
        dest = PUBLIC / url_prefix
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "index.html").write_text(academic_page, encoding="utf-8")

        # Archive page — always at /<lang>/archive/papers/...
        banner = classification_banner(fm, fm_lang)
        archive_page = archive_shell(fm_lang, title, body_html, banner)
        arch_prefix = ("" if fm_lang == "zh" else fm_lang + "/") 
        dest2 = PUBLIC / arch_prefix / "archive" / "papers" / url_parts[0] / url_parts[1]
        dest2.mkdir(parents=True, exist_ok=True)
        (dest2 / "index.html").write_text(archive_page, encoding="utf-8")

        manuscripts_index.append({
            "title": title, "dio": fm.get("dio",""), "lang": fm_lang,
            "academic_url": "/" + url_prefix + "/",
            "archive_url": "/" + arch_prefix + "archive/papers/" + "/".join(url_parts) + "/",
            "date": fm.get("date",""), "grade": fm.get("grade","FG-2"),
        })

    # ── Academic portal pages ──
    for lang, prefix in [("zh", ""), ("en", "en/")]:
        # Homepage
        ms_items = ""
        for ms in reversed(manuscripts_index):
            ms_items += f'<li><div class="ms-title"><a href="/{ms["academic_url"]}">{ms["title"]}</a></div><div class="ms-meta">{ms["dio"]} · {ms["date"]} · [{ms["lang"]}]</div></li>'
        home_html = academic_shell(lang, "Home", f"<h1>Latest Manuscripts</h1><p>{t(lang,'footer_disclosure_academic')}</p><ul class=\"manuscript-list\">{ms_items}</ul>")
        d = PUBLIC / (prefix if prefix else "")
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(home_html, encoding="utf-8")

        # About
        about_body = md2html(f"""## {t(lang,'nav_about')}
B.A.I.T. is a **community fictional academic manuscript workshop**.
{t(lang,'footer_disclosure_academic')}
### What We Are Not
- Not a real academic journal
- Not a preprint server
- Not an indexing service
- Not a certification body""")
        d2 = PUBLIC / prefix / "about"
        d2.mkdir(parents=True, exist_ok=True)
        (d2 / "index.html").write_text(academic_shell(lang, t(lang,'nav_about'), about_body), encoding="utf-8")

        # Workshop
        workshop_body = md2html(f"""## {t(lang,'nav_workshop')}
1. Fork → Create manuscript → Submit PR → Community screening → Archive
### Review Pipeline
| Stage | Description |
|-------|-------------|
| CAST | Submission Intake |
| HOOK | Community Editorial Screening |
| CATCH | Style & Safety Review |
| RELEASE | Archive Publication |
**Community screening is not real peer review.**""")
        d3 = PUBLIC / prefix / "workshop"
        d3.mkdir(parents=True, exist_ok=True)
        (d3 / "index.html").write_text(academic_shell(lang, t(lang,'nav_workshop'), workshop_body), encoding="utf-8")

        # Papers listing
        d4 = PUBLIC / prefix / "papers"
        d4.mkdir(parents=True, exist_ok=True)
        (d4 / "index.html").write_text(academic_shell(lang, t(lang,'nav_papers'), f"<h1>{t(lang,'nav_papers')}</h1><ul class=\"manuscript-list\">{ms_items}</ul>"), encoding="utf-8")

    # ── Archive portal pages ──
    for lang in ["zh", "en"]:
        pref = "" if lang == "zh" else lang + "/"
        # Archive home
        items = ""
        for ms in reversed(manuscripts_index):
            items += f'- [{ms["dio"]} — {ms["title"]}](/{ms["archive_url"]}) `F-2 STABLE FISSURE` [{ms["lang"]}]\n'
        arch_body = md2html(f"## R.E.E.F. Archive\n\n> {t(lang,'footer_disclosure_archive')}\n\n### Available Records\n{items}\n\n→ [Terminal](/terminal/)")
        d = PUBLIC / pref / "archive"
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(archive_shell(lang, "Archive Home", arch_body), encoding="utf-8")

        # Sub-pages
        for sub in ["cosmos", "records", "wiki"]:
            d2 = PUBLIC / pref / "archive" / sub
            d2.mkdir(parents=True, exist_ok=True)
            body = md2html(f"## {sub.title()}\n\n*{t(lang,'nav_'+sub) if t(lang,'nav_'+sub) else sub.title()} — under construction.*")
            (d2 / "index.html").write_text(archive_shell(lang, sub.title(), body), encoding="utf-8")

    # ── Terminal ──
    terminal_html = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Terminal Access — B.A.I.T. Archive</title>
<link rel="stylesheet" href="/static/css/archive.css"><link rel="stylesheet" href="/static/css/terminal.css">
</head>
<body class="terminal-page">
<div class="archive-topbar"><span>R.E.E.F. ARCHIVE TERMINAL // SESSION: ANONYMOUS</span><span><a href="/archive/">← Archive</a></span></div>
<main class="terminal-wrapper"><div id="terminal"></div></main>
<script src="/static/js/terminal.js"></script>
</body></html>"""
    (PUBLIC / "terminal").mkdir(exist_ok=True)
    (PUBLIC / "terminal" / "index.html").write_text(terminal_html, encoding="utf-8")

    # ── Policy pages ──
    policy_routes = {"DISCLAIMER.md":"disclaimer","CODE_OF_CONDUCT.md":"code-of-conduct",
                     "CONTRIBUTING.md":"contributing","TAKEDOWN.md":"takedown","PRIVACY.md":"privacy"}
    for src_name, slug in policy_routes.items():
        src = POLICIES / src_name
        if not src.exists(): continue
        text = src.read_text(encoding="utf-8")
        _, body = parse_fm(text)
        page = academic_shell("en", src.stem.replace("_"," ").title(), md2html(body))
        dest = PUBLIC / "policies" / slug
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "index.html").write_text(page, encoding="utf-8")

    print(f"Built {len(manuscripts_index)} manuscript(s) → {PUBLIC}")
    for ms in manuscripts_index:
        print(f"  [{ms['lang']}] {ms['dio']} → {ms['academic_url']}")

if __name__ == "__main__":
    build()
