#!/usr/bin/env python3
"""Build the Year 11 Music 1 teaching site.

Reads data/, writes docs/. Standard library only, on purpose: no package
manager, no lockfile, nothing that needs updating in years when nobody is
looking (see PRODUCT.md, Stack).

    python3 build.py

Every page is generated. Never edit anything in docs/ by hand; it gets
overwritten.

World: On Air. The approved comps are .impeccable/mocks/comp-f-stationfront.html
(home and lesson pages) and comp-d-schedule.html (term hub pages). The comp read
as a design system lives in .impeccable/surfaces/docs-index-html.md.
"""

import html
import json
import os
import re
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
    # The source data mixes straight and curly apostrophes. Curl only the ones
    # sitting inside a word, so contractions and possessives are typeset properly
    # and a straight quotation mark round a word is left alone.
    return re.sub(r"(?<=\w)&#x27;(?=\w)", "’", html.escape(str(s), quote=True))


def write(path_parts, markup):
    path = os.path.join(OUT, *path_parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(markup)


def first_week(text):
    """The first week number in a label like 'Weeks 2, 4, 8 & 10' or 'Term 1, Week 8'.
    Anchored on the word 'week' so 'Term 1' is not read as week 1. None if absent."""
    m = re.search(r"weeks?\s*(\d+)", str(text or ""), re.I)
    return int(m.group(1)) if m else None


DOT = '<span class="live onair-dot" aria-hidden="true"></span>'


def at_title(a):
    """'AT3: Music in Focus Examination' names its task; 'AT2' does not yet.
    The slot cell beside it already reads AT 2, so a bare repeat is no title."""
    name = a["name"]
    return name.split(": ", 1)[1] if ": " in name else "Assessment task"


# --------------------------------------------------------------- page shell


def masthead(site, nav_active):
    base = site["base"]
    items = [
        ("This week", "/", "home"),
        ("Term 1", "/term1/", "term1"),
        ("Term 2", "/term2/", "term2"),
        ("Term 3", "/term3/", "term3"),
        ("The Works", "/the-works/", "works"),
    ]
    links = []
    for label, href, key in items:
        cur = ' aria-current="page"' if key == nav_active else ""
        links.append(f'<a href="{base}{href}"{cur}>{e(label)}</a>')
    canvas_url = site.get("canvasUrl")
    if canvas_url:
        links.append(f'<a href="{e(canvas_url)}">Canvas</a>')
    else:
        links.append('<span class="off">Canvas <span class="vh">(course not yet built)</span></span>')
    course = site["course"]
    return f"""<header class="masthead">
  <a class="wordmark" href="{base}/">{e(course['wordmark'])}<span class="yr">{e(course['year'])}</span></a>
  <nav class="site-nav" aria-label="Site">{"".join(links)}</nav>
</header>"""


def archive(site, course, works, current_work):
    """The twenty works, on the foot of every page. The course's spine, always visible."""
    base = site["base"]
    chips = []
    for w in works:
        on = " on" if w["no"] == current_work else ""
        inner = f'<b>M{w["no"]:02d}</b><span class="t">{e(w["short"])}</span>'
        if w.get("lesson"):
            term = term_of(course, w["lesson"])
            href = f'{base}/{term["id"]}/{w["lesson"]}/'
            aria = ' aria-current="true"' if on else ""
            chips.append(f'<li><a class="chip{on}" href="{href}"{aria}>{inner}</a></li>')
        else:
            chips.append(f'<li><span class="chip{on}">{inner}</span></li>')
    return f"""<section class="arch" aria-labelledby="arch-h">
  <div class="archhead">
    <h2 class="tag-lg" id="arch-h">The archive &nbsp;/&nbsp; twenty works, every one of them a page</h2>
    <span class="tag muted">Ordered by the week we meet them</span>
  </div>
  <ol class="chips">{"".join(chips)}</ol>
</section>"""


def layout(site, title, body, description="", nav_active=None, strand="term1", current_work=None,
           course=None, works=None):
    base = site["base"]
    robots = '<meta name="robots" content="noindex, nofollow">' if site.get("noindex") else ""
    full_title = e(title) if title == site["title"] else e(title) + " | " + e(site["title"])
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{robots}
<title>{full_title}</title>
<meta name="description" content="{e(description)}">
<link rel="preload" href="{base}/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{base}/assets/site.css">
</head>
<body data-strand="{e(strand)}">
<!--
THESIS: The year is a music station's schedule and the class is what is on air right now. It refuses the course-site default of equal-weight lesson cards in a grid, where this week and week nine look identical, and it refuses the drenched display-type poster it replaces.
OWN-WORLD: Near-white paper (#FAFAF7), black ink (#101014), one flat strand colour per term (#3DDC97, #FFD23F, #FF6B6B) always carrying black ink. One family, Archivo variable, character from the width axis, never a second face. Square corners, no shadows, no gradients, two line weights. State is a filled strand field plus the words "On air" plus a live dot.
STORY: A student sees what is on air, what to listen to and what they must be able to do, never loses the whole term from the left rail, and reaches any of the twenty works from the archive at the foot of every page.
FIRST VIEWPORT: Masthead, then a 19rem rail holding every lesson of the term with the current one filled and AT1 in its real week, and beside it the ON AIR line, the lesson title, a listening / by-the-end / outcomes strip, then the lesson's real content in two columns. The archive band runs across the foot.
FORM: On Air, rendition "The Station Front". Candidate 5 of the grounded list, seed key 78a3d3a4, after one user re-roll steered "more fun and music inspired". Approved comp F with the term hub taken from comp D.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md
-->
<a class="skip" href="#main">Skip to content</a>
{masthead(site, nav_active)}
{body}
{archive(site, course, works, current_work)}
<footer class="foot">
  <p>{e(site['course']['canvasNote'])}</p>
  <p>Updated {date.today().strftime('%-d %B %Y')}</p>
</footer>
<script src="{base}/assets/site.js" defer></script>
</body>
</html>
"""


# ------------------------------------------------------------------ the rail


def rail_rows(site, course, term, current_no, reading_no):
    """Every lesson in the term, with the assessment sitting in its real week.
    Status wording is comp D's, folded into comp F's rail on Matthew's call.
    Two distinct states: `on` is where the class is up to, `aria-current` is the
    page you are reading. They are usually different lessons."""
    base = site["base"]
    a = term["assessment"]
    a_week = first_week(a.get("when"))
    rows, placed = [], False

    def at_row():
        bits = [b for b in (a.get("when"), a.get("weighting"), "in Canvas") if b]
        return (f'<li><span class="rl at"><span class="n">AT {term["id"][-1]}</span>'
                f'<span class="t">{e(at_title(a))}</span>'
                f'<span class="w">{e(" · ".join(bits))}</span></span></li>')

    for l in term["lessons"]:
        if not placed and a_week is not None and (first_week(l["week"]) or 0) >= a_week:
            rows.append(at_row())
            placed = True
        built = "blocks" in l
        if l["number"] == current_no:
            state, meta = "on", f'{DOT}On air · {e(l["week"])}'
        elif built and current_no is not None and l["number"] < current_no:
            state, meta = "done", e(l["week"])
        elif not built:
            state, meta = "stub", f'{e(l["week"])} · not yet on the site'
        else:
            state, meta = "", e(l["week"])
        inner = (f'<span class="n">L {l["number"]:02d}</span>'
                 f'<span class="t">{e(l["title"])}</span>'
                 f'<span class="w">{meta}</span>')
        if built:
            cur = ' aria-current="page"' if l["number"] == reading_no else ""
            rows.append(f'<li><a class="rl {state}" href="{base}/{term["id"]}/{l["number"]}/"{cur}>{inner}</a></li>')
        else:
            rows.append(f'<li><span class="rl {state}">{inner}</span></li>')
    if not placed:
        rows.append(at_row())
    return "".join(rows)


def rail(site, course, term, current_no, reading_no):
    base = site["base"]
    n = len(term["lessons"])
    strands = "".join(
        f'<div><i style="background:var(--s{i+1})"></i>Term {i+1} &nbsp;{e(t["focusArea"])}</div>'
        for i, t in enumerate(course["terms_loaded"])
    )
    return f"""<nav class="rail" aria-label="{e(term['name'])} schedule">
  <div class="railhead">
    <span class="tag muted">Strand {term['id'][-1]} &nbsp;·&nbsp; {n} lessons</span>
    <a href="{base}/{term['id']}/"><span class="t">{e(term['focusArea'])}</span></a>
  </div>
  <ul class="rlist">{rail_rows(site, course, term, current_no, reading_no)}</ul>
  <div class="railfoot">
    <span class="tag muted">The three strands</span>
    <div class="key">{strands}</div>
  </div>
</nav>"""


# ------------------------------------------------------------------ helpers


def term_of(course, lesson_no):
    for t in course["terms_loaded"]:
        start = t.get("lessonNumberStart", t["lessons"][0]["number"] if t["lessons"] else 1)
        if start <= lesson_no < start + len(t["lessons"]):
            return t
    return course["terms_loaded"][0]


# ------------------------------------------------------------------- blocks


def block_html(block):
    t = block["type"]
    title = e(block.get("title", ""))
    if t == "table":
        cols = block["columns"]
        head = "".join(f"<th>{e(c)}</th>" for c in cols)
        # data-label lets the phone stack each cell under its own column name
        # instead of hiding two columns off the side of a scroller.
        rows = "".join(
            "<tr>" + "".join(
                f'<td data-label="{e(cols[i]) if i < len(cols) else ""}">{e(c)}</td>'
                for i, c in enumerate(r)
            ) + "</tr>"
            for r in block["rows"]
        )
        return (f'<section class="sect"><h2>{title}</h2><div class="tw"><table>'
                f"<thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div></section>")
    if t == "prose":
        return f'<section class="sect"><h2>{title}</h2><p>{e(block["text"])}</p></section>'
    if t == "note":
        return f'<aside class="note"><span class="tag">{title}</span><p>{e(block["text"])}</p></aside>'
    if t == "media":
        if block.get("embed"):
            brief = f'<p class="pending">{e(block["brief"])}</p>' if block.get("brief") else ""
            return ('<section class="sect"><h2>Listen</h2>'
                    f'<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{e(block["embed"])}" '
                    'title="Listening example" loading="lazy" allowfullscreen '
                    'allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture"></iframe></div>'
                    f"{brief}</section>")
        return ('<section class="sect"><h2>Listen</h2>'
                f'<span class="pending">{e(block.get("brief") or "Not sourced yet.")}</span></section>')
    return ""


# --------------------------------------------------------------- the lesson


def lesson_main(site, course, term, lesson, works, is_home=False, current_no=None):
    base = site["base"]

    # Only the lesson the class is actually up to may say "On air". Every other
    # lesson page states its own position plainly.
    pos = f'{e(term["name"].split(": ")[0])} &nbsp;·&nbsp; {e(lesson["week"])} &nbsp;·&nbsp; Lesson {lesson["number"]} of {course["totalLessons"]}'
    if lesson["number"] == current_no:
        status = f'{DOT}On air &nbsp;·&nbsp; {pos}'
    elif current_no is not None and lesson["number"] < current_no:
        status = f'Aired &nbsp;·&nbsp; {pos}'
    else:
        status = f'Coming up &nbsp;·&nbsp; {pos}'

    listening = '<span class="tag muted">Now listening</span>'
    if lesson.get("listening"):
        w = next(wk for wk in works if wk["no"] == lesson["listening"])
        href = f'{base}/{term_of(course, w["lesson"])["id"]}/{w["lesson"]}/' if w.get("lesson") else None
        name = f'<a href="{href}">{e(w["short"])}</a>' if href else e(w["short"])
        listening += (f'<div class="work">{name}</div>'
                      f'<div class="by">{e(w["composer"])} &nbsp;·&nbsp; M {w["no"]:02d}</div>')
        if lesson.get("listeningNote"):
            listening += f'<p>{e(lesson["listeningNote"])}</p>'
    else:
        listening += ('<div class="work">Teacher&rsquo;s choice</div>'
                      f'<p>{e(lesson.get("listeningNote") or "Confirmed in class.")}</p>')

    outcomes = "<br>".join(e(c) for c in lesson["outcomes"])

    acts = ""
    if lesson["steps"]:
        items = "".join(f'<li><b>{i+1:02d}</b>{e(s)}</li>' for i, s in enumerate(lesson["steps"]))
        acts = f'<section class="sect"><h2>In class this fortnight</h2><ul class="acts">{items}</ul></section>'

    crit = ""
    if lesson["criteria"]:
        items = "".join(
            f'<li><input type="checkbox" id="c{i}"><label for="c{i}">{e(c)}</label></li>'
            for i, c in enumerate(lesson["criteria"])
        )
        crit = f'<section class="sect"><h2>Success criteria</h2><ul class="crit">{items}</ul></section>'

    # Notes go in the narrow column beside the activities; everything else runs wide.
    wide = "".join(block_html(b) for b in lesson["blocks"] if b["type"] != "note")
    notes = "".join(block_html(b) for b in lesson["blocks"] if b["type"] == "note")

    all_l = term["lessons"]
    idx = next((i for i, l in enumerate(all_l) if l["number"] == lesson["number"]), 0)
    prev_l = all_l[idx - 1] if idx else None
    next_l = all_l[idx + 1] if idx + 1 < len(all_l) else None
    nav = []
    if prev_l and "blocks" in prev_l:
        nav.append(f'<a class="pn" href="{base}/{term["id"]}/{prev_l["number"]}/">'
                   f'<span class="k">Last aired</span><span class="t">{e(prev_l["title"])}</span></a>')
    if next_l and "blocks" in next_l:
        nav.append(f'<a class="pn pn-next" href="{base}/{term["id"]}/{next_l["number"]}/">'
                   f'<span class="k">Next up</span><span class="t">{e(next_l["title"])}</span></a>')
    prevnext = f'<nav class="prevnext" aria-label="Lessons">{"".join(nav)}</nav>' if nav else ""

    permalink = ""
    if is_home:
        permalink = (f'<p class="permalink"><a href="{base}/{term["id"]}/{lesson["number"]}/">'
                     f'Open Lesson {lesson["number"]} in full</a></p>')

    return f"""<div class="main" id="main">
  <div class="lead">
    <p class="onair"><span class="tag-lg">{status}</span></p>
    <h1>{e(lesson['title'])}</h1>
  </div>
  <div class="strip">
    <div class="sc">{listening}</div>
    <div class="sc"><span class="tag muted">By the end you can</span><p>{e(lesson['whatYouWillDo'])}</p></div>
    <div class="sc"><span class="tag muted">Outcomes</span><div class="oc">{outcomes}</div></div>
  </div>
  <div class="two">
    <div>{wide}</div>
    <div>{acts}{crit}{notes}</div>
  </div>
  {permalink}
  {prevnext}
  <div class="mainfoot"></div>
</div>"""


def build_lesson(site, course, term, lesson, works, current_no, is_home=False):
    body = f"""<div class="split">
{rail(site, course, term, current_no, lesson["number"])}
{lesson_main(site, course, term, lesson, works, is_home, current_no)}
</div>"""
    title = site["course"]["name"] if is_home else f"Lesson {lesson['number']}: {lesson['title']}"
    desc = "What is on air this week." if is_home else lesson["intention"]
    return layout(site, title, body, desc, nav_active=("home" if is_home else term["id"]),
                  strand=term["id"], current_work=lesson.get("listening"),
                  course=course, works=works)


# ---------------------------------------------------------------- term hubs


def hub_band(site, course, term, current_no, works):
    """comp-d's opening band: the largest element on that surface, and the only
    thing on it that answers "what is on air". The strand fill is spent only on
    the term that is actually on air; a term that is not gets the same geometry
    on paper, or the fill would be teaching that a strand field means nothing."""
    base = site["base"]
    lessons = term["lessons"]
    first, last = lessons[0]["number"], lessons[-1]["number"]
    live = current_no is not None and first <= current_no <= last

    if live:
        l = next(x for x in lessons if x["number"] == current_no)
        kicker = (f'{DOT}On air &nbsp;·&nbsp; {e(term["name"].split(": ")[0])} &nbsp;·&nbsp; '
                  f'{e(l["week"])} &nbsp;·&nbsp; Lesson {l["number"]} of {course["totalLessons"]}')
    else:
        aired = current_no is not None and current_no > last
        l = lessons[-1] if aired else lessons[0]
        word = "Aired" if aired else "Coming up"
        kicker = (f'{word} &nbsp;·&nbsp; {e(term["name"].split(": ")[0])} &nbsp;·&nbsp; '
                  f'{e(term["focusArea"])} &nbsp;·&nbsp; Lessons {first} to {last}')

    title = e(l["title"])
    if "blocks" in l:
        title = f'<a href="{base}/{term["id"]}/{l["number"]}/">{title}</a>'

    aside = ""
    if live and l.get("listening"):
        w = next((x for x in works if x["no"] == l["listening"]), None)
        if w:
            aside = (f'<span class="tag">Now listening</span>'
                     f'<span class="ln">M {w["no"]:02d} &nbsp;{e(w["short"])}</span>'
                     f'<span class="lb">{e(w["composer"])}</span>')
    if not aside:
        a = term["assessment"]
        aside = (f'<span class="tag">Assessment</span>'
                 f'<span class="ln">{e(a["name"])}</span>'
                 f'<span class="lb">{e(a["when"])} &nbsp;·&nbsp; in Canvas</span>')

    return f"""<div class="hubband{' hb-live' if live else ''}">
    <div class="hb-main"><p class="tag-lg">{kicker}</p><p class="hb-t">{title}</p></div>
    <div class="hb-side">{aside}</div>
  </div>"""


def build_term(site, course, term, current_no, works):
    """comp-d-schedule.html: the on-air band, then the schedule grid."""
    base = site["base"]
    a = term["assessment"]
    a_week = first_week(a.get("when"))
    rows, placed = [], False

    def cell(cls, label, inner):
        # An empty cell stays genuinely empty, so the phone's stacked view can
        # drop it with :empty instead of printing a label with nothing under it.
        if not inner:
            return f'<td class="{cls}" data-label="{label}"></td>'
        return f'<td class="{cls}" data-label="{label}"><div class="c">{inner}</div></td>'

    def at_row():
        bits = [b for b in (a.get("weighting"), "task and rubric in Canvas") if b]
        return ('<tr class="at">'
                + cell("wk", "Week", e(a["when"].split(", ")[-1]))
                + cell("no", "Slot", f'AT {term["id"][-1]}')
                + f'<td data-label="Lesson"><div class="c ti">{e(at_title(a))}</div></td>'
                + cell("wo", "Set work", e(" · ".join(bits)))
                + cell("oc", "Outcomes", "")
                + cell("st", "Status", "<span>Assessment</span>")
                + "</tr>")

    for l in term["lessons"]:
        if not placed and a_week is not None and (first_week(l["week"]) or 0) >= a_week:
            rows.append(at_row())
            placed = True
        built = "blocks" in l
        # A stub row says nothing in three columns at once. The hub head says it
        # once instead, so the status column stays as sparse as comp D's.
        work, status = "", ""
        if l.get("listening"):
            w = next((x for x in works if x["no"] == l["listening"]), None)
            if w:
                work = f'M {w["no"]:02d} {e(w["short"])}'
        elif built:
            work = "Teacher&rsquo;s choice"
        if l["number"] == current_no:
            cls, status = "on", f"{DOT}On air"
        elif built and current_no is not None and l["number"] < current_no:
            cls, status = "done", "Aired"
        elif built and current_no is not None and l["number"] == current_no + 1:
            cls, status = "", "Next"
        elif not built:
            cls = "stub"
        else:
            cls = ""
        title = e(l["title"])
        if built:
            title = f'<a href="{base}/{term["id"]}/{l["number"]}/">{title}</a>'
        cur = ' aria-current="true"' if l["number"] == current_no else ""
        outcomes = "<br>".join(e(c) for c in (l.get("outcomes") or []))
        rows.append(
            f'<tr class="{cls}"{cur}>'
            + cell("wk", "Week", e(l["week"]))
            + cell("no", "Slot", f'L {l["number"]:02d}')
            + f'<td data-label="Lesson"><div class="c ti">{title}</div></td>'
            + cell("wo", "Set work", work)
            + cell("oc", "Outcomes", outcomes)
            + cell("st", "Status", f"<span>{status}</span>" if status else "")
            + "</tr>"
        )
    if not placed:
        rows.append(at_row())

    pending = sum(1 for l in term["lessons"] if "blocks" not in l)
    note = ""
    if pending == len(term["lessons"]):
        note = (f'<p class="hubnote">{e(term["name"].split(": ")[0])} lessons are titles only '
                "until the content pour. The weeks and the sequence below are the registered ones.</p>")
    elif pending:
        note = f'<p class="hubnote">The last {pending} lessons are titles only until the content pour.</p>'

    body = f"""<main class="hub" id="main">
  {hub_band(site, course, term, current_no, works)}
  <div class="hubhead">
    <h1>{e(term['name'].split(': ')[0])} schedule &nbsp;/&nbsp; {e(term['focusArea'])}</h1>
    <span class="tag muted">{len(term['lessons'])} lessons &nbsp;·&nbsp; {e(a['name'])}, {e(a['when'])}</span>
  </div>
  {note}
  <div class="tw">
    <table class="sched">
      <thead><tr><th>Week</th><th>Slot</th><th>Lesson</th><th>Set work</th><th>Outcomes</th><th style="text-align:right">Status</th></tr></thead>
      <tbody>{"".join(rows)}</tbody>
    </table>
  </div>
</main>"""
    return layout(site, term["name"], body, f"{term['name']}, lesson by lesson.",
                  nav_active=term["id"], strand=term["id"], course=course, works=works)


# -------------------------------------------------------------- the works


def build_works(site, course, works, current_no, current_work):
    base = site["base"]
    lesson_by_no = {l["number"]: (t, l) for t in course["terms_loaded"] for l in t["lessons"]}
    rows = []
    for w in works:
        on = " on" if w["no"] == current_work else ""
        cx = e(w["category"].replace("Music of the ", "").replace("Music of ", ""))
        title = f'<b>{e(w["title"])}</b> {e(w["composer"])}'
        # the fill never carries the position on its own, here or anywhere else
        now = f'<span class="wnow">{DOT}On air</span>' if on else ""
        taught = '<span class="muted">Not yet on the site</span>'
        if w.get("lesson"):
            t, l = lesson_by_no[w["lesson"]]
            href = f'{base}/{t["id"]}/{w["lesson"]}/'
            title = f'<a href="{href}">{title}</a>'
            taught = f'<a href="{href}">L {l["number"]:02d} &nbsp;{e(l["title"])}</a>'
        cur = ' aria-current="true"' if on else ""
        rows.append(
            f'<tr class="{on.strip()}"{cur}>'
            f'<td class="no" data-label="No.">M {w["no"]:02d}</td>'
            f'<td class="ti" data-label="Work">{title}{now}</td>'
            f'<td class="tin" data-label="Taught in">{taught}</td>'
            f'<td class="cx" data-label="Category">{cx}</td>'
            f'<td class="tw2" data-label="Term.week">{w["term"]}.{w["week"]}</td></tr>'
        )
    strands = "".join(
        f'<div class="st-c"><span class="tag muted"><span class="sw" style="background:var(--s{i+1})"></span>'
        f'Term {i+1} &nbsp;·&nbsp; {len(t["lessons"])} lessons</span>'
        f'<span class="n">{e(t["focusArea"])}</span></div>'
        for i, t in enumerate(course["terms_loaded"])
    )
    body = f"""<main class="works" id="main">
  <div class="wkhead">
    <h1>Twenty works, one year</h1>
    <span class="tag muted">The archive &nbsp;·&nbsp; ordered by the week it is taught</span>
  </div>
  <div class="tw">
    <table class="wtable">
      <thead><tr><th>No.</th><th>Work</th><th>Taught in</th><th>Category</th><th style="text-align:right">Term.week</th></tr></thead>
      <tbody>{"".join(rows)}</tbody>
    </table>
  </div>
  <div class="strands">{strands}</div>
</main>"""
    return layout(site, "The Works", body,
                  "The twenty works studied across Year 11 Music 1, in the order they are taught.",
                  nav_active="works", strand="term1", current_work=current_work,
                  course=course, works=works)


# -------------------------------------------------------------------- main


def main():
    site = load("site.json")
    course = load("course", "course.json")
    works = load("course", "works.json")
    terms = [load("course", t, "term.json") for t in ("term1", "term2", "term3")]
    course["terms_loaded"] = terms
    site["course"] = course

    # The live position, updated from debriefs. Defaults to the first lesson,
    # which is the honest "day one" state until 2027 teaching starts.
    current_no = course.get("currentLesson") or terms[0]["lessons"][0]["number"]
    current_term = term_of(course, current_no)
    current_lesson = next(l for l in current_term["lessons"] if l["number"] == current_no)
    current_work = current_lesson.get("listening")

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    pages = 0
    write(["index.html"], build_lesson(site, course, current_term, current_lesson, works,
                                       current_no, is_home=True))
    pages += 1

    for term in terms:
        write([term["id"], "index.html"], build_term(site, course, term, current_no, works))
        pages += 1
        for lesson in term["lessons"]:
            if "blocks" not in lesson:
                continue  # Term 2/3 lessons are stubs: title and week only, no page yet.
            write([term["id"], str(lesson["number"]), "index.html"],
                  build_lesson(site, course, term, lesson, works, current_no))
            pages += 1

    write(["the-works", "index.html"], build_works(site, course, works, current_no, current_work))
    pages += 1

    shutil.copytree(ASSETS, os.path.join(OUT, "assets"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    unbuilt = sum(1 for t in terms[1:] for l in t["lessons"])
    unlinked = sum(1 for w in works if not w.get("lesson"))
    print(f"built {pages} pages into docs/")
    print(f"  on air: lesson {current_no}, {current_term['name']}")
    print(f"  {unbuilt} lesson slots in Term 2/3 are titles only, no page yet")
    print(f"  {unlinked} of {len(works)} works have no lesson page to link to yet")


if __name__ == "__main__":
    main()
