# Next session: Year 11 is finished. Phase 2 (Year 9) opens.

**The close-out list is closed** (12 August 2026). Every item is either done or named below as genuinely blocked on Matthew, and none of them is a reason to open another Year 11 session. The next session starts Phase 2: Year 9 course design, from near-nothing on disk (one file, `Year 9 Music Term 4.docx`). See `00 Planner/Music 8-12 Master Build Plan.md`, Phase 2.

**Where the site stands.** The **On Air** world is built, reviewed, documented, all three terms poured (50 lessons, zero stubs), and 19 of 20 works have verified YouTube ids across 15 listening slots. Public and live at `https://edwards-resources.github.io/year11-music-2027/`, confirmed working on Matthew's phone. `DESIGN.md` and `.impeccable/design.json` are the system of record for how it looks; `DIRECTION.md` carries the world's contract.

## What the close-out actually resolved

1. **M16's id ("In Motion", Reznor and Ross) is closed as unsourceable, not deferred.** Searched again and stopped: The Null Corporation's own channel carries no upload of it, the "Trent Reznor - Topic" channel carries the duo's later scores but not this album, SonySoundtracksVEVO carries Challengers and not The Social Network, and every candidate naming the track resolves through oEmbed to a fan channel. The "Not sourced yet" stub on Term 3 Lesson 37 is the permanent honest answer. **Do not reopen this without new information**, for example the album appearing on a Topic channel.
2. **Lesson 11 is rewritten and is no longer a stub.** The corrupted source is genuinely gone and Matthew confirmed he has no other copy, so the lesson was authored from what survived: the twelve-question cumulative quiz and answer key already on disk for this exact lesson, the Unit Home page's Weeks 9 to 10 brief, and the vocabulary the other ten Term 1 lessons actually teach. **Matthew has not yet sanity-checked it** (see below). It is the first place in the whole course where "well-formed dot point" is named and worked, which Terms 2 and 3 had been using from Lesson 16 with no introduction.
3. **M03 and M04 are wired into Lesson 1.** Libertango and Chan Chan join Mozart and Puente, which is what that lesson's own comparison step asks for: one frame held against contrasting traditions. Both ids re-verified live on their label channels (Carosello Records, World Circuit Records). All twenty works now link to a lesson page.
4. **Canvas URL: blocked on Matthew.** The 2027 course does not exist yet (confirmed with him 12 August 2026). `canvasUrl` stays null and the nav renders that honestly as "Canvas (course not yet built)". Nothing to do here until he creates the course.
5. **The exam date fields were a false alarm and are gone.** `examLesson`, `examDate` and `examWhen` were dead fields, referenced by no template. There is also no 2027 HSC date to find: Year 11 is the Preliminary course and sits no HSC. The real date is the school's own AT3 examination, which the signed assessment schedule puts at Term 3 Weeks 6 to 7, and that is now carried in `term3/term.json`'s assessment block where the hub actually reads it.

## Three fixes taken beyond the list, all defects rather than scope

- **AT2 and AT3 carried null weightings and a bare "Term 2" / "Term 3" for when.** That put both assessment rows at the bottom of their term hubs instead of in their real week, because `first_week()` returns `None` for a label with no week number. Filled from `Music1_Y11_AssessmentSchedule.docx`, the signed compliance document: AT2 Week 7 at 30%, AT3 Weeks 6 to 7 at 40%, with the real two-part splits. Both rows now land in the right week.
- **Seventeen em dashes across all three terms**, every one in a media block's `brief`, against `PRODUCT.md`'s own rule. All converted to colons. The built site now has none. These were almost certainly agent-written, which is the watch-out below proving itself.
- **The corrupted source file** in `09 Teaching Resources (Term 1)/Canvas Pages (HTML)/` was replaced with a marker pointing at the site page, rather than rebuilt as a Canvas page, because teaching content does not go on Canvas any more. The Term 1 README records why. **Matthew may prefer the full content written back into that file instead; his call.**

## Left for Matthew

- **Sanity-check Lesson 11** at `https://edwards-resources.github.io/year11-music-2027/term1/11/`. It is authored content, not migrated content, and it is the only page on the site that is.
- **Create the 2027 Canvas course**, then the `canvasUrl` can be wired in.
- Standing admin, unchanged: import the Canvas blueprint into a fresh test course before the real blueprint, get Head Teacher and Deputy sign-off on the assessment bundle, then export the notification PDFs into Canvas Module 2.

## Watch out for

- **`file://` previews of `docs/` render as a static snapshot with no CSS or JS in this environment.** Serve properly, and note the site's asset paths assume the GitHub Pages base (`/year11-music-2027/...`): make a symlink named `year11-music-2027` pointing at `docs/` inside a scratch directory, serve *that* directory, and load `http://localhost:<port>/year11-music-2027/...`. The `year11-music` entry in `School Master/.claude/launch.json` does this on port 8805; repoint its `--directory` at the current session's scratchpad.
- **Headless Chrome on this Mac clamps its window to a 500px minimum**, so `--headless --window-size=390,844 --screenshot` lays out at 500px and crops to 390, manufacturing clipping that is not there. Use the in-app browser's `resize_window` instead, which resizes a real viewport.
- **A bare element selector cannot reset a property set one class deep.** This bit twice: `table{min-width:0}` lost to `.wtable{min-width:40rem}`, and `.sched tbody td{width:auto}` lost to `.sched .wk{width:7rem}`. Match specificity when overriding inside the mobile block.
- **`first_week()` returns `None` for any label without a week number**, and that has now caused three separate silent failures. Anything branching on it must be checked against a label carrying no week.
- **The mobile rail is its own scroll container**, so a screenshot can clip the top row of it and look like missing content. Check geometry with `getBoundingClientRect()` before believing a capture.
- **Two different states, easy to conflate.** `.rl.on` (strand fill + dot + the words "On air") is where the class is up to. `aria-current="page"` (ink inversion) is the page being read. They are usually different lessons and must stay visually distinct.
- **A filled strand field never carries position on its own.** The words and the dot travel with it on every surface. The one documented exception is the archive chips, which mark the current work by fill alone because the approved comp draws them that way and they carry `aria-current`.
- **The strand fill is spent only on what is live.** A term hub is strand-filled only when that term is on air; any other term gets the same band geometry on paper with a 1px ink border.
- **`--strand` comes from `data-strand` on `<body>`** and is the term's colour. Black ink on every strand colour, never white text on a fill, never coloured text on paper. A fourth hue is a defect.
- **"On air" is reserved for the current lesson only.** Every other lesson page says *Aired* or *Coming up*.
- **The live position is one field**: `currentLesson` in `data/course/course.json`, default 1. That is the knob the debrief cascade turns once 2027 teaching starts.
- **`site.js` is an enhancement only** and the site must keep working without it.
- **The shipped subagents do not inherit the no-em-dash rule.** Check anything an agent writes before committing it. Seventeen got through into shipped content.
- **Global lesson numbering is load-bearing** (Term 1 = 1-11, Term 2 = 12-32, Term 3 = 33-50, via `lessonNumberStart` in each `term.json`).
- Same standing rules as the sibling sites: no school name anywhere in the repo, no student names or work, twenty works never twenty-two, verify every YouTube id before shipping, each year group keeps its own visual world.
- `.impeccable/mocks/superseded/` is the dead Liner Notes world. Anti-reference, alongside Year 10's Marker Zine and Year 8's Tour Tee. Do not mine it for parts.
- **A pinned world pins the world, not its softest rendition.** This applies to Year 9 next. The first sketch of the Year 11 world was warm cream board and an editorial serif, which is the look every model defaults to. The fix was to spread the comps across three colour strategies and hold the type voice fixed. Do not let Year 9's world arrive as cream plus a serif either.

## Model and effort

**Opus, medium-high** to open Phase 2. Year 9 starts with a world-choice conversation and a course design from almost nothing on disk, which is design judgement rather than assembly. Drop to Sonnet, medium once the world and the scaffold are locked and it becomes a content pour.

## One thing deliberately left for a later pass

**The small end of the type ramp is dense.** The site ships fourteen font-size steps, four of them at 11, 11.5, 12 and 12.5px, and those four do not separate four clearly different jobs. It shipped that way and passed the finish review, so `DESIGN.md` records it as built. Collapsing the small end to three steps is a reasonable future pass, but it is a visual change and needs its own review round.

## Last commit

See `git log`. The close-out commit is the most recent; it was **not pushed automatically** (standing rule).
