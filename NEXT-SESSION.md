# Next session: close out Year 11, then Year 9 starts

**This is meant to be the last Year 11 session before Phase 2 (Year 9) opens.** Matthew's instruction (12 August 2026): finish off everything left for Year 11 in one session, then move on. Treat every item below as something to actually close, not just triage — flag back to Matthew only the ones that are genuinely blocked on something only he can supply (see each item).

**Where things stand:** The **On Air** world is built, reviewed, documented, all three terms poured (50 lessons, zero stubs), and 17 of 20 works have verified YouTube ids wired into 13 listening slots. The repo is public at `Edwards-Resources/year11-music-2027`, pushed, and **live and confirmed working on Matthew's phone** at `https://edwards-resources.github.io/year11-music-2027/` (GitHub Pages enabled by Matthew after the last session). `DESIGN.md` and `.impeccable/design.json` are the system of record for how the site looks; `DIRECTION.md` carries the world's contract. **Do not touch any term's content accuracy** — changes should be visual or structural, never a rewrite of what was said.

## The close-out list

1. **M16's id** ("In Motion", Trent Reznor and Atticus Ross, The Social Network). Last session tried hard and found only fan reuploads. Give it one more focused pass (try a Null Corporation or Sony Classical channel search specifically); if still nothing authoritative turns up, **accept the honest "Not sourced yet" stub as final** and stop — this is meant to close, not loop.
2. **Lesson 11's corrupted source** (`Music1_Y11_T1_Canvas_11_UnitReview_Vocabulary.html` holds only a header comment and a stray character). First check whether Matthew has the real content somewhere else (the Canvas course itself, an earlier export, a Google Doc). If genuinely gone, this becomes a content-authorship call — write a real Unit Review and Vocabulary lesson from the Term 1 scope and sequence, matching the depth of the other ten Term 1 lessons, then ask Matthew to sanity-check it before it goes live. Do not leave the stub in place without asking first — a stub was fine mid-build, not as the final state.
3. **The two `"lesson": null"` works** (M03 Libertango, M04 Chan Chan, `works.json`, both Term 1 Week 2, both category "Music of global music culture"). Lesson 1 already spans Weeks 1-2 and already carries M01 (Mozart) and M02 (Puente, also global music culture) as a deliberate style/genre-versus-tradition pairing. The natural close here is **adding M03 and M04 to Lesson 1 the same way** — two more contrasting global traditions against the same frame — rather than inventing a new lesson slot. Verified ids already on file: `yvtpT1ARF1o` (Piazzolla, Carosello Records) and `o5cELP06Mik` (Buena Vista Social Club, World Circuit Records). Check this reading against the lesson's actual content before wiring it in; if it doesn't fit, ask Matthew rather than force it.
4. **Canvas course URL** (`course.json`'s `canvasUrl`, currently `null`). This needs Matthew to actually create the 2027 Canvas course (he's the admin) before there's a URL to wire in. **Ask him directly whether that course exists yet** rather than leaving this open silently again — if not, this item stays blocked and should be named as blocked in the close-out summary, not just carried forward again.
5. **Real 2027 HSC exam date** (`course.json`'s `examLesson` and `examDate`, both `null`). NESA's 2027 exam timetable may not be published this far out — check before assuming it's gone missing. If genuinely unavailable yet, say so plainly and move on; this is not something to keep re-flagging every session without checking why it's still open.
6. **Matthew's own outstanding admin, worth a one-line reminder rather than action:** import the Canvas blueprint into a fresh test course before the real blueprint, get Head Teacher/DP sign-off on the assessment bundle, then export the notification PDFs into Canvas Module 2. Not this session's work, but the close-out summary should say clearly whether these are still open.

**When this list is actually closed** (each item either done or named as genuinely blocked on Matthew), say so plainly and treat Year 11 as finished. Then the next session opens Phase 2: Year 9 course design, starting from near-nothing on disk (one file, `Year 9 Music Term 4.docx`) — see `00 Planner/Music 8-12 Master Build Plan.md`, Phase 2.

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

**Opus, medium-high** for this session as a whole. It reads like mechanical cleanup but two items are real judgement calls: the Lesson 11 rebuild may need genuine content authorship against the Term 1 scope and sequence, and the M03/M04 placement is a content-fit decision, not just data entry. Start the session at Opus rather than triaging up mid-way.

## One thing deliberately left for a later pass

**The small end of the type ramp is dense.** The site ships fourteen font-size steps, four of them at 11, 11.5, 12 and 12.5px, and those four do not separate four clearly different jobs. It shipped that way and passed the finish review, so `DESIGN.md` records it as built rather than tidying it in a documentation edit. Collapsing the small end to three steps is a reasonable future pass, but it is a visual change and needs its own review round, not a quiet edit during a content pour.

## Last commit

`5f9d143` "Source and verify YouTube ids for all 13 listening slots" — pushed to `main` on `https://github.com/Edwards-Resources/year11-music-2027` (public).
