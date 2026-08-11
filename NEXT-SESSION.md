# Next session: Year 11 site

**Where things stand (11 August 2026, night):** The site has been **fully redesigned**. The Liner Notes / The Billing world (oxblood, Anton, the giant billing headline) is dead — Matthew rejected it outright mid-session as too shouty, too dark and heavy, and hard to use. It has been replaced by **On Air**, and all 16 pages are rebuilt and committed. See `DIRECTION.md` for the new contract and the full session write-up at `~/Documents/Obsidian Vault/projects/School Master/Session Logs/2026/Year 11 Site World Replaced with On Air.md`.

Do not mine `.impeccable/mocks/superseded/` for parts. That is the dead world, and it is now an anti-reference alongside Year 10's Marker Zine and Year 8's Tour Tee.

## The next task: discharge the FINISH line

The direction contract in every built page ends with `FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md`. That line is **undischarged**. Two passes, in this order:

1. **Finish review.** Spawn `impeccable-finish-reviewer` fresh (no forked history — a reviewer that inherits the build thread inherits its optimism). Its input packet needs: the original request, the artifact path, screenshot paths, the direction contract, the approved comp paths (`.impeccable/mocks/comp-f-stationfront.png` governs home and lesson pages, `comp-d-schedule.png` governs term hubs), and the craft-floor reference path. Apply its material fixes in one batch, recapture the same viewports, and send them back for a verdict.
2. **`DESIGN.md`.** Spawn `impeccable-documenter` afterwards, from the built world rather than from intentions.

Serving the site for screenshots: there is no dev server in the repo. Symlink `docs/` into a scratch dir as `year11-music-2027` and serve the parent (the built pages use absolute `/year11-music-2027/...` paths), then use headless Chrome:
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=1280,900 --screenshot=out.png <url>`

## What's still open after that, in order

1. **Term 2 content pour**: 21 lessons (site numbers 12-32), from `11 Teaching Resources (Term 2)/Lesson Content (docx)/`. `data/course/term2/term.json` already has the right titles and weeks as stubs.
2. **Term 3 content pour**: 18 lessons (site numbers 33-50), from `12 Teaching Resources (Term 3)/Lesson Content (docx)/`. Five weeks are aural practice-paper weeks; those get a stub page describing the paper, never the paper itself.
3. **Audio and YouTube ids for every listening slot.** None exist yet, on purpose. Apple catalogue explicitness check first (`trackExplicitness`, `cleaned` is the one that matters), then oEmbed verification for the YouTube id.
4. **Rebuild the corrupted Lesson 11 source** (`Music1_Y11_T1_Canvas_11_UnitReview_Vocabulary.html` has no real content; the site currently shows an honest stub, not an invented lesson).
5. **Create the GitHub repo** `year11-music-2027` under `Edwards-Resources` and push. **Ask Matthew before pushing.**
6. **Wire the real Canvas course URL** once it exists (`course.json`'s `canvasUrl` is `null`).
7. **A real 2027 exam date** (`course.json`'s `examLesson`/`examDate` are `null`).

## Watch out for

- **The design system is recorded, use it.** `.impeccable/surfaces/docs-index-html.md` holds the comp read as a design system: palette, the two line weights, the type ramp, corner language, and what is deliberately absent (no icons, no imagery, no second typeface). Anything the comps do not show gets built from that record, not invented.
- **`--strand` is set from `data-strand` on `<body>`** and is the term's colour. Black ink goes on every strand colour; never white text on a strand fill, never coloured text on paper. A fourth hue is a defect.
- **Two different states, easy to conflate.** `.rl.on` (strand fill + dot + the words "On air") is where the class is up to. `aria-current="page"` (ink inversion) is the page being read. They are usually different lessons and must stay visually distinct.
- **"On air" is reserved for the current lesson only.** Every other lesson page says *Aired* or *Coming up*. The old build claimed "On air" on all eleven pages; do not reintroduce that.
- **The live position is one field**: `currentLesson` in `data/course/course.json`, default 1. That is the knob the debrief cascade turns once 2027 teaching starts.
- **Comp content should be the worst real case, not a representative one.** The old world's headline was comped on a 16-character title and broke on Lesson 3's 48 characters. When comping anything new, feed it the longest real title and the five-row table.
- **Don't touch Term 1's content accuracy** — the text was transcribed faithfully from the Canvas HTML source. Changes should be visual/structural, not rewriting what was said.
- **Global lesson numbering is load-bearing** (Term 1 = 1-11, Term 2 = 12-32, Term 3 = 33-50, via `lessonNumberStart` in each `term.json`).
- Same standing rules as the sibling sites: no school name anywhere in the repo, no student names/work, twenty works never twenty-two, verify every YouTube id before shipping, each year group keeps its own visual world.
- A `.claude/launch.json` entry named `year11-music` was added at `~/Claude/Projects/School Master/` pointing at a session-specific scratch dir. It is stale in any new session; repoint it or ignore it.

**Model/effort:** Opus, medium for the finish review and DESIGN.md — it is judgement against an approved comp, and the reviewer's findings need weighing rather than mechanical application. Drop to Sonnet, medium once that is signed off and it is the Term 2/3 content pour, which is now mechanical work against a settled design.

## Last commit

`30b4eb4` "Replace The Liner Notes with On Air: full visual redesign" (local repo, not pushed).
