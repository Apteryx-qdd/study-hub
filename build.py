# -*- coding: utf-8 -*-
"""Build the study-material site from site_data.json.

Usage:
    python build.py            # regenerate index, subject pages, data.js, doc top-bars
Adding material:
    1. drop the authored doc HTML into docs/<subject-code>/<file>
    2. add an entry under that subject in site_data.json
    3. run this script
"""
import json, os, re, html, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
CSS_VER = "3"


def esc(s):
    return html.escape(str(s), quote=True)


def load():
    with open(os.path.join(BASE, "site_data.json"), encoding="utf-8") as f:
        return json.load(f)


def doc_url(sub, doc, prefix=""):
    return f"{prefix}docs/{sub['code']}/{doc['file']}"


def inject_docbar(path, sub, doc):
    """Insert (or replace) a slim breadcrumb bar at the top of a doc page."""
    h = open(path, encoding="utf-8").read()
    bar = f'''<div class="docbar" id="docbar"><div class="docbar-in">
<a href="../../index.html">← 资料库</a><span style="opacity:.45">/</span>
<a href="../../subjects/{sub["code"]}.html">{esc(sub["name"])}</a><span style="opacity:.45">/</span>
<b>{esc(doc["title"])}</b>
<span class="spacer"></span>
<a href="#top" onclick="window.scrollTo({{top:0,behavior:'smooth'}});return false;">↑ 顶部</a>
{f'<a class="pdfbtn" href="../../assets/pdf/{esc(doc["pdf"])}" target="_blank" rel="noopener">打开 PDF</a>' if doc.get("pdf") else ""}
</div></div>
<style>
.docbar{{background:#0e2b44;color:#cfe0ef;font-size:13.2px;line-height:1.6}}
.docbar-in{{max-width:1080px;margin:0 auto;padding:8px 22px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.docbar a{{color:#a9c6de;text-decoration:none}}
.docbar a:hover{{color:#fff;text-decoration:underline}}
.docbar b{{color:#fff;font-weight:600}}
.docbar .spacer{{flex:1;min-width:8px}}
.docbar .pdfbtn{{border:1px solid rgba(255,255,255,.38);border-radius:999px;padding:1px 12px;color:#fff}}
.docbar .pdfbtn:hover{{background:rgba(255,255,255,.14);text-decoration:none}}
@media print{{.docbar{{display:none}}}}
</style>
'''
    # remove an existing injected bar (idempotent rebuild)
    h = re.sub(r'<div class="docbar" id="docbar">.*?</style>\s*', '', h, flags=re.S)
    # ensure a #top anchor exists
    if 'id="top"' not in h:
        h = h.replace("<body>", '<body id="top">', 1)
    h = h.replace("<body>", "<body>", 1)
    # insert right after <body ...>
    h = re.sub(r'(<body[^>]*>)', r'\1\n' + bar.replace('\\', '\\\\'), h, count=1)
    open(path, "w", encoding="utf-8").write(h)


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
"""

FOOT = """<footer><div class="wrap">
  <div>复习资料库 · 按科目分类 · 离线可用（直接双击 index.html 打开）</div>
  <div style="margin-top:6px">数据来源：{src} ｜ 最近更新：{date}</div>
</div></footer>
"""


def build_index(data):
    s = data["site"]
    subs = data["subjects"]
    n_docs = sum(len(x["docs"]) for x in subs)
    cards = []
    for sub in subs:
        tags = "".join(f'<span class="chip soft">{esc(t)}</span>' for d in sub["docs"] for t in d.get("tags", [])[:1])
        cards.append(f'''<a class="subject" href="subjects/{sub["code"]}.html" style="--sc:{sub.get("color", "#2f6f9f")}">
  <div class="code">{esc(sub.get("course",""))}</div>
  <h3>{esc(sub["name"])}</h3>
  <div class="en">{esc(sub.get("en",""))}</div>
  <div class="count">{len(sub["docs"])} 份资料 · {esc(sub.get("term",""))}</div>
  <div class="tags">{tags}</div>
</a>''')

    docs = []
    for sub in subs:
        for d in sub["docs"]:
            tags = "".join(f'<span class="chip">{esc(t)}</span>' for t in d.get("tags", []))
            kw = esc((d["title"] + " " + d.get("desc", "") + " " + d.get("keywords", "") + " " + sub["name"]).lower())
            pdf = f'<a class="btn" href="assets/pdf/{esc(d["pdf"])}" target="_blank" rel="noopener">PDF</a>' if d.get("pdf") else ""
            full = f'<a class="btn" href="docs/{esc(sub["code"])}/{esc(d["full"])}">完整单页</a>' if d.get("full") else ""
            docs.append(f'''<div class="card doc-card" data-kw="{kw}" style="border-left-color:{sub.get("color","#2f6f9f")}">
  <h3><a href="{doc_url(sub, d)}">{esc(d["title"])}</a></h3>
  <div class="meta"><span class="cat" style="background:#eaf3fa;color:{sub.get("color","#2f6f9f")}">{esc(sub["name"])}</span>
    <span>{esc(d.get("date",""))}</span>{f'<span>{d.get("pages","")} 页</span>' if d.get("pages") else ""}</div>
  <div class="desc">{esc(d.get("desc",""))}</div>
  <div class="meta">{tags}</div>
  <div class="actions"><a class="btn primary" href="{doc_url(sub, d)}">分节阅读</a>{full}{pdf}</div>
</div>''')

    body = f'''<header class="hero"><div class="wrap">
  <div class="eyebrow">Study Hub</div>
  <h1>{esc(s["name"])}</h1>
  <p>{esc(s["subtitle"])}</p>
  <div class="stats">
    <div class="stat"><b>{len(subs)}</b>个科目</div>
    <div class="stat"><b>{n_docs}</b>份资料</div>
    <div class="stat"><b>{len([1 for x in subs for d in x["docs"] if d.get("pdf")])}</b>份 PDF</div>
    <div class="stat">更新 {esc(s.get("updated",""))}</div>
  </div>
</div></header>

<main class="wrap">
  <div class="searchbar">
    <input id="q" type="search" placeholder="搜索：科目 / 标题 / 关键词，例如“逆矩阵”“子空间”“模拟卷”">
    <span class="hint" id="hint"></span>
  </div>

  <h2>按科目</h2>
  <p class="lead">每个科目下是一组按统一模板生成的材料；点进去可以看范围、资料清单和阅读入口。</p>
  <div class="grid">{"".join(cards)}</div>

  <h2>全部资料</h2>
  <p class="lead">按时间倒序；用上面的搜索框可以过滤。</p>
  <div class="grid" id="doclist">{"".join(docs)}</div>

  <details>
    <summary>这个站怎么用 / 怎么加新科目</summary>
    <ul>
      <li><b>离线使用</b>：整个 <code>site/</code> 文件夹拷到手机或电脑，双击 <code>index.html</code> 即可；不需要联网、不需要服务器。</li>
      <li><b>分享</b>：把文件夹压缩成 zip 发出去；或整体上传到任意静态托管（GitHub Pages / Netlify / 校内空间）。</li>
      <li><b>新增资料</b>：把新材料的 PDF/讲义交给我 → 我按同一模板生成文档页 → 在 <code>site_data.json</code> 里加一条记录 → 运行 <code>build.py</code>，首页与科目页自动更新。</li>
      <li><b>新增科目</b>：在 <code>site_data.json</code> 的 <code>subjects</code> 里加一个对象（名称、课程号、颜色、考试范围），再放文档即可。</li>
    </ul>
  </details>
</main>
'''

    body += FOOT.format(src="site_data.json", date=s.get("updated", ""))
    body += """<script>
(function(){
  var q = document.getElementById('q'), hint = document.getElementById('hint');
  var cards = [].slice.call(document.querySelectorAll('.doc-card'));
  function run(){
    var v = (q.value || '').trim().toLowerCase();
    var n = 0;
    cards.forEach(function(c){
      var hit = !v || (c.getAttribute('data-kw') || '').indexOf(v) >= 0;
      c.style.display = hit ? '' : 'none';
      if (hit) n++;
    });
    hint.textContent = v ? ('匹配 ' + n + ' 份') : ('共 ' + cards.length + ' 份');
  }
  q.addEventListener('input', run);
  run();
})();
</script>
</body>
</html>
"""
    write(os.path.join(BASE, "index.html"),
          HEAD.format(title="复习资料库 · Study Hub", css="assets/site.css") + body)


def build_subject(sub):
    color = sub.get("color", "#2f6f9f")
    scope = "".join(f"<li>{esc(x)}</li>" for x in sub.get("scope", []))
    excl = "、".join(sub.get("exclude", [])) or "—"
    cards = []
    for d in sub["docs"]:
        tags = "".join(f'<span class="chip">{esc(t)}</span>' for t in d.get("tags", []))
        pdf = f'<a class="btn" href="../assets/pdf/{esc(d["pdf"])}" target="_blank" rel="noopener">PDF</a>' if d.get("pdf") else ""
        full = f'<a class="btn" href="../docs/{esc(sub["code"])}/{esc(d["full"])}">完整单页</a>' if d.get("full") else ""
        cards.append(f'''<div class="card" style="border-left-color:{color}">
  <h3><a href="../docs/{sub["code"]}/{d["file"]}">{esc(d["title"])}</a></h3>
  <div class="meta"><span>{esc(d.get("date",""))}</span>{f'<span>{d.get("pages","")} 页</span>' if d.get("pages") else ""}</div>
  <div class="desc">{esc(d.get("desc",""))}</div>
  <div class="meta">{tags}</div>
  <div class="actions"><a class="btn primary" href="../docs/{sub["code"]}/{d["file"]}">分节阅读</a>{full}{pdf}</div>
</div>''')

    body = f'''<header class="subhero"><div class="wrap">
  <div class="crumb" style="color:rgba(255,255,255,.75)"><a href="../index.html" style="color:rgba(255,255,255,.85)">资料库</a> <span style="opacity:.5">/</span> {esc(sub["name"])}</div>
  <h1>{esc(sub["name"])}</h1>
  <div class="en">{esc(sub.get("en",""))} · {esc(sub.get("course",""))} · {esc(sub.get("term",""))}</div>
  <div class="en" style="margin-top:6px">{esc(sub.get("teacher",""))}</div>
</div></header>

<main class="wrap">
  <h2>考试范围</h2>
  <div class="panel">
    <ul>{scope}</ul>
    <p style="margin-top:10px;font-size:14px;color:#5d6b7a"><b>不考：</b>{esc(excl)}</p>
    {f'<p style="margin-top:6px;font-size:14px;color:#5d6b7a"><b>备注：</b>{esc(sub.get("notes",""))}</p>' if sub.get("notes") else ""}
  </div>

  <h2>资料（{len(sub["docs"])}）</h2>
  <p class="lead">同一科目下的材料共用一套模板：先看“考点版”抓范围，再用“提纲”补细节，最后做模拟卷。</p>
  <div class="grid">{"".join(cards)}</div>
</main>
'''
    body += FOOT.format(src="site_data.json", date=load()["site"].get("updated", ""))
    body += "</body>\n</html>\n"
    write(os.path.join(BASE, "subjects", sub["code"] + ".html"),
          HEAD.format(title=f'{sub["name"]} · 复习资料库', css="../assets/site.css") + body)


def build_data_js(data):
    js = "window.SITE_DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n"
    write(os.path.join(BASE, "assets", "data.js"), js)


def main():
    data = load()
    build_index(data)
    build_data_js(data)
    for sub in data["subjects"]:
        build_subject(sub)
        for d in sub["docs"]:
            # chunked landing pages already carry their own top bar
            if "/" in d.get("file", ""):
                continue
            p = os.path.join(BASE, "docs", sub["code"], d["file"])
            if os.path.exists(p):
                inject_docbar(p, sub, d)
            else:
                print("!! missing doc:", p)
            if d.get("full"):
                fp = os.path.join(BASE, "docs", sub["code"], d["full"])
                if os.path.exists(fp):
                    inject_docbar(fp, sub, d)
    print("built:", len(data["subjects"]), "subjects,",
          sum(len(s["docs"]) for s in data["subjects"]), "docs")


if __name__ == "__main__":
    main()
