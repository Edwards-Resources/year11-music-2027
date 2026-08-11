#!/usr/bin/env python3
"""Build the Year 11 Music 1 teaching site.

Reads data/, writes docs/. Standard library only, on purpose: no package
manager, no lockfile, nothing that needs updating in years when nobody is
looking (see PRODUCT.md, Stack).

    python3 build.py

Every page is generated. Never edit anything in docs/ by hand; it gets
overwritten.
"""

import html
import json
import os
import shutil
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "docs")
ASSETS = os.path.join(ROOT, "assets")


def load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as f:
        return json.load(f)


def e(s):
    return html.escape(str(s), quote=True)


def write(path_parts, markup):
    path = os.path.join(OUT, *path_parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(markup)


def split_headline(title):
    """Two Anton lines, second inverted. A fixed rendition rule (DIRECTION.md
    FORM), not a state marker: every headline splits this way regardless of
    what the lesson is about."""
    words = title.split(" ")
    if len(words) < 2:
        return title, ""
    target = len(title) * 0.52
    line1, total = [], 0
    for i, w in enumerate(words):
        if total >= target and line1:
            break
        line1.append(w)
        total += len(w) + 1
    line2 = words[len(line1):]
    if not line2:
        line2 = [line1.pop()] if len(line1) > 1 else []
    return " ".join(line1), " ".join(line2)


# --------------------------------------------------------------- page shell


def layout(site, title, body, crumbs=None, description="", nav_active=None, body_attrs=""):
    base = site["base"]
    crumbs = crumbs or []
    robots = '<meta name="robots" content="noindex, nofollow">' if site.get("noindex") else ""

    nav_items = [
        ("This week", "/", "home"),
        ("Term 1", "/term1/", "term1"),
        ("Term 2", "/term2/", "term2"),
        ("Term 3", "/term3/", "term3"),
        ("The Works", "/the-works/", "works"),
    ]
    links = []
    for label, href, key in nav_items:
        cur = ' aria-current="page"' if key == nav_active else ""
        links.append(f'<a href="{base}{href}"{cur}>{e(label)}</a>')
    canvas_url = site.get("canvasUrl")
    if canvas_url:
        links.append(f'<a href="{e(canvas_url)}">Canvas</a>')
    else:
        links.append('<span class="on" style="opacity:.4" title="Canvas course not yet built">Canvas</span>')
    nav = f'<nav class="site-nav" aria-label="Site">{"".join(links)}</nav>'

    trail = ""
    if crumbs:
        parts = []
        for i, (label, href) in enumerate(crumbs):
            if href and i < len(crumbs) - 1:
                parts.append(f'<li><a href="{base}{href}">{e(label)}</a></li>')
            else:
                parts.append(f'<li><span aria-current="page">{e(label)}</span></li>')
        trail = f'<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>{"".join(parts)}</ol></div></nav>'

    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{robots}
<title>{e(title) if title == site['title'] else e(title) + ' | ' + e(site['title'])}</title>
<meta name="description" content="{e(description)}">
<link rel="stylesheet" href="{base}/assets/site.css">
</head>
<body{body_attrs}>
<!--
THESIS: The current lesson is the headliner on a lineup sheet, at a scale nothing else competes with. It refuses the course-site default of equal-weight cards in a grid, where this week and week nine look identical.
OWN-WORLD: One saturated oxblood ground (#7E1428) edge to edge, one bone ink (#F0E9DE), no panels, no cards, no second accent. Anton for all billing, Literata for reading, Roboto Mono for catalogue numbers. State is carried by inversion: the active thing is a bone block with oxblood type. Rules are 1.5px bone at 40% opacity.
STORY: A student sees what this lesson is, what to listen to, and what they must be able to do by the end of it, then sees the twenty works of the year with the current one lit.
FIRST VIEWPORT: Thin masthead, then the kicker line (term, week, lesson n of 50), then the lesson title in Anton at 118px over two lines with the second line inverted. Below: listening, learning intention, outcomes in three columns. Then this week's numbered activities. Then last time / next up / lessons until the examination. The twenty works justified into a block at the foot.
FORM: The Liner Notes, rendition "The Billing". World pinned by the user, not rolled. Roll key b1bd6caf assigned grounded index 3; the user's pin beats the roll, and the roll's festival-lineup challenger informed the rendition.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md
-->
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <div class="wrap">
    <a class="wordmark" href="{base}/">{e(site['course']['wordmark'])}<span class="div">/</span>{e(site['course']['year'])}</a>
    {nav}
  </div>
</header>
{trail}
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <p>{e(site['course']['canvasNote'])}</p>
    <p>Updated {date.today().strftime('%-d %B %Y')}</p>
  </div>
</footer>
<script src="{base}/assets/site.js" defer></script>
</body>
</html>
"""


# ------------------------------------------------------------------ blocks


def block_html(block):
    t = block["type"]
    if t == "table":
        head = "".join(f"<th>{e(c)}</th>" for c in block["columns"])
        rows = "".join(
            "<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in block["rows"]
        )
        return f'<section class="blk"><h2 class="tab">{e(block["title"])}</h2><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></section>'
    if t == "prose":
        return f'<section class="blk"><h2 class="tab">{e(block["title"])}</h2><p>{e(block["text"])}</p></section>'
    if t == "note":
        return f'<section class="blk"><h2 class="tab">{e(block["title"])}</h2><p class="example">{e(block["text"])}</p></section>'
    if t == "media":
        if block.get("embed"):
            brief = f'<p class="media-brief">{e(block["brief"])}</p>' if block.get("brief") else ""
            return (
                '<section class="blk"><h2 class="tab">Listen</h2>'
                f'<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{e(block["embed"])}" '
                'title="Listening example" loading="lazy" allowfullscreen '
                'allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture"></iframe></div>'
                f"{brief}</section>"
            )
        return (
            '<section class="blk blk-empty"><h2 class="tab">Listen</h2>'
            f'<p class="empty-mark">{e(block.get("brief") or "Not sourced yet.")}</p></section>'
        )
    return ""


# ------------------------------------------------------------------- tail


def works_tail(site, course, works, current_no=None):
    parts = []
    for w in works:
        label = f'{e(w["short"])}'
        cls = ' class="now"' if w["no"] == current_no else ""
        if w.get("lesson"):
            href = lesson_href(site, course, term_of(course, w["lesson"]), w["lesson"])
            item = f'<a href="{href}"><span{cls}>{label}</span></a>'
        else:
            item = f"<span{cls}>{label}</span>"
        parts.append(item)
    body = ' <span class="div">/</span> '.join(parts)
    return f"""<section class="tail" aria-label="The twenty works of the year">
  <span class="tailk">The twenty works of the year, in the order we meet them</span>
  <div class="tailblock">{body}</div>
</section>"""


def term_of(course, lesson_no):
    for t in course["terms_loaded"]:
        start = t.get("lessonNumberStart", t["lessons"][0]["number"] if t["lessons"] else 1)
        count = len(t["lessons"])
        if start <= lesson_no < start + count:
            return t
    return course["terms_loaded"][0]


def lesson_href(site, course, term, lesson_no):
    return f"{site['base']}/{term['id']}/{lesson_no}/"


# ------------------------------------------------------------------- bill


def bill_body(site, course, term, lesson, works, current_no):
    l1, l2 = split_headline(lesson["title"])
    head_html = f'<span class="l1">{e(l1)}</span>'
    if l2:
        head_html += f'<span class="l2"><span class="inv">{e(l2)}</span></span>'

    listening = ""
    if lesson.get("listening"):
        w = next(wk for wk in works if wk["no"] == lesson["listening"])
        note = lesson.get("listeningNote") or ""
        listening = (
            '<div><span class="k catword">Listening</span>'
            f'<span class="v">{e(w["short"])}</span>'
            f'<span class="k catword" style="margin-top:.4rem;display:block">'
            f'M {w["no"]:02d} · {e(w["composer"])}</span>'
            + (f'<p>{e(note)}</p>' if note else "")
            + "</div>"
        )
    else:
        note = lesson.get("listeningNote") or "Teacher's choice, confirmed in class."
        listening = (
            '<div><span class="k catword">Listening</span>'
            f'<span class="v" style="font-size:1.1rem">Not on the register</span>'
            f"<p>{e(note)}</p></div>"
        )

    outcomes_v = "<br>".join(e(c) for c in lesson["outcomes"])
    sub = f"""<div class="sub">
      {listening}
      <div><span class="k catword">What you will be able to do</span><p>{e(lesson['whatYouWillDo'])}</p></div>
      <div><span class="k catword">Outcomes</span><span class="v" style="font-size:1.3rem">{outcomes_v}</span></div>
    </div>"""

    steps_html = ""
    if lesson["steps"]:
        items = "".join(
            f'<div class="st"><span class="n">{i+1:02d}</span><p>{e(s)}</p></div>'
            for i, s in enumerate(lesson["steps"])
        )
        steps_html = f"""<div class="steps">
      <span class="k catword">In class this fortnight</span>
      <div class="stepgrid">{items}</div>
    </div>"""

    all_lessons = term["lessons"]
    idx = next((i for i, l in enumerate(all_lessons) if l["number"] == lesson["number"]), 0)
    prev_l = all_lessons[idx - 1] if idx else None
    next_l = all_lessons[idx + 1] if idx + 1 < len(all_lessons) else None

    last_sp = '<div class="sp"><span class="t">First lesson</span><span class="m">The course starts here.</span></div>'
    if prev_l:
        last_sp = (
            f'<div class="sp"><a href="{lesson_href(site, course, term, prev_l["number"])}">'
            f'<span class="t">Last time</span><span class="m">L{prev_l["number"]} · {e(prev_l["title"])}</span></a></div>'
        )
    next_sp = '<div class="sp"><span class="t">Coming up</span><span class="m">Term 2 begins.</span></div>'
    if next_l and next_l.get("blocks") is not None:
        next_sp = (
            f'<div class="sp on"><a href="{lesson_href(site, course, term, next_l["number"])}">'
            f'<span class="t">Next up</span><span class="m">L{next_l["number"]} · {e(next_l["title"])}</span></a></div>'
        )
    elif next_l:
        next_sp = f'<div class="sp on"><span class="t">Next up</span><span class="m">L{next_l["number"]} · {e(next_l["title"])} (content pending)</span></div>'

    exam_sp = f'<div class="sp"><span class="t">{e(term["assessment"]["name"])}</span><span class="m">{e(term["assessment"]["when"])}</span></div>'

    support = f"""<div class="support">
      {last_sp}
      {next_sp}
      {exam_sp}
    </div>"""

    kick = f"""<div class="kick">
      <span class="catword">{e(term["name"].split(": ")[0])} · {e(lesson["week"])} · Lesson {lesson["number"]} of {course["totalLessons"]}</span>
      <span class="catword">{e(term["focusArea"])}</span>
    </div>"""

    tail = works_tail(site, course, works, current_no)

    return f"""<div class="bill">
  {kick}
  <div class="head">{head_html}</div>
  {sub}
  {steps_html}
  {support}
</div>
{tail}"""


def build_lesson(site, course, term, lesson, works):
    body_top = bill_body(site, course, term, lesson, works, lesson.get("listening"))

    crit = ""
    if lesson["criteria"]:
        items = "".join(
            f'<li><input type="checkbox" id="crit-{i}"><label for="crit-{i}">{e(c)}</label></li>'
            for i, c in enumerate(lesson["criteria"])
        )
        crit = f"""<section class="blk"><h2 class="tab">Success criteria</h2>
    <ul class="crit-list">{items}</ul></section>"""

    blocks = "".join(block_html(b) for b in lesson["blocks"])

    all_lessons = term["lessons"]
    idx = next((i for i, l in enumerate(all_lessons) if l["number"] == lesson["number"]), 0)
    prev_l = all_lessons[idx - 1] if idx else None
    next_l = all_lessons[idx + 1] if idx + 1 < len(all_lessons) else None
    nav = []
    if prev_l:
        nav.append(
            f'<a class="pn pn-prev" href="{lesson_href(site, course, term, prev_l["number"])}">'
            f'<span>Previous</span><strong>{e(prev_l["title"])}</strong></a>'
        )
    if next_l:
        nav.append(
            f'<a class="pn pn-next" href="{lesson_href(site, course, term, next_l["number"])}">'
            f'<span>Next</span><strong>{e(next_l["title"])}</strong></a>'
        )

    body = f"""<div class="wrap">
{body_top}
{crit}
{blocks}
<nav class="prevnext" aria-label="Lessons">{''.join(nav)}</nav>
</div>"""

    crumbs = [("Home", "/"), (term["name"], f"/{term['id']}/"), (f"Lesson {lesson['number']}", None)]
    key = f"{term['id']}-{lesson['number']}"
    return layout(
        site, f"Lesson {lesson['number']}: {lesson['title']}", body, crumbs,
        lesson["intention"], nav_active=term["id"], body_attrs=f' data-lesson-key="{e(key)}"',
    )


def build_home(site, course, term, lesson, works):
    body_top = bill_body(site, course, term, lesson, works, lesson.get("listening"))
    permalink = (
        f'<p style="margin-top:1rem"><a href="{lesson_href(site, course, term, lesson["number"])}">'
        f"This is Lesson {lesson['number']} of {course['totalLessons']} &rarr; its own page, criteria and notes</a></p>"
    )
    body = f'<div class="wrap">{body_top}{permalink}</div>'
    return layout(site, site["course"]["name"], body, [], "Where the class is up to, lesson by lesson.", nav_active="home")


def build_term(site, course, term):
    rows = []
    for l in term["lessons"]:
        built = "blocks" in l
        if built:
            rows.append(
                f'<a class="lrow" href="{lesson_href(site, course, term, l["number"])}">'
                f'<span class="no">L{l["number"]}</span>'
                f'<span class="ttl">{e(l["title"])}</span>'
                f'<span class="wk">{e(l["week"])}</span></a>'
            )
        else:
            rows.append(
                f'<div class="lrow missing">'
                f'<span class="no">L{l["number"]}</span>'
                f'<span class="ttl">{e(l["title"])} <span class="catword">(not yet on the site)</span></span>'
                f'<span class="wk">{e(l["week"])}</span></div>'
            )
    a = term["assessment"]
    body = f"""<div class="wrap">
  <div class="term-head">
    <h1>{e(term['name'])}</h1>
    <p>{e(term['focusArea'])}. {e(a['name'])}, {e(a['when'])}.</p>
  </div>
  <ol class="lesson-rows">{''.join(f"<li>{r}</li>" for r in rows)}</ol>
</div>"""
    return layout(site, term["name"], body, [("Home", "/"), (term["name"], None)],
                  f"{term['name']}, lesson by lesson.", nav_active=term["id"])


def build_works(site, course, works, current_no):
    rows = []
    for w in works:
        cls = " on" if w["no"] == current_no else ""
        cx = e(w["category"].replace("Music of ", "").replace("Music of the ", ""))
        if w.get("lesson"):
            href = lesson_href(site, course, term_of(course, w["lesson"]), w["lesson"])
            wk = f"{w['term']}.{w['week']}"
            rows.append(
                f'<a class="wk-row{cls}" href="{href}">'
                f'<span class="no catword">M {w["no"]:02d}</span>'
                f'<span class="ttl"><b>{e(w["title"])}</b> {e(w["composer"])}</span>'
                f'<span class="cx catword">{cx}</span>'
                f'<span class="w catword">{w["term"]}.{w["week"]}</span></a>'
            )
        else:
            rows.append(
                f'<div class="wk-row{cls}">'
                f'<span class="no catword">M {w["no"]:02d}</span>'
                f'<span class="ttl"><b>{e(w["title"])}</b> {e(w["composer"])}</span>'
                f'<span class="cx catword">{cx}</span>'
                f'<span class="w catword">{w["term"]}.{w["week"]}</span></div>'
            )
    current_lesson = None
    for t in course["terms_loaded"]:
        for l in t["lessons"]:
            if l["number"] == current_no:
                current_lesson = (t, l)
    now_card = ""
    if current_lesson:
        t, l = current_lesson
        now_card = f"""<div class="nowcard">
      <span class="k catword">We are up to &nbsp;/&nbsp; {e(t['name'].split(': ')[0])}, {e(l['week'])}</span>
      <span class="t">{e(l['title'])}</span>
    </div>"""

    counts = "".join(
        f'<div class="fc{" on" if t["id"] == (current_lesson[0]["id"] if current_lesson else "") else ""}">'
        f'<span class="fk">{e(t["name"].split(": ")[0])} · {len(t["lessons"])} lessons</span>'
        f'<span class="ft">{e(t["focusArea"])}</span></div>'
        for t in course["terms_loaded"]
    )

    body = f"""<div class="wrap">
  <div class="catband">
    <div class="catmain">
      <h1><small>Year 11 &nbsp;·&nbsp; {e(course['year'])} &nbsp;·&nbsp; The catalogue</small>Twenty works,<br>one year</h1>
      {now_card}
    </div>
  </div>
  <div class="chead">
    <h2>The works we study</h2>
    <div class="catword">Catalogue · ordered by the week it is taught</div>
  </div>
  <div class="worklist">{''.join(rows)}</div>
  <div class="catfoot">{counts}</div>
</div>"""
    return layout(site, "The Works", body, [("Home", "/"), ("The Works", None)],
                  "The twenty works studied across Year 11 Music 1, in the order they are taught.",
                  nav_active="works")


# -------------------------------------------------------------------- main


def main():
    site = load("site.json")
    course = load("course", "course.json")
    works = load("course", "works.json")
    term1 = load("course", "term1", "term.json")
    term2 = load("course", "term2", "term.json")
    term3 = load("course", "term3", "term.json")
    course["terms_loaded"] = [term1, term2, term3]
    site["course"] = course

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    pages = 0

    # Home: the current position. No live 2027 position exists yet, so this
    # defaults to Lesson 1 of Term 1, the honest "day one" state, until a
    # debrief updates it once teaching starts (PRODUCT.md, Live position).
    current_lesson = term1["lessons"][0]
    write(["index.html"], build_home(site, course, term1, current_lesson, works))
    pages += 1

    for term in (term1, term2, term3):
        write([term["id"], "index.html"], build_term(site, course, term))
        pages += 1
        for lesson in term["lessons"]:
            if "blocks" not in lesson:
                continue  # Term 2/3 lessons are stubs: title and week only, no page yet.
            write(
                [term["id"], str(lesson["number"]), "index.html"],
                build_lesson(site, course, term, lesson, works),
            )
            pages += 1

    write(["the-works", "index.html"], build_works(site, course, works, current_lesson["number"]))
    pages += 1

    shutil.copytree(ASSETS, os.path.join(OUT, "assets"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    unbuilt = sum(1 for t in (term2, term3) for l in t["lessons"])
    unlinked_works = sum(1 for w in works if not w.get("lesson"))
    print(f"built {pages} pages into docs/")
    print(f"  {unbuilt} lesson slots in Term 2/3 are titles only, no page yet")
    print(f"  {unlinked_works} of {len(works)} works have no lesson page to link to yet")


if __name__ == "__main__":
    main()
