# Next session: Year 11 site

**Where things stand (12 August 2026):** The **On Air** world is built, reviewed, documented, and all three terms are now poured — 50 lessons, real content, zero stubs. Term 3 (18 lessons, site numbers 33 to 50) was poured this session from the drafted `.docx` sources into `data/course/term3/term.json`, matching Term 1/2's lesson shape. The five weekly aural practice papers (real HSC content) were deliberately left off the site entirely — not referenced by any lesson, no stub page — per Matthew's call this session, overriding an earlier (wrong) note that said they'd get stub pages. Also assigned all eight remaining Term 3 works in `works.json` by content, not just week number: Concerning Hobbits to the leitmotif lesson, Blade Runner and The Social Network as two eras of electronic scoring, and the Saint-Saëns/Westlake pairing to the "Australian work" lesson (Westlake's Babe score quotes the Organ Symphony finale at its climax). Fixed a stale build.py diagnostic along the way (it was hardcoded to always report 39 unbuilt lessons regardless of actual pour state). Built and verified in a real browser (`file://` renders as a CSS-less static snapshot in this environment — serve `docs/` with `http.server` behind a symlink matching the `/year11-music-2027` base path to see it properly). Five commits, local only, nothing pushed.

`DESIGN.md` and `.impeccable/design.json` are the system of record for how this site looks. Read `DESIGN.md` before changing anything visual; read `DIRECTION.md` for the contract and the six rules the world establishes.

**Do not touch any term's content accuracy.** Changes there should be visual or structural, never a rewrite of what was said.

## The next task, in order

1. **Audio and YouTube ids for every listening slot**, across all three terms now. None exist yet, on purpose. Apple catalogue explicitness check first (read `trackExplicitness`; `cleaned` is the one that matters), then oEmbed verification of the video id and its channel. Both checks have caught real faults on the sibling sites.
2. **Rebuild the corrupted Lesson 11 source** (`Music1_Y11_T1_Canvas_11_UnitReview_Vocabulary.html` holds only a header comment and a stray character). The site currently shows an honest stub, not an invented lesson.
3. **Create the GitHub repo** `year11-music-2027` under `Edwards-Resources` and push. **Ask Matthew before pushing.**
4. **Wire the real Canvas course URL** once it exists (`course.json`'s `canvasUrl` is `null`).
5. **A real 2027 exam date** (`course.json`'s `examLesson` and `examDate` are `null`).
6. **Two works still carry `"lesson": null`** in `works.json` (M03 Libertango, M04 Chan Chan, both Term 1 Week 2) — a pre-existing gap from before this session, unrelated to the Term 3 pour. Assign them the same way if picked up.

## Watch out for

- **`file://` previews of `docs/` render as a static snapshot with no CSS or JS in this environment.** Serve properly: `cd docs && python3 -m http.server <port>` won't work alone either, because the site's asset paths assume the GitHub Pages base (`/year11-music-2027/...`). Make a symlink named `year11-music-2027` pointing at `docs/` inside a scratch directory, serve *that* directory, and load `http://localhost:<port>/year11-music-2027/...`.
- **The screenshot recipe in old versions of this file was wrong, and it had been copied forward through three handoffs.** Headless Chrome on this Mac **clamps its window to a 500px minimum**, so `--headless --window-size=390,844 --screenshot` lays the page out at 500px and crops to 390. That manufactures clipping that is not there and hides overflow that is. If you need honest mobile captures, render the page in a same-origin iframe sized to the exact CSS viewport inside a wider window, then crop back to the iframe box. Desktop widths above 500 are unaffected.
- **A bare element selector cannot reset a property set one class deep.** This bit twice already: `table{min-width:0}` lost to `.wtable{min-width:40rem}`, and `.sched tbody td{width:auto}` lost to `.sched .wk{width:7rem}`. Match specificity when overriding inside the mobile block.
- **`first_week()` returns `None` for any label without a week number**, and that has caused two separate silent failures already. Anything new that branches on it should be checked against `"Term 2"` and `"Term 3"`, which are real values in the data.
- **Two different states, easy to conflate.** `.rl.on` (strand fill + dot + the words "On air") is where the class is up to. `aria-current="page"` (ink inversion) is the page being read. They are usually different lessons and must stay visually distinct.
- **A filled strand field never carries position on its own.** The words and the dot travel with it on every surface, including the phone-stacked schedule and the works table. The one documented exception is the archive chips, which mark the current work by fill alone because the approved comp draws them that way and they carry `aria-current`.
- **The strand fill is spent only on what is live.** A term hub is strand-filled only when that term is on air; any other term gets the same band geometry on paper with a 1px ink border.
- **`--strand` comes from `data-strand` on `<body>`** and is the term's colour. Black ink on every strand colour, never white text on a fill, never coloured text on paper. A fourth hue is a defect.
- **"On air" is reserved for the current lesson only.** Every other lesson page says *Aired* or *Coming up*.
- **The live position is one field**: `currentLesson` in `data/course/course.json`, default 1. That is the knob the debrief cascade turns once 2027 teaching starts.
- **`site.js` is an enhancement only** and the site must keep working without it. It scrolls the mobile rail to the row being read and persists the success-criteria ticks.
- **The shipped subagents do not inherit the no-em-dash rule.** Check anything an agent writes before committing it.
- **Comp content should be the worst real case, not a representative one.** Lesson 9's title is 53 characters and Lesson 3's is 50; comp anything new against those, not a short one.
- **Global lesson numbering is load-bearing** (Term 1 = 1-11, Term 2 = 12-32, Term 3 = 33-50, via `lessonNumberStart` in each `term.json`).
- Same standing rules as the sibling sites: no school name anywhere in the repo, no student names or work, twenty works never twenty-two, verify every YouTube id before shipping, each year group keeps its own visual world.
- `.impeccable/mocks/superseded/` is the dead Liner Notes world. Anti-reference, alongside Year 10's Marker Zine and Year 8's Tour Tee. Do not mine it for parts.

## Model and effort

**Sonnet, medium** for the YouTube/audio id pass — mechanical, but each id needs real verification (explicitness check, oEmbed), so it is not zero-judgement. **Opus** if the Lesson 11 rebuild turns out to need real content invention rather than an honest stub, since that's a content-authorship call, not assembly.

## One thing deliberately left for a later pass

**The small end of the type ramp is dense.** The site ships fourteen font-size steps, four of them at 11, 11.5, 12 and 12.5px, and those four do not separate four clearly different jobs. It shipped that way and passed the finish review, so `DESIGN.md` records it as built rather than tidying it in a documentation edit. Collapsing the small end to three steps is a reasonable future pass, but it is a visual change and needs its own review round, not a quiet edit during a content pour.

## Last commit

`ed8ef51` "Point next session at YouTube/audio ids and the Lesson 11 rebuild" (local repo, not pushed).
