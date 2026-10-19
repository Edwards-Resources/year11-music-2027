#!/usr/bin/env python3
"""Build the Year 11 Music 1 teaching site.

Reads data/, writes docs/. Standard library only, on purpose: no package
manager, no lockfile, nothing that needs updating in years when nobody is
looking (see PRODUCT.md, Stack).

    python3 build.py

Every page is generated. Never edit anything in docs/ by hand; it gets
overwritten.

Every page is built by the shared music shell (shell.py, copied in from
Sites/music-shell by its sync.py): direction B, Stage Card, chosen 19 October
2026. This file only turns the site's data into the shell's pieces. The On Air
world it replaced is recorded in DESIGN.md and .impeccable/.
"""

import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import shell as S  # noqa: E402  the shared page shell, copied in by music-shell/sync.py
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "docs")
ASSETS = os.path.join(ROOT, "assets")


def load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as f:
        return json.load(f)


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


def at_title(a):
    """'AT3: Music in Focus Examination' names its task; 'AT2' does not yet.
    The slot cell beside it already reads AT 2, so a bare repeat is no title."""
    name = a["name"]
    return name.split(": ", 1)[1] if ": " in name else "Assessment task"


# ------------------------------------------------------------------ helpers


def term_of(course, lesson_no):
    for t in course["terms_loaded"]:
        start = t.get("lessonNumberStart", t["lessons"][0]["number"] if t["lessons"] else 1)
        if start <= lesson_no < start + len(t["lessons"]):
            return t
    return course["terms_loaded"][0]


# ----------------------------------------------------- the lesson, on the shell
#
# Lessons and the home page (the current lesson) are built by the shared shell
# (shell.py). Everything below only translates this site's data into the shell's
# components; the markup and the look live in the shell. Every page is on the
# shell since 19 October 2026.

def shell_site(site, course):
    """The site dict the shell's page() needs."""
    nav = [("This week", "/", "home"), ("Term 1", "/term1/", "term1"),
           ("Term 2", "/term2/", "term2"), ("Term 3", "/term3/", "term3"),
           ("The Works", "/the-works/", "works")]
    return {"base": site["base"], "title": site["title"], "year": 11, "key": "y11-2027",
            "foot": course["canvasNote"], "nav": nav, "noindex": site.get("noindex")}


def term_short(term):
    return term["name"].split(": ")[0]


def term_schedule(term, current_no, works):
    """The term's lessons as one group for S.schedule, with the assessment task
    sitting in its real week. `now` is where the class is up to."""
    a = term["assessment"]
    a_week = first_week(a.get("when"))
    rows, placed = [], False

    def at_row():
        bits = [b for b in (a.get("when"), a.get("weighting"), "in Canvas") if b]
        return {"n": f'AT{term["id"][-1]}', "title": at_title(a), "meta": " · ".join(bits), "at": True}

    for l in term["lessons"]:
        if not placed and a_week is not None and (first_week(l["week"]) or 0) >= a_week:
            rows.append(at_row())
            placed = True
        built = "blocks" in l
        if l["number"] == current_no:
            st = "now"
        elif built and current_no is not None and l["number"] < current_no:
            st = "done"
        else:
            st = None
        meta = l["week"]
        w = next((x for x in works if x["no"] == l.get("listening")), None)
        if w:
            meta += f' · M {w["no"]:02d} {w["short"]}'
        rows.append({"n": f'{l["number"]}', "title": l["title"], "meta": meta, "state": st,
                     "href": f'/{term["id"]}/{l["number"]}/' if built else None})
    if not placed:
        rows.append(at_row())
    return [(None, rows)]


def term_card(site, term, current_no, works):
    return S.schedule(term_schedule(term, current_no, works), base=site["base"], label="This term",
                      title=term["focusArea"])


def works_card(site, course, works, current_work):
    """The twenty works, on the foot of every lesson page. Every chip is a link,
    so it is standalone only (the shell hides extras inside Canvas)."""
    base = site["base"]
    chips = []
    for w in works:
        here = ' aria-current="true"' if w["no"] == current_work else ""
        inner = f'<b>M{w["no"]:02d}</b><span>{S.e(w["short"])}</span>'
        if w.get("lesson"):
            href = f'{base}/{term_of(course, w["lesson"])["id"]}/{w["lesson"]}/'
            chips.append(f'<li><a class="wchip int" href="{href}"{here}>{inner}</a></li>')
        else:
            chips.append(f'<li><span class="wchip"{here}>{inner}</span></li>')
    return S.section("works", "The archive", "works", "Twenty works, ordered by the week we meet them",
                     f'<ol class="wchips">{"".join(chips)}</ol>')


def listening_card(site, course, works, lesson):
    """Beside the steps. The work's name goes to the lesson that teaches it
    (inert inside a Canvas frame, like every in-site link)."""
    base = site["base"]
    note = lesson.get("listeningNote")
    if lesson.get("listening"):
        w = next(x for x in works if x["no"] == lesson["listening"])
        name = S.e(w["short"])
        if w.get("lesson") and w["lesson"] != lesson["number"]:
            href = f'{base}/{term_of(course, w["lesson"])["id"]}/{w["lesson"]}/'
            name = f'<a class="int" href="{href}">{name}</a>'
        body = f'<p><strong>{name}</strong><br>{S.e(w["composer"])} · M {w["no"]:02d}</p>'
    else:
        body = "<p><strong>Teacher’s choice</strong></p>"
        note = note or "Confirmed in class."
    if note:
        body += f"<p>{S.rich(note)}</p>"
    return S.side_card("Listening", "listen", body)


def clip_of(b):
    """One media block as a clip. A media block has no title of its own, but its
    brief opens with the recording's name ("Mozart's Eine kleine Nachtmusik,
    first movement: ..."), so that is the name and the rest is the caption."""
    brief = b.get("brief") or ""
    if ": " in brief:
        name, rest = brief.split(": ", 1)
    else:
        name, rest = "Listening example", brief
    return {"title": name, "embed": b.get("embed"), "meta": rest[:1].upper() + rest[1:],
            "pending": "Not sourced yet." if not brief else ""}


def lesson_sections(blocks):
    """The lesson's blocks in order, as shell components. Consecutive media
    blocks share one Listen card; a note becomes the side card of the section
    before it."""
    secs, i = [], 0
    while i < len(blocks):
        b = blocks[i]
        if b["type"] == "note":
            i += 1
            continue
        j = i + 1
        if b["type"] == "media":
            while j < len(blocks) and blocks[j]["type"] == "media":
                j += 1
        nxt = blocks[j] if j < len(blocks) else None
        side = S.note_card(nxt.get("title"), nxt["text"]) if nxt and nxt["type"] == "note" else ""
        if b["type"] == "media":
            secs.append(S.listen([clip_of(m) for m in blocks[i:j]], side=side))
        elif b["type"] == "table":
            form = len(b["columns"]) > 1 and all(not c for r in b["rows"] for c in r[1:])
            secs.append(S.compare(b["columns"], b["rows"], title=b["title"], side=side, form=form))
        elif b["type"] == "prose" and b["title"].startswith("Worked example"):
            # "Worked example: hearing conventions" names its case; a bare
            # "Worked example" is already said by the card's own label.
            t = b["title"].split(": ", 1)[1] if ": " in b["title"] else ""
            secs.append(S.worked(text=b["text"], title=t[:1].upper() + t[1:] if t else None, side=side))
        elif b["type"] == "prose":
            secs.append(S.learn([b["text"]], title=b["title"], side=side))
        i = j
    return secs


def build_lesson(site, course, term, lesson, works, current_no, is_home=False):
    sh = shell_site(site, course)
    base = site["base"]
    n = lesson["number"]
    kicker = f'{term_short(term)} · {lesson["week"]}'
    if n == current_no:
        kicker = "Up to here · " + kicker
    hd = S.head(lesson["title"], kicker=kicker, num=n,
                meta=f'Lesson {n} of {course["totalLessons"]} · {lesson["contentGroup"]}')
    it = S.intent(lesson["intention"], by_end=lesson["whatYouWillDo"], criteria=lesson["criteria"],
                  outcomes=lesson["outcomes"])
    secs = [S.steps(lesson["steps"], title="This fortnight",
                    side=listening_card(site, course, works, lesson))]
    secs += lesson_sections(lesson["blocks"])
    body = S.lesson(hd, it, secs)
    if is_home:
        body += (f'<p class="btns permalink"><a class="btn btn-quiet int" href="{base}/{term["id"]}/{n}/">'
                 f'Open Lesson {n} on its own page</a></p>')

    extras = S.fold(f'This term: {term["focusArea"]}, {len(term["lessons"])} lessons',
                    term_card(site, term, current_no, works))
    extras += works_card(site, course, works, lesson.get("listening"))

    all_l = term["lessons"]
    idx = next((k for k, l in enumerate(all_l) if l["number"] == n), 0)
    prev_l = all_l[idx - 1] if idx else None
    next_l = all_l[idx + 1] if idx + 1 < len(all_l) else None
    pn = (("Previous", prev_l["title"], f'/{term["id"]}/{prev_l["number"]}/') if prev_l and "blocks" in prev_l else None,
          ("Next", next_l["title"], f'/{term["id"]}/{next_l["number"]}/') if next_l and "blocks" in next_l else None)

    if is_home:
        title, crumbs, current = course["name"], None, "home"
    else:
        title = f'Lesson {n}: {lesson["title"]}'
        crumbs = [("Home", "/"), (term_short(term), f'/{term["id"]}/'), (f"Lesson {n}", None)]
        current = term["id"]
    return S.page(sh, title=title, body=body, description=lesson["intention"], crumbs=crumbs,
                  nav_current=current, prevnext=pn, extras=extras)


# ---------------------------------------------------------------- term hubs


def build_term(site, course, term, current_no, works):
    """The term hub, on the shell: head card, where the class is up to, the
    assessment, then every lesson of the term open. The archive of works sits
    at the foot, as on every lesson page."""
    sh = shell_site(site, course)
    a = term["assessment"]
    lessons = term["lessons"]
    first, last = lessons[0]["number"], lessons[-1]["number"]
    short = term_short(term)
    title = term["name"].split(": ", 1)[-1]

    hd = S.head(title, kicker=f"{short} · Lessons {first} to {last}",
                meta=f'{len(lessons)} lessons across {term["weeks"]} weeks')
    if term["focusArea"].lower() != title.lower():
        # "Music in focus (film and screen)" says more than its title does.
        hd = S.head(title, kicker=f"{short} · Lessons {first} to {last}",
                    meta=f'{term["focusArea"]} · {len(lessons)} lessons across {term["weeks"]} weeks')

    # Where the class is up to, said on every hub. On a term that is not the
    # one being taught, the card says so and points across to the live term.
    cur_t = term_of(course, current_no)
    cur = next(l for l in cur_t["lessons"] if l["number"] == current_no)
    k = f'Lesson {current_no} of {course["totalLessons"]} · {cur["week"]}'
    if cur_t["id"] == term["id"]:
        lead = ""
        if cur.get("listening"):
            w = next((x for x in works if x["no"] == cur["listening"]), None)
            if w:
                lead = f'Listening: M {w["no"]:02d} {w["short"]}, {w["composer"]}.'
    else:
        k = f'{term_short(cur_t)} · {k}'
        lead = (f"{short} is done. The class has moved on to {term_short(cur_t)}." if current_no > last
                else f"{short} has not started yet. The class is in {term_short(cur_t)}.")
    up = S.upto(cur["title"], base=site["base"], kicker=k, lead=lead,
                href=f'/{cur_t["id"]}/{current_no}/' if "blocks" in cur else None)

    # The detail ends by saying the task is in Canvas, which the card already says.
    about = re.sub(r"\s*Full task[^.]*\.$", "", a.get("detail", ""))
    at = S.assessment(a["name"], due=a["when"], weighting=a.get("weighting", ""), about=about)

    pending = sum(1 for l in lessons if "blocks" not in l)
    note = ""
    if pending == len(lessons):
        note = (f"{short} lessons are titles only until the content pour. "
                "The weeks and the sequence are the registered ones.")
    elif pending:
        note = f"The last {pending} lessons are titles only until the content pour."
    sched = S.schedule(term_schedule(term, current_no, works), base=site["base"], label="Every lesson",
                       note=note)

    return S.page(sh, title=term["name"], body=hd + up + at + sched,
                  description=f"{term['name']}, lesson by lesson.",
                  crumbs=[("Home", "/"), (short, None)], nav_current=term["id"],
                  extras=works_card(site, course, works, None))


# -------------------------------------------------------------- the works


def build_works(site, course, works, current_no, current_work):
    """The twenty works, on the shell: a head card, then the works grouped by
    the term that teaches them, in the order they are met. Each row goes to
    the lesson that teaches the work. The works archive that sits at the foot
    of every other page would only repeat this one, so it is left off here."""
    by_no = {l["number"]: l for t in course["terms_loaded"] for l in t["lessons"]}
    groups = []
    for t in course["terms_loaded"]:
        rows = []
        for w in (x for x in works if x["term"] == t["number"]):
            bits = [w["composer"]]
            if w.get("lesson"):
                bits.append(f'Lesson {w["lesson"]}: {by_no[w["lesson"]]["title"]}')
            # "Music of global music culture" reads better as its last words.
            cat = re.sub(r"^Music of (the )?", "", w["category"])
            bits += [cat[:1].upper() + cat[1:], f'Term {w["term"]}, Week {w["week"]}']
            rows.append({"n": f'M{w["no"]:02d}', "title": w["title"], "meta": " · ".join(bits),
                         "state": "now" if w["no"] == current_work else None,
                         "href": f'/{t["id"]}/{w["lesson"]}/' if w.get("lesson") else None})
        groups.append((f'{term_short(t)}: {t["focusArea"]}', rows))
    hd = S.head("Twenty works, one year", kicker="The Works",
                meta="Ordered by the week each one is taught")
    body = hd + S.schedule(groups, base=site["base"], label="The archive")
    return S.page(shell_site(site, course), title="The Works", body=body,
                  description="The twenty works studied across Year 11 Music 1, in the order they are taught.",
                  crumbs=[("Home", "/"), ("The Works", None)], nav_current="works")


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

    unbuilt = sum(1 for t in terms for l in t["lessons"] if "blocks" not in l)
    unlinked = sum(1 for w in works if not w.get("lesson"))
    print(f"built {pages} pages into docs/")
    print(f"  on air: lesson {current_no}, {current_term['name']}")
    print(f"  {unbuilt} lesson slots are titles only, no page yet")
    print(f"  {unlinked} of {len(works)} works have no lesson page to link to yet")


if __name__ == "__main__":
    main()
