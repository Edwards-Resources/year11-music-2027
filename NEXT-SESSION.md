# Next session: Year 11 Music 1 (2027)

## Where this stands, 20 October 2026

**The site is finished and on the shared music shell.** All 50 lessons, the three term hubs, The Works and the home page are built by `shell.py` (direction B, Stage Card, berry accent). The On Air world is gone: no `legacy.css`, no old layout functions, no Archivo. Pushed 19 October 2026 at `80c121f`, live at `https://edwards-resources.github.io/year11-music-2027/`.

- 54 pages. Parity 0 missing, sweep 0 hits, `sync.py --check` clean, no sideways scroll at 375.
- `DESIGN.md` says how the data reaches the shell and what is still this site's own (the works archive, twenty works, the assessment row in its real week). The look itself is documented in `../music-shell/README.md` and `../.serve/proto/redesign/SHELL-PLAN.md`.
- 19 of 20 works have verified YouTube ids. M16 ("In Motion", Reznor and Ross) is closed as unsourceable, not deferred: no official upload exists on the artists' channels, a Topic channel or the label's. **Do not reopen it without new information**, for example the album appearing on a Topic channel.

## Next task

Nothing is owed on the build. The next real work is 2027 teaching:

- **Turn `currentLesson`** in `data/course/course.json` as the class moves. That one field drives "Up to here" everywhere, the schedules, the archive's current work and the home page.
- **Wire `canvasUrl`** once Matthew creates the 2027 Canvas course. Until then it stays `null`.

## Left for Matthew

- **Create the 2027 Canvas course**, then `canvasUrl` can be filled in.
- **Re-import the Canvas blueprint** into the test course and walk it in Student View, if not done since 12 August 2026. Detail in `Year 11 Music Planning (New Syllabus)/13 Canvas Blueprint/Music1_Y11_CanvasBlueprint_BuildNotes.md`.
- **Sign-off on the assessment bundle** from the Head Teacher and Deputy, then the notification PDFs into Canvas Module 2.
- **The Term 1 Canvas source pages still carry their own ICIP blocks.** Left deliberately, since teaching content no longer goes on Canvas. Matthew may want the same pass run there.

## Watch out for

- **Never edit this repo's copy of the shell** (`shell.py`, `assets/shell.css`, `assets/shell.js`, the fonts). Edit `music-shell/` and run `python3 music-shell/sync.py year11-music-2027` from `Sites/`. Run `sync.py --check` at the start of any session that touches the site.
- **`site.css` styles furniture only** (the works archive). Never restyle a shell class here.
- **URLs stay exactly as they are.** Canvas frames point at them, and the repo name is compiled into every link.
- **Sweep before every commit**: `python3 music-shell/tools/sweep.py year11-music-2027` from `Sites/`, then parity after every build: `python3 music-shell/tools/parity.py year11-music-2027`. The sweep never prints what it matched; keep notes the same.
- **Build with `/usr/bin/python3`** (3.9). The shell has to import on it.
- **Preview** through the `course-sites` launch config, which serves all the sites from `Sites/.serve/` on port 8820. A `file://` preview has no CSS.
- **`first_week()` returns `None` for any label without a week number**, which has caused three silent failures. Check anything that branches on it against a label with no week.
- **Global lesson numbering is load-bearing** (Term 1 is 1 to 11, Term 2 is 12 to 32, Term 3 is 33 to 50, via `lessonNumberStart` in each `term.json`).
- **Twenty works, never twenty-two.** No school name, no student names or work anywhere in the repo. Verify every YouTube id before shipping.
- **Subagents do not inherit the no-em-dash rule.** Seventeen got through into shipped content once. Check anything an agent writes before committing it.

## Model and effort

**Haiku, low** for a `currentLesson` turn and rebuild. **Sonnet, medium** for content changes to a lesson. Anything that changes how a page looks is shell work, done in `music-shell/`, not here.

## Last commit

`80c121f` The Works on the shared shell; the old On Air layout is gone (pushed). The docs rewrite for the shell follows it.
