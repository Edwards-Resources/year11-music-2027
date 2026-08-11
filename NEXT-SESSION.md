# Next session: Year 11 site

**Where things stand (11 August 2026, night):** Scaffold and Term 1 (10 of 11 lessons) are built and working — see the previous entry below for full detail. **Matthew's call at the end of this session: the build quality is noticeably behind `year8-music` and `year10-music-2026`, so the next session is an impeccable design pass on what exists, not the Term 2 content pour.** Don't start Term 2/3 content until that pass is done and he's happy with it.

## The next task: impeccable pass on the current build

Use the `impeccable` skill to critique and improve `Sites/year11-music-2027/` against its own approved direction (`DIRECTION.md`, the comps in `.impeccable/mocks/`) and against the bar the sibling sites already clear (Tour Tee on `year8-music`, Marker Zine on `year10-music-2026`). Some things worth checking, not a prescriptive list:

- **Does the build actually match the approved comp**, or has something drifted or flattened in translation from static HTML comp to templated, data-driven pages? Compare `docs/index.html` and a lesson page side by side against `comp-c-billing.html`, and `docs/the-works/index.html` against `comp-b-catalogue.html` recoloured.
- **Density and rhythm** — the comps were built on one fixed 1280×900 frame; the real site is responsive and has to hold up at more sizes and with more real content (tables, longer titles) than the comp ever carried. Check whether the "bill" layout still reads as confidently as the comp once real Term 1 content (some lessons have five-row tables, some have none) is sitting inside it.
- **The parts I added beyond the comp** — the `.blk` table/prose/note rendering, the term hub pages, the success-criteria checklist — none of these existed in the comp, so they're the most likely source of the "quite bad" read. They were built to the letter of the world's rules (one ground, one ink, Anton bills/Literata reads/Roboto Mono numbers) but not against a comp, so they haven't had the same scrutiny.
- **Already fixed this session, don't re-flag**: a coloured left-border "side-tab" on note/example panels (an AI-UI tell caught by the design hook) was removed in favour of a plain tonal fill.
- **Roboto Mono is locked**, named explicitly in `DIRECTION.md` and both approved comps. Not a candidate for changing during this pass.

## What's still open after the design pass, in order

1. **Term 2 content pour**: 21 lessons (site numbers 12-32), from `11 Teaching Resources (Term 2)/Lesson Content (docx)/`. `data/course/term2/term.json` already has the right titles and weeks as stubs.
2. **Term 3 content pour**: 18 lessons (site numbers 33-50), from `12 Teaching Resources (Term 3)/Lesson Content (docx)/`. Five weeks are aural practice-paper weeks; those get a stub page describing the paper, never the paper itself.
3. **Audio and YouTube ids for every listening slot.** None exist yet, on purpose. Apple catalogue explicitness check first (`trackExplicitness`, `cleaned` is the one that matters), then oEmbed verification for the YouTube id.
4. **Rebuild the corrupted Lesson 11 source** (`Music1_Y11_T1_Canvas_11_UnitReview_Vocabulary.html` has no real content; the site currently shows an honest stub, not an invented lesson).
5. **Create the GitHub repo** `year11-music-2027` under `Edwards-Resources` and push. **Ask Matthew before pushing.**
6. **Wire the real Canvas course URL** once it exists (`course.json`'s `canvasUrl` is `null`).
7. **A real 2027 exam date** (`course.json`'s `examLesson`/`examDate` are `null`).
8. **DESIGN.md and the finish review**, once the design pass above is done and the build is signed off.

## Watch out for

- **Don't touch Term 1's content accuracy while doing the design pass** — the text was transcribed faithfully from the Canvas HTML source; changes here should be visual/structural, not rewriting what was said.
- **Global lesson numbering is load-bearing** (Term 1 = 1-11, Term 2 = 12-32, Term 3 = 33-50, via `lessonNumberStart` in each `term.json`) — matches the approved comp's "Lesson 16 of 50". Don't renumber without checking the comp reference still holds.
- Same standing rules as the sibling sites: no school name anywhere in the repo, no student names/work, twenty works never twenty-two, verify every YouTube id before shipping, each year group keeps its own visual world.

**Model/effort:** Opus, medium-to-high for the impeccable design pass — this is a design-quality judgement call comparing the build against an approved reference and against sibling sites, not mechanical content work. Drop to Sonnet, medium once the pass is done and it's back to the Term 2/3 content pour.

## Last commit

`682c607` "Drop the side-tab border on note/example panels" (local repo, not pushed).
