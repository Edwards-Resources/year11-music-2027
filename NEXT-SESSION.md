# Next session: Year 11 site

**Where things stand (12 August 2026):** The **On Air** world is built, reviewed, and documented. The `FINISH:` line in the direction contract is discharged: finish review, one fix batch, verdict pass, a second batch, and `DESIGN.md` written from the built world. Three commits, local only, nothing pushed.

`DESIGN.md` and `.impeccable/design.json` are now the system of record for how this site looks. Read `DESIGN.md` before changing anything visual; read `DIRECTION.md` for the contract and the six rules the world establishes.

## The next task: pour in Term 2

21 lessons, site numbers 12 to 32, from `Year 11 Music Planning (New Syllabus)/11 Teaching Resources (Term 2)/Lesson Content (docx)/`. `data/course/term2/term.json` already holds the right titles and weeks as stubs, so this is filling out lesson objects to match Term 1's shape, then running `python3 build.py`.

A Term 1 lesson object is the template: `title`, `week`, `contentGroup`, `intention`, `whatYouWillDo`, `outcomes`, `steps`, `criteria`, `listening`, `listeningNote`, `blocks`. A lesson without a `blocks` key is treated as a stub everywhere (rail, hub, works table), so the site degrades honestly as you go and you can pour in batches.

**Do not touch Term 1's content accuracy.** It was transcribed faithfully from the Canvas HTML source; changes there should be visual or structural, never a rewrite of what was said.

## Then, in order

1. **Term 3 content pour**: 18 lessons, site numbers 33 to 50, from `12 Teaching Resources (Term 3)/Lesson Content (docx)/`. Five of those weeks are aural practice-paper weeks and get a stub page describing what the paper covers, never the paper itself.
2. **Audio and YouTube ids for every listening slot.** None exist yet, on purpose. Apple catalogue explicitness check first (read `trackExplicitness`; `cleaned` is the one that matters), then oEmbed verification of the video id and its channel. Both checks have caught real faults on the sibling sites.
3. **Rebuild the corrupted Lesson 11 source** (`Music1_Y11_T1_Canvas_11_UnitReview_Vocabulary.html` holds only a header comment and a stray character). The site currently shows an honest stub, not an invented lesson.
4. **Create the GitHub repo** `year11-music-2027` under `Edwards-Resources` and push. **Ask Matthew before pushing.**
5. **Wire the real Canvas course URL** once it exists (`course.json`'s `canvasUrl` is `null`).
6. **A real 2027 exam date** (`course.json`'s `examLesson` and `examDate` are `null`).

## Watch out for

- **The screenshot recipe in the old version of this file was wrong, and it had been copied forward through three handoffs.** Headless Chrome on this Mac **clamps its window to a 500px minimum**, so `--headless --window-size=390,844 --screenshot` lays the page out at 500px and crops to 390. That manufactures clipping that is not there and hides overflow that is. Verified with a probe page that renders `innerWidth`: it reports 500. If you need honest mobile captures, render the page in a same-origin iframe sized to the exact CSS viewport inside a wider window, then crop back to the iframe box. Desktop widths above 500 are unaffected.
- **A bare element selector cannot reset a property set one class deep.** This bit twice in one session: `table{min-width:0}` lost to `.wtable{min-width:40rem}`, and `.sched tbody td{width:auto}` lost to `.sched .wk{width:7rem}`. Both were invisible in the CSS and obvious in the proof. Match specificity when overriding inside the mobile block.
- **`first_week()` returns `None` for any label without a week number**, and that has now caused two separate silent failures ("Term 1, Week 8" read as week 1 last session; the whole AT row vanishing from Terms 2 and 3 this session). Anything new that branches on it should be checked against `"Term 2"` and `"Term 3"`, which are real values in the data.
- **Two different states, easy to conflate.** `.rl.on` (strand fill + dot + the words "On air") is where the class is up to. `aria-current="page"` (ink inversion) is the page being read. They are usually different lessons and must stay visually distinct.
- **A filled strand field never carries position on its own.** The words and the dot travel with it on every surface, including the phone-stacked schedule and the works table. The one documented exception is the archive chips, which mark the current work by fill alone because the approved comp draws them that way and they carry `aria-current`.
- **The strand fill is spent only on what is live.** A term hub is strand-filled only when that term is on air; any other term gets the same band geometry on paper with a 1px ink border.
- **`--strand` comes from `data-strand` on `<body>`** and is the term's colour. Black ink on every strand colour, never white text on a fill, never coloured text on paper. A fourth hue is a defect.
- **"On air" is reserved for the current lesson only.** Every other lesson page says *Aired* or *Coming up*.
- **The live position is one field**: `currentLesson` in `data/course/course.json`, default 1. That is the knob the debrief cascade turns once 2027 teaching starts.
- **`site.js` is an enhancement only** and the site must keep working without it. It scrolls the mobile rail to the row being read and persists the success-criteria ticks. It was dead code until this session (referenced by no page, written against selectors the build never emitted), so if you change class names in `build.py`, check it still matches.
- **The shipped subagents do not inherit the no-em-dash rule.** `DESIGN.md` and `design.json` both needed a pass. Check anything an agent writes before committing it.
- **Comp content should be the worst real case, not a representative one.** Lesson 9's title is 53 characters and Lesson 3's is 50; comp anything new against those, not a short one.
- **Global lesson numbering is load-bearing** (Term 1 = 1-11, Term 2 = 12-32, Term 3 = 33-50, via `lessonNumberStart` in each `term.json`).
- Same standing rules as the sibling sites: no school name anywhere in the repo, no student names or work, twenty works never twenty-two, verify every YouTube id before shipping, each year group keeps its own visual world.
- `.impeccable/mocks/superseded/` is the dead Liner Notes world. Anti-reference, alongside Year 10's Marker Zine and Year 8's Tour Tee. Do not mine it for parts.

## Model and effort

**Sonnet, medium.** The Term 2 and 3 pours are mechanical assembly against a settled, now-documented design: reading .docx into lesson objects that already have a proven shape. Opus is only warranted if a lesson's content will not fit the existing block types and the page composition has to change.

## Last commit

`fb261a5` "Record DESIGN.md from the built world" (local repo, not pushed).
