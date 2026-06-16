#!/usr/bin/env python3
"""
B.A.I.T. static site builder v5 — proper markdown + advanced components + day/night
"""
import shutil, re
from pathlib import Path
from markdown import Markdown
from markdown.extensions import extra, codehilite
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PUBLIC = ROOT / "public"
STATIC = ROOT / "static"
POLICIES = ROOT / "policies"
DATA = ROOT / "data"
GITHUB_REPO = "bohuyeshan/bait-core"

# ── i18n ──
def load_i18n():
    i18n = {}; cl = None
    p = DATA / "i18n.toml"
    if not p.exists(): return {"zh": {}, "en": {}}
    for line in p.read_text(encoding="utf-8").split("\n"):
        line = line.strip()
        if line.startswith("#") or not line: continue
        if line.startswith("[") and line.endswith("]"): cl = line[1:-1]; i18n[cl] = {}
        elif "=" in line and cl:
            k, _, v = line.partition("="); i18n[cl][k.strip()] = v.strip().strip('"')
    return i18n
I18N = load_i18n()
def t(lang, key, fb=""): return I18N.get(lang, {}).get(key, I18N.get("en", {}).get(key, fb))

# ── Advanced Markdown Preprocessor ─────────────────────────
class BaitPreprocessor(Preprocessor):
    """Handle B.A.I.T. custom markdown: ::fissure-banner::, ::callout::, ::meta-table::"""
    def run(self, lines):
        result = []
        in_meta = False; in_callout = False; in_fissure = False
        meta_rows = []; callout_lines = []; fissure_lines = []
        for line in lines:
            # Fissure banner block
            if line.strip() == ":::fissure":
                in_fissure = True; fissure_lines = []; continue
            if in_fissure:
                if line.strip() == ":::": in_fissure = False; result.append("<!--FISSURE-->"); continue
                fissure_lines.append(line); continue
            # Callout block
            if line.strip().startswith(":::callout"):
                in_callout = True; callout_lines = [line.strip()[10:].strip()]; continue
            if in_callout:
                if line.strip() == ":::": in_callout = False; result.append("<!--CALLOUT:" + "|".join(callout_lines) + "-->"); continue
                callout_lines.append(line); continue
            # Meta table block
            if line.strip() == ":::meta":
                in_meta = True; meta_rows = []; continue
            if in_meta:
                if line.strip() == ":::":
                    in_meta = False
                    tbl = '<div class="ac-meta-table"><table>\n'
                    for r in meta_rows:
                        cells = [c.strip() for c in r.strip("|").split("|")]
                        if len(cells) >= 2:
                            tbl += f'<tr><td class="meta-key">{cells[0].strip()}</td><td class="meta-val">{cells[1].strip()}</td></tr>\n'
                    tbl += '</table></div>'
                    result.append(tbl); continue
                meta_rows.append(line); continue
            result.append(line)
        return result

class BaitExtension(Extension):
    def extendMarkdown(self, md): md.preprocessors.register(BaitPreprocessor(md), 'bait', 25)

# ── Markdown engine ──
md_engine = Markdown(extensions=['extra','codehilite',BaitExtension()],
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
    text = re.sub(r'\$\$(.+?)\$\$', save, text, flags=re.DOTALL)
    text = re.sub(r'\$(.+?)\$', save, text)
    html = md_engine.convert(text)
    md_engine.reset()
    for k, v in blocks.items(): html = html.replace(k, v)
    # Post-process callout markers
    html = re.sub(r'<!--CALLOUT:(.*?)-->', lambda m: f'<div class="ac-callout"><div class="ac-callout-title">{m.group(1).split("|")[0]}</div>{"".join(f"<p>{l}</p>" for l in m.group(1).split("|")[1:])}</div>', html)
    html = re.sub(r'<!--FISSURE-->', '<div class="ac-fissure-note">⚠️ R.E.E.F. 裂隙观测报告 — 以下内容整理自裂隙信号。裂隙本身为虚构设定。</div>', html)
    return html

def extract_toc(html):
    headings = re.findall(r'<h([23])\s+id="([^"]+)"[^>]*>(.+?)</h[23]>', html)
    if len(headings) < 2: return ""
    items = ""
    for level, aid, text in headings:
        cls = "toc-h2" if level == "2" else "toc-h3"
        items += f'<li class="{cls}"><a href="#{aid}">{text}</a></li>'
    return f'<ul>{items}</ul>'

# ── Shells ──
def academic_shell(lang, title, content, toc_html="", other_url="/", stage=""):
    prefix = "" if lang == "zh" else lang + "/"
    ls = f'<span class="ac-lang-switch"><a href="{other_url}">{"EN" if lang=="zh" else "中文"}</a></span>'
    tb = f'<div class="ac-toolbar"><button class="ac-tool-btn" onclick="scrollTo({{top:0,behavior:\"smooth\"}})">↑</button><button class="ac-tool-btn theme-toggle" onclick="document.body.classList.toggle(\"dark\")">◐</button><span class="ac-tool-stage">{stage}</span></div>' if stage else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — {t(lang,'site_name')}</title>
<link rel="stylesheet" href="/static/css/theme.css">
<link rel="stylesheet" href="/static/css/code.css">
<script>MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}},svg:{{fontCache:'global'}}}};</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body class="academic">
<div class="ac-topbar">{t(lang,'journal_bar')} · <a href="/{prefix}about/">About</a> {ls}</div>
<header class="ac-masthead">
  <div class="ac-logo">{open(ROOT/"static/img/logo.svg").read() if (ROOT/"static/img/logo.svg").exists() else "B.A.I.T."}</div>
  <div class="ac-journal-name">{t(lang,'site_name')}</div>
  <div class="ac-subtitle">{t(lang,'site_subtitle')}</div>
  <div class="ac-issn">ISSN 2998-0001 (Online) · Established 2025 · Community Editorial Review</div>
</header>
<nav class="ac-nav">
  <a href="/{prefix}">{t(lang,'nav_home')}</a>
  <a href="/{prefix}papers/">{t(lang,'nav_papers')}</a>
  <a href="/{prefix}workshop/">{t(lang,'nav_workshop')}</a>
  <a href="/{prefix}about/">{t(lang,'nav_about')}</a>
</nav>
<div class="ac-layout">
  <aside class="ac-sidebar"><nav class="ac-toc"><h4>Contents</h4>{toc_html}</nav></aside>
  <main class="ac-main">{tb}{content}</main>
</div>
<footer class="ac-footer">
  <div class="ac-footer-disclosure">{t(lang,'footer_disclosure_academic')}</div>
  <div><a href="/policies/disclaimer/">Disclaimer</a> <a href="/policies/code-of-conduct/">Code of Conduct</a> <a href="/policies/contributing/">Contributing</a> <a href="https://github.com/{GITHUB_REPO}/issues/new?template=takedown.yml">Takedown</a> <a href="https://github.com/{GITHUB_REPO}">GitHub</a></div>
  <div class="ac-footer-watermark">Community Fictional Manuscript · Not a Journal Publication</div>
</footer>
</body>
</html>"""

def archive_shell(lang, title, content, classification="", other_url="/", toc_html="", stage=""):
    pref = "" if lang == "zh" else lang + "/"
    ls = f'<a href="{other_url}">{"EN" if lang=="zh" else "中文"}</a>'
    tb = f'<div class="ar-toolbar"><button class="ar-tool-btn" onclick="scrollTo({{top:0,behavior:\"smooth\"}})">↑</button><button class="ar-tool-btn" onclick="document.body.classList.toggle(\"ar-light\")">◐</button><span class="ar-tool-stage">{stage}</span></div>' if stage else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>{title} — R.E.E.F. Archive</title>
<link rel="stylesheet" href="/static/css/theme.css"><link rel="stylesheet" href="/static/css/code.css">
<script>MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}},svg:{{fontCache:'global'}}}};</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body class="archive">
<div class="ar-topbar"><span>R.E.E.F. ARCHIVE SYSTEM v4.0</span><span><a href="/{pref}">Academic</a> · <a href="/{pref}archive/">Archive</a> · {ls}</span></div>
<header class="ar-header"><div class="ar-logo">R.E.E.F. ARCHIVE</div><div class="ar-tagline">Research Encyclopedia of Emerging Frontiers · Fictional Records</div></header>
<nav class="ar-nav"><a href="/{pref}archive/">{t(lang,'nav_archive_home')}</a><a href="/{pref}archive/cosmos/">{t(lang,'nav_cosmos')}</a><a href="/{pref}archive/records/">{t(lang,'nav_records')}</a><a href="/{pref}archive/wiki/">{t(lang,'nav_wiki')}</a><a href="/terminal/">{t(lang,'nav_terminal')}</a></nav>
{classification}
<div class="ar-layout"><aside class="ar-sidebar"><nav class="ar-toc"><h4>Contents</h4>{toc_html}</nav></aside><main class="ar-main">{tb}{content}</main></div>
<footer class="ar-footer"><div class="ar-footer-disclosure">{t(lang,'footer_disclosure_archive')}</div><div><a href="/policies/disclaimer/">Disclaimer</a> <a href="/policies/code-of-conduct/">Code of Conduct</a> <a href="/policies/contributing/">Contributing</a> <a href="https://github.com/{GITHUB_REPO}/issues/new?template=takedown.yml">Takedown</a></div></footer>
</body>
</html>"""

def classification_banner(fm, lang="en"):
    grade = fm.get("grade", "FG-0"); ddi = fm.get("ddi", "0"); dio = fm.get("dio", "—")
    gmap = {"FG-0":("F-0","SURFACE RIPPLE","ar-fissure-0"),"FG-1":("F-1","MINOR FISSURE","ar-fissure-1"),"FG-2":("F-2","STABLE FISSURE","ar-fissure-2"),"FG-3":("F-3","DEEP RIFT","ar-fissure-3"),"TG-1":("Σ","STANDARD","ar-sigma"),"TG-2":("Σ","STANDARD","ar-sigma"),"TG-3":("Σ","STANDARD","ar-sigma")}
    label, desc, css_cls = gmap.get(grade, ("F-0","UNCLASSIFIED","ar-fissure-0"))
    dcolors = {"0":"#888","1":"#4a8899","2":"#c49944","3":"#c46644","4":"#c42222","5":"#000"}
    color = dcolors.get(str(ddi),"#888")
    return f"""<div class="ar-classification"><div class="ar-class-card"><div class="ar-class-header">{t(lang,'classification_label')} · ONTOLOGICAL FISSURE SIGNAL</div><div class="ar-class-body"><div class="ar-class-level {css_cls}">{label} — {desc}</div><div class="ar-class-props"><span class="ar-prop-label">DIO:</span><span class="ar-prop-value">{dio}</span><span class="ar-prop-label">FDI:</span><span class="ar-prop-value" style="color:{color}">{ddi}/5 — FISSURE DEVIATION INDEX</span><span class="ar-prop-label">STATUS:</span><span class="ar-prop-value">ARCHIVED</span></div><p style="margin-top:8px;font-size:0.72em;color:var(--ar-text-dim)">{t(lang,'classification_note')}</p></div></div></div>"""

# ── Build ──
def build():
    if PUBLIC.exists(): shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(); shutil.copytree(STATIC, PUBLIC/"static", dirs_exist_ok=True)
    shutil.copy2(ROOT/"_dev.html", PUBLIC/"_dev.html")
    ms_dir = CONTENT/"manuscripts"; ms_index = []
    ms_data = {}  # dio -> {lang: (fm, body, parts)}
    for p in sorted(ms_dir.rglob("*.md")):
        rel = p.relative_to(ms_dir); parts = list(rel.parts); fn = parts[-1]
        if fn == "index.md": lang = "zh"
        elif fn.startswith("index.") and fn.endswith(".md"): lang = fn.rsplit(".",2)[1]
        else: continue
        fm, body = parse_fm(p.read_text(encoding="utf-8"))
        dio = fm.get("dio",""); ms_data.setdefault(dio,{})[lang] = (fm, body, parts[:-1])

    for dio, langs in ms_data.items():
        for lang, (fm, body, url_parts) in langs.items():
            title = fm.get("title","Untitled")
            body_html = md2html(body)
            toc_html = extract_toc(body_html)
            stage = f"{fm.get('grade','?')} · {fm.get('review_status','?')}"
            url_prefix = "/".join(url_parts)
            ac_url = "/" + ("" if lang=="zh" else lang+"/") + url_prefix + "/"
            ar_url = "/" + ("" if lang=="zh" else lang+"/") + "archive/papers/" + url_prefix + "/"
            other_lang = "en" if lang=="zh" else "zh"
            other_url = "/" + ("" if other_lang=="zh" else other_lang+"/") + url_prefix + "/" if other_lang in langs else "/" + ("" if other_lang=="zh" else other_lang+"/")
            # Academic
            (PUBLIC/("" if lang=="zh" else lang)/url_parts[0]/url_parts[1]).mkdir(parents=True,exist_ok=True)
            (PUBLIC/("" if lang=="zh" else lang)/url_parts[0]/url_parts[1]/"index.html").write_text(academic_shell(lang,title,body_html,toc_html,other_url,stage),encoding="utf-8")
            # Archive
            banner = classification_banner(fm, lang)
            arch_other = "/"+( "" if other_lang=="zh" else other_lang+"/")+"archive/papers/"+url_prefix+"/" if other_lang in langs else "/"+( "" if other_lang=="zh" else other_lang+"/")+"archive/"
            (PUBLIC/("" if lang=="zh" else lang)/"archive"/"papers"/url_parts[0]/url_parts[1]).mkdir(parents=True,exist_ok=True)
            (PUBLIC/("" if lang=="zh" else lang)/"archive"/"papers"/url_parts[0]/url_parts[1]/"index.html").write_text(archive_shell(lang,title,body_html,banner,arch_other,toc_html,stage),encoding="utf-8")
            ms_index.append({"title":title,"dio":dio,"lang":lang,"academic_url":ac_url,"archive_url":ar_url,"date":fm.get("date",""),"grade":fm.get("grade","FG-2")})

    # Portal homepages
    for lang, prefix in [("zh",""),("en","en/")]:
        other = "/en/" if lang=="zh" else "/"
        seen = set(); ms_items = ""
        for ms in reversed(ms_index):
            if ms["dio"] in seen: continue; seen.add(ms["dio"])
            dio_langs = [m for m in ms_index if m["dio"]==ms["dio"]]
            badges = " ".join(f'<span class="ac-lang-badge">{m["lang"].upper()}</span>' for m in dio_langs)
            ms_items += f'<li><div class="ac-list-title"><a href="{ms["academic_url"]}">{ms["title"]}</a> {badges}</div><div class="ac-list-meta">{ms["dio"]} · {ms["date"]}</div></li>'
        home = academic_shell(lang,"Home",f'<h1>Latest Manuscripts</h1><p style="color:var(--ac-ink-muted);font-size:0.9em">{t(lang,"footer_disclosure_academic")}</p><ul class="ac-list">{ms_items}</ul>',"",other)
        (PUBLIC/(prefix if prefix else ".")/"index.html").write_text(home,encoding="utf-8")
        # About/Workshop/Papers
        for slug, title_key, body_md in [("about","nav_about",f"## {t(lang,'nav_about')}\n\nB.A.I.T. is a community fictional manuscript workshop.\n\n{t(lang,'footer_disclosure_academic')}"),("workshop","nav_workshop",f"## {t(lang,'nav_workshop')}\n\n1. Fork → Create → Submit PR → Community screening → Archive.\n\n**Community screening is not real peer review.**"),("papers","nav_papers",f"## {t(lang,'nav_papers')}\n\n<ul class=\"ac-list\">{ms_items}</ul>")]:
            (PUBLIC/prefix/slug).mkdir(parents=True,exist_ok=True)
            (PUBLIC/prefix/slug/"index.html").write_text(academic_shell(lang,t(lang,title_key),md2html(body_md),"",other),encoding="utf-8")
        # Archive home
        seen2 = set(); ai = ""
        for ms in reversed(ms_index):
            if ms["dio"] in seen2: continue; seen2.add(ms["dio"])
            ai += f'- [{ms["dio"]} — {ms["title"]}]({ms["archive_url"]}) `F-2 STABLE FISSURE`\n'
        (PUBLIC/prefix/"archive").mkdir(parents=True,exist_ok=True)
        (PUBLIC/prefix/"archive"/"index.html").write_text(archive_shell(lang,"Archive Home",md2html(f"## R.E.E.F. Archive\n\n> {t(lang,'footer_disclosure_archive')}\n\n### Available Records\n{ai}\n\n→ [Terminal](/terminal/)"),"",other),encoding="utf-8")
        for sub in ["cosmos","records","wiki"]:
            (PUBLIC/prefix/"archive"/sub).mkdir(parents=True,exist_ok=True)
            (PUBLIC/prefix/"archive"/sub/"index.html").write_text(archive_shell(lang,sub.title(),md2html(f"## {sub.title()}\n\n*Under construction.*"),"",other),encoding="utf-8")

    # Terminal
    (PUBLIC/"terminal").mkdir(exist_ok=True)
    (PUBLIC/"terminal"/"index.html").write_text("""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Terminal — B.A.I.T.</title><link rel="stylesheet" href="/static/css/theme.css"><link rel="stylesheet" href="/static/css/terminal.css"></head><body class="archive" style="background:#08080f"><div class="ar-topbar"><span>R.E.E.F. TERMINAL // ANONYMOUS</span><span><a href="/archive/">← Archive</a></span></div><main class="terminal-wrapper"><div id="terminal"></div></main><script src="/static/js/terminal.js"></script></body></html>""",encoding="utf-8")

    # Policies
    for src, slug in {"DISCLAIMER.md":"disclaimer","CODE_OF_CONDUCT.md":"code-of-conduct","CONTRIBUTING.md":"contributing","TAKEDOWN.md":"takedown","PRIVACY.md":"privacy"}.items():
        p = POLICIES/src
        if not p.exists(): continue
        _, body = parse_fm(p.read_text(encoding="utf-8"))
        (PUBLIC/"policies"/slug).mkdir(parents=True,exist_ok=True)
        (PUBLIC/"policies"/slug/"index.html").write_text(academic_shell("en",src.replace("_"," ").replace(".md","").title(),md2html(body)),encoding="utf-8")

    print(f"Built {len(ms_index)} manuscript(s)")
    for ms in ms_index: print(f"  [{ms['lang']}] {ms['dio']} → {ms['academic_url']}")

if __name__=="__main__": build()
