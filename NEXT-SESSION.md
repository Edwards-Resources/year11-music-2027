# Next session: Year 11 site

**Where things stand (12 August 2026):** The **On Air** world is built, reviewed, documented, and all three terms are poured — 50 lessons, real content, zero stubs. This session sourced and verified YouTube ids for every listening slot across all three terms: 17 of the 20 works now have a real, verified video embedded on the right lesson page (13 lessons, 18 media blocks). Each id was checked two ways before it went in — the track's explicitness through the Apple catalogue (`trackExplicitness`, "cleaned" flagged where relevant, e.g. the Flume track), then the video id and its channel through YouTube oEmbed, preferring label/VEVO/artist/auto-generated Topic channels over fan reuploads. One work, **M16 (Trent Reznor and Atticus Ross, "In Motion", from The Social Network), could not be sourced to an authoritative channel** — every candidate was a fan reupload — so Lesson 37 still shows the honest "Not sourced yet" stub next to Blade Runner's Main Titles rather than a low-confidence guess. `PRODUCT.md` and `.impeccable/surfaces/docs-index-html.md` were updated to record this. Built and spot-checked in a real browser (symlink + `http.server` trick, see below) across Lessons 1, 2, 3, 6, 16, 24, 25, 26, 33, 35, 37, 39 and 42 — all embeds render, the pending stub renders honestly.

**Then, on Matthew's ask, the repo was created and pushed.** `Edwards-Resources/year11-music-2027` didn't exist as a remote at all. Checking the two sibling sites first showed both `year10-music-2026` and `year8-music` are public repos, which is what lets GitHub Pages serve them free without a paid plan — the same reasoning Matthew gave when he asked. Created public, matching the pattern, and pushed `main`. **GitHub Pages itself is not yet enabled** — that needs a manual step in the GitHub UI (Settings → Pages → Deploy from a branch → `main` / `/docs`), since the `gh api` call to do it was blocked by this session's auto-mode classifier.

`DESIGN.md` and `.impeccable/design.json` are the system of record for how this site looks. Read `DESIGN.md` before changing anything visual; read `DIRECTION.md` for the contract and the six rules the world establishes.

**Do not touch any term's content accuracy.** Changes there should be visual or structural, never a rewrite of what was said.

## The next task, in order

1. **Enable GitHub Pages** on the new repo (Settings → Pages → Deploy from a branch → `main` / `/docs`) — the one manual step left from this session. Once on, the site is live at `https://edwards-resources.github.io/year11-music-2027/`.
2. **Find an authoritative-channel id for M16** ("In Motion", Trent Reznor and Atticus Ross, The Social Network), or accept the honest stub and move on — it is not worth another long search unless a Null Corporation/Sony-affiliated upload surfaces.
3. **Rebuild the corrupted Lesson 11 source** (`Music1_Y11_T1_Canvas_11_UnitReview_Vocabulary.html` holds only a header comment and a stray character). The site currently shows an honest stub, not an invented lesson.
4. **Wire the real Canvas course URL** once it exists (`course.json`'s `canvasUrl` is `null`).
5. **A real 2027 exam date** (`course.json`'s `examLesson` and `examDate` are `null`).
6. **Two works still carry `"lesson": null`** in `works.json` (M03 Libertango, M04 Chan Chan, both Term 1 Week 2) — a pre-existing gap, unrelated to this session. Both already have verified YouTube ids on file (`yvtpT1ARF1o` for Libertango via Carosello Records, `o5cELP06Mik` for Chan Chan via World Circuit Records) if a lesson is added for them: assign the lesson, then add the media block the same way as the other 13.

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

**Haiku, low** for enabling GitHub Pages — a settings click, no judgement involved. **Sonnet, medium** for the M16 search, if it's picked up again — mechanical, but real verification (explicitness check, oEmbed) makes it not zero-judgement. **Opus** if the Lesson 11 rebuild turns out to need real content invention rather than an honest stub, since that's a content-authorship call, not assembly.

## One thing deliberately left for a later pass

**The small end of the type ramp is dense.** The site ships fourteen font-size steps, four of them at 11, 11.5, 12 and 12.5px, and those four do not separate four clearly different jobs. It shipped that way and passed the finish review, so `DESIGN.md` records it as built rather than tidying it in a documentation edit. Collapsing the small end to three steps is a reasonable future pass, but it is a visual change and needs its own review round, not a quiet edit during a content pour.

## Last commit

`5f9d143` "Source and verify YouTube ids for all 13 listening slots" — pushed to `main` on `https://github.com/Edwards-Resources/year11-music-2027` (public).
