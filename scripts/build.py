#!/usr/bin/env python3
"""
B.A.I.T. static site builder v4 — i18n + TOC sidebar + article controls
"""
import shutil, re
from pathlib import Path
from markdown import Markdown
from markdown.extensions import extra, codehilite, toc

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PUBLIC = ROOT / "public"
STATIC = ROOT / "static"
POLICIES = ROOT / "policies"
DATA = ROOT / "data"
GITHUB_REPO = "bohuyeshan/bait-core"

# ── i18n ────────────────────────────────────────────────────
def load_i18n():
    i18n = {}
    path = DATA / "i18n.toml"
    if not path.exists(): return {"zh": {}, "en": {}}
    cl = None
    for line in path.read_text(encoding="utf-8").split("\n"):
        line = line.strip()
        if line.startswith("#") or not line: continue
        if line.startswith("[") and line.endswith("]"): cl = line[1:-1]; i18n[cl] = {}
        elif "=" in line and cl:
            k, _, v = line.partition("="); i18n[cl][k.strip()] = v.strip().strip('"')
    return i18n
I18N = load_i18n()
def t(lang, key, fb=""): return I18N.get(lang, {}).get(key, I18N.get("en", {}).get(key, fb))

# ── Markdown ──────────────────────────────────────────────
md_engine = Markdown(extensions=['extra','codehilite','toc'],
    extension_configs={'codehilite':{'css_class':'highlight','guess_lang':False},
                       'toc':{'permalink':False,'baselevel':2}})

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
    for k, v in blocks.items(): html = html.replace(k, v)
    return html

def extract_toc(html):
    """Extract h2/h3 from HTML to build a TOC sidebar list."""
    headings = re.findall(r'<h([23])\s+id="([^"]+)"[^>]*>(.+?)</h[23]>', html)
    if len(headings) < 2: return ""
    items = ""
    for level, aid, text in headings:
        cls = "toc-h2" if level == "2" else "toc-h3"
        items += f'<li class="{cls}"><a href="#{aid}">{text}</a></li>'
    return f'<nav class="toc-sidebar"><h4>Contents</h4><ul>{items}</ul></nav>'

# ── Shells ─────────────────────────────────────────────────

LANG_SWITCHER = """<div class="lang-switch">
  <a href="{other_url}" title="{other_label}">{lang_label}</a>
</div>"""

ARTICLE_TOOLBAR = """<div class="article-toolbar">
  <button class="tool-btn" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" title="Back to top">↑ Top</button>
  <span class="tool-stage" title="Review stage">{stage}</span>
</div>"""

def academic_shell(lang, title, content, toc_html="", other_url="/", stage=""):
    other_label = t(lang, 'lang_switch_to')
    prefix = "" if lang == "zh" else lang + "/"
    ls = LANG_SWITCHER.format(other_url=other_url, other_label=other_label,
        lang_label="EN" if lang == "zh" else "中文")
    tb = ARTICLE_TOOLBAR.format(stage=stage) if stage else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — {t(lang,'site_name')}</title>
<link rel="stylesheet" href="/static/css/academic.css">
<link rel="stylesheet" href="/static/css/code.css">
<script>MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}},svg:{{fontCache:'global'}}}};</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
<div class="journal-bar">
  {t(lang,'journal_bar')} · <a href="/{prefix}about/">About</a>
  <span style="float:right">{ls}</span>
</div>
<header class="journal-masthead">
  <div class="journal-name">{t(lang,'site_name')}</div>
  <div class="journal-subtitle">{t(lang,'site_subtitle')}</div>
  <div class="journal-meta">ISSN 2998-0001 (Online) · Established 2025 · Community Editorial Review</div>
</header>
<nav class="journal-nav">
  <a href="/{prefix}">{t(lang,'nav_home')}</a>
  <a href="/{prefix}papers/">{t(lang,'nav_papers')}</a>
  <a href="/{prefix}workshop/">{t(lang,'nav_workshop')}</a>
  <a href="/{prefix}about/">{t(lang,'nav_about')}</a>
</nav>
<div class="article-layout">
  <aside class="article-sidebar">{toc_html}</aside>
  <main class="academic-content">
{tb}
{content}
  </main>
</div>
<footer class="journal-footer">
  <div class="footer-disclosure">{t(lang,'footer_disclosure_academic')}</div>
  <div class="footer-links">
    <a href="/policies/disclaimer/">Disclaimer</a> · <a href="/policies/code-of-conduct/">Code of Conduct</a> ·
    <a href="/policies/contributing/">Contributing</a> ·
    <a href="https://github.com/{GITHUB_REPO}/issues/new?template=takedown.yml">Takedown</a> ·
    <a href="https://github.com/{GITHUB_REPO}">GitHub</a>
  </div>
  <div class="journal-footer-watermark">Community Fictional Manuscript · Not a Journal Publication</div>
</footer>
</body>
</html>"""

def archive_shell(lang, title, content, classification="", other_url="/"):
    other_label = t(lang, 'lang_switch_to')
    pref = "" if lang == "zh" else lang + "/"
    ls = LANG_SWITCHER.format(other_url=other_url, other_label=other_label,
        lang_label="EN" if lang == "zh" else "中文")
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>{title} — R.E.E.F. Archive</title>
<link rel="stylesheet" href="/static/css/archive.css"><link rel="stylesheet" href="/static/css/code.css">
<script>MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}},svg:{{fontCache:'global'}}}};</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
<div class="archive-topbar">
  <span>R.E.E.F. ARCHIVE SYSTEM v4.0</span>
  <span><a href="/{pref}">Academic Portal</a> · <a href="/{pref}archive/">Archive</a> · {ls}</span>
</div>
<header class="archive-header">
  <div class="archive-logo">R.E.E.F. ARCHIVE</div>
  <div class="archive-tagline">Research Encyclopedia of Emerging Frontiers · Fictional Records Repository</div>
</header>
<nav class="archive-nav">
  <a href="/{pref}archive/">{t(lang,'nav_archive_home')}</a>
  <a href="/{pref}archive/cosmos/">{t(lang,'nav_cosmos')}</a>
  <a href="/{pref}archive/records/">{t(lang,'nav_records')}</a>
  <a href="/{pref}archive/wiki/">{t(lang,'nav_wiki')}</a>
  <a href="/terminal/">{t(lang,'nav_terminal')}</a>
</nav>
{classification}
<main class="archive-content">
{content}
</main>
<footer class="archive-footer">
  <div class="footer-disclosure">{t(lang,'footer_disclosure_archive')}</div>
  <div>
    <a href="/policies/disclaimer/">Disclaimer</a> · <a href="/policies/code-of-conduct/">Code of Conduct</a> ·
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
      <span class="prop-label">DIO:</span><span class="prop-value">{dio}</span>
      <span class="prop-label">FDI:</span><span class="prop-value" style="color:{color}">{ddi} / 5 — FISSURE DEVIATION INDEX</span>
      <span class="prop-label">STATUS:</span><span class="prop-value">ARCHIVED · COMMUNITY SCREENING PASSED</span>
    </div>
    <p style="margin-top:8px;font-size:0.78em;color:#888;">{t(lang,'classification_note')}</p>
  </div>
</div>
</div>"""

# ── Build ──────────────────────────────────────────────────
def build():
    if PUBLIC.exists(): shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()
    shutil.copytree(STATIC, PUBLIC / "static", dirs_exist_ok=True)
    shutil.copy2(ROOT / "_dev.html", PUBLIC / "_dev.html")

    manuscripts_dir = CONTENT / "manuscripts"
    manuscripts_index = []

    # First pass: collect all manuscripts with their language info
    manuscripts = {}  # dio -> {zh: (fm,body,path), en: (fm,body,path)}
    for md_path in sorted(manuscripts_dir.rglob("*.md")):
        rel = md_path.relative_to(manuscripts_dir)
        parts = list(rel.parts)
        filename = parts[-1]
        if filename == "index.md": lang = "zh"
        elif filename.startswith("index.") and filename.endswith(".md"): lang = filename.rsplit(".", 2)[1]
        else: continue
        text = md_path.read_text(encoding="utf-8")
        fm, body = parse_fm(text)
        dio = fm.get("dio", "")
        if dio not in manuscripts: manuscripts[dio] = {}
        manuscripts[dio][lang] = (fm, body, parts[:-1])

    # Second pass: build pages
    for dio, langs in manuscripts.items():
        for lang, (fm, body, url_parts) in langs.items():
            title = fm.get("title", "Untitled")
            body_html = md2html(body)
            toc_html = extract_toc(body_html)
            stage = f"{fm.get('grade','?')} · {fm.get('review_status','?')}"

            # Determine URLs for language switching
            url_prefix = "/".join(url_parts)
            academic_url = "/" + ("" if lang == "zh" else lang + "/") + url_prefix + "/"
            arch_url = "/" + ("" if lang == "zh" else lang + "/") + "archive/papers/" + url_prefix + "/"

            # Other language URL (for switcher)
            other_lang = "en" if lang == "zh" else "zh"
            if other_lang in langs:
                other_url = "/" + ("" if other_lang == "zh" else other_lang + "/") + url_prefix + "/"
            else:
                other_url = "/" + ("" if other_lang == "zh" else other_lang + "/")

            # Academic page
            acad = academic_shell(lang, title, body_html, toc_html, other_url, stage)
            dest = PUBLIC / ("" if lang == "zh" else lang) / url_parts[0] / url_parts[1]
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "index.html").write_text(acad, encoding="utf-8")

            # Archive page
            banner = classification_banner(fm, lang)
            arch_other = "/" + ("" if other_lang == "zh" else other_lang + "/") + "archive/papers/" + url_prefix + "/" if other_lang in langs else "/" + ("" if other_lang == "zh" else other_lang + "/") + "archive/"
            arch = archive_shell(lang, title, body_html, banner, arch_other)
            dest2 = PUBLIC / ("" if lang == "zh" else lang) / "archive" / "papers" / url_parts[0] / url_parts[1]
            dest2.mkdir(parents=True, exist_ok=True)
            (dest2 / "index.html").write_text(arch, encoding="utf-8")

            manuscripts_index.append({"title": title, "dio": dio, "lang": lang,
                "academic_url": academic_url, "archive_url": arch_url,
                "date": fm.get("date",""), "grade": fm.get("grade","FG-2")})

    # ── Portal pages ──
    for lang, prefix in [("zh", ""), ("en", "en/")]:
        other = "/en/" if lang == "zh" else "/"
        # Deduplicate manuscripts by DIO, keep one entry per DIO
        seen_dio = set()
        ms_items = ""
        for ms in reversed(manuscripts_index):
            if ms["dio"] in seen_dio: continue
            seen_dio.add(ms["dio"])
            # Build language badge
            dio_langs = [m for m in manuscripts_index if m["dio"] == ms["dio"]]
            lang_badges = " ".join(f'<span class="lang-badge">{m["lang"].upper()}</span>' for m in dio_langs)
            ms_items += f'<li><div class="ms-title"><a href="{ms["academic_url"]}">{ms["title"]}</a> {lang_badges}</div><div class="ms-meta">{ms["dio"]} · {ms["date"]}</div></li>'
        # Home
        home = academic_shell(lang, "Home", f"<h1>Latest Manuscripts</h1><p>{t(lang,'footer_disclosure_academic')}</p><ul class=\"manuscript-list\">{ms_items}</ul>")
        (PUBLIC / (prefix if prefix else ".") / "index.html").write_text(home, encoding="utf-8")
        # About
        ab = md2html(f"## {t(lang,'nav_about')}\n\nB.A.I.T. is a **community fictional academic manuscript workshop**.\n\n{t(lang,'footer_disclosure_academic')}")
        (PUBLIC / prefix / "about").mkdir(parents=True, exist_ok=True)
        (PUBLIC / prefix / "about" / "index.html").write_text(academic_shell(lang, t(lang,'nav_about'), ab, "", other), encoding="utf-8")
        # Workshop
        ws = md2html(f"## {t(lang,'nav_workshop')}\n\n1. Fork → Create → Submit PR → Community screening → Archive.\n\n**Community screening is not real peer review.**")
        (PUBLIC / prefix / "workshop").mkdir(parents=True, exist_ok=True)
        (PUBLIC / prefix / "workshop" / "index.html").write_text(academic_shell(lang, t(lang,'nav_workshop'), ws, "", other), encoding="utf-8")
        # Papers list — deduplicate by DIO
        seen_dio2 = set()
        pl = ""
        for ms in reversed(manuscripts_index):
            if ms["dio"] in seen_dio2: continue
            seen_dio2.add(ms["dio"])
            pl += f'<li><div class="ms-title"><a href="{ms["academic_url"]}">{ms["title"]}</a></div><div class="ms-meta">{ms["dio"]} · {ms["date"]}</div></li>'
        (PUBLIC / prefix / "papers").mkdir(parents=True, exist_ok=True)
        (PUBLIC / prefix / "papers" / "index.html").write_text(academic_shell(lang, t(lang,'nav_papers'), f"<h1>{t(lang,'nav_papers')}</h1><ul class=\"manuscript-list\">{pl}</ul>", "", other), encoding="utf-8")
        # Archive home — deduplicate by DIO
        seen_dio = set()
        ai = ""
        for ms in reversed(manuscripts_index):
            if ms["dio"] in seen_dio: continue
            seen_dio.add(ms["dio"])
            ai += f'- [{ms["dio"]} — {ms["title"]}]({ms["archive_url"]}) `F-2 STABLE FISSURE`\n'
        ab2 = md2html(f"## R.E.E.F. Archive\n\n> {t(lang,'footer_disclosure_archive')}\n\n### Available Records\n{ai}\n\n→ [Terminal](/terminal/)")
        (PUBLIC / prefix / "archive").mkdir(parents=True, exist_ok=True)
        (PUBLIC / prefix / "archive" / "index.html").write_text(archive_shell(lang, "Archive Home", ab2, "", other), encoding="utf-8")
        # Archive sub-pages
        for sub in ["cosmos", "records", "wiki"]:
            (PUBLIC / prefix / "archive" / sub).mkdir(parents=True, exist_ok=True)
            (PUBLIC / prefix / "archive" / sub / "index.html").write_text(archive_shell(lang, sub.title(), md2html(f"## {sub.title()}\n\n*Under construction.*"), "", other), encoding="utf-8")

    # ── Terminal ──
    (PUBLIC / "terminal").mkdir(exist_ok=True)
    (PUBLIC / "terminal" / "index.html").write_text("""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Terminal — B.A.I.T.</title>
<link rel="stylesheet" href="/static/css/archive.css"><link rel="stylesheet" href="/static/css/terminal.css">
</head><body class="terminal-page">
<div class="archive-topbar"><span>R.E.E.F. TERMINAL // ANONYMOUS</span><span><a href="/archive/">← Archive</a></span></div>
<main class="terminal-wrapper"><div id="terminal"></div></main>
<script src="/static/js/terminal.js"></script></body></html>""", encoding="utf-8")

    # ── Policies ──
    pr = {"DISCLAIMER.md":"disclaimer","CODE_OF_CONDUCT.md":"code-of-conduct","CONTRIBUTING.md":"contributing","TAKEDOWN.md":"takedown","PRIVACY.md":"privacy"}
    for src, slug in pr.items():
        p = POLICIES / src
        if not p.exists(): continue
        _, body = parse_fm(p.read_text(encoding="utf-8"))
        d = PUBLIC / "policies" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(academic_shell("en", src.replace("_"," ").replace(".md","").title(), md2html(body)), encoding="utf-8")

    print(f"Built {len(manuscripts_index)} manuscript(s)")
    for ms in manuscripts_index:
        print(f"  [{ms['lang']}] {ms['dio']} → {ms['academic_url']}")

if __name__ == "__main__":
    build()
