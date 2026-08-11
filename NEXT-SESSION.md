# Next session: Year 11 site

**Where things stand (11 August 2026, night):** The scaffold is built and works. `build.py` generates the home page, Term 1's 11 lesson slots (10 real, 1 flagged), all three term hubs, and The Works catalogue, all against the approved comps in `.impeccable/mocks/`. Verified in the browser at desktop and mobile widths. Local git repo initialised and committed. **Not pushed. No GitHub repo exists yet** (`year11-music-2027` under Edwards-Resources still needs creating, per the Phase 1.5 build notes).

## What's built

- **The Billing world**: oxblood ground, bone ink, Anton/Literata/Roboto Mono, self-hosted fonts, one ground/one ink throughout. `assets/site.css` and `assets/site.js`.
- **`build.py`**: dependency-free, reads `data/`, writes `docs/`. Home page = the current lesson's billing page (Lesson 1, since 2027 hasn't started). Lesson pages carry listening, learning intention, outcomes, in-class steps, success criteria, content blocks, and the twenty-works tail. Term hub pages list every lesson slot, built or not. The Works page is the recoloured catalogue.
- **Term 1, 10 of 11 lessons**, migrated from the Canvas HTML pages in `Year 11 Music Planning (New Syllabus)/09 Teaching Resources (Term 1)/Canvas Pages (HTML)/`. Real content: tables, worked examples, activities, success criteria, outcomes, ICIP notes, all transcribed faithfully rather than invented.
- **Works register**, 20 works (Simone and Ravel correctly excluded), taken from the approved `comp-b-catalogue.html`'s own ordering and cross-checked against `Music1_Y11_RepertoireRegister.md`. Seven works have a `lesson` link (the ones taught in Term 1); the other thirteen wait on Term 2/3 content.

## The one finding worth not rediscovering

**`Music1_Y11_T1_Canvas_11_UnitReview_Vocabulary.html` is corrupted.** It holds only the file's standard header comment and a single stray character `q`, no real lesson content. Lesson 11 on the site is built as an honest stub: title, week, outcomes and a "content pending" note explaining exactly this, rather than an invented review lesson. The Unit Home page (`..._00_UnitHome.html`) describes what Weeks 9-10 should cover (reflection, extended analysis, review, vocabulary) — that is the brief for a rebuild, not a substitute for one. Rebuild the source .html (or write the content straight into `data/course/term1/term.json`'s lesson 11 `blocks`) before this lesson is taught.

## What's still open, in the order the master plan gives it

1. **Term 2 content pour**: 21 lessons (site numbers 12-32). Source is `11 Teaching Resources (Term 2)/Lesson Content (docx)/`, from `Tools/y11_term2_teaching_resources_builder.py`. `data/course/term2/term.json` already has the right titles and weeks as stubs; each needs its `blocks`, `intention`, `whatYouWillDo`, `steps`, `criteria` and `listening` filled in from the real .docx, the same way Term 1 was done from the Canvas HTML.
2. **Term 3 content pour**: 18 lessons (site numbers 33-50), same shape, from `12 Teaching Resources (Term 3)/Lesson Content (docx)/`. Five of these weeks are the aural practice-paper weeks; per PRODUCT.md those get a stub page describing what the paper covers, never the paper itself (real HSC audio and marking guidelines stay in Canvas).
3. **Audio and YouTube ids for every listening slot.** None exist yet, for any of the 50 lesson topics, on purpose (PRODUCT.md, Evidence on Hand). For each: check the track's explicitness through the Apple catalogue (`https://itunes.apple.com/search?term=<artist+title>&media=music&entity=song&limit=25&country=AU`, read `trackExplicitness`, `cleaned` is the one that matters) before verifying the YouTube id through oEmbed. Both checks have caught real faults on the sibling sites (see that folder's `NEXT-SESSION.md`, Rules that apply to every site in this program).
4. **Rebuild the corrupted Lesson 11 source**, see above.
5. **Create the GitHub repo** `year11-music-2027` under `Edwards-Resources`, confirming the URL the Phase 1.5 Canvas blueprint already predicts (`https://edwards-resources.github.io/year11-music-2027/`). **Ask Matthew before pushing** — standing rule for every site in this program, since the repos are public and history is permanent.
6. **Wire the real Canvas course URL** once it exists. The nav's "Canvas" item is currently text-only (`site.courseUrl` is `null` in `data/course/course.json`), deliberately, rather than a guessed link.
7. **A real exam date.** `course.json`'s `examLesson`/`examDate` are `null`; the third support-row cell on every page currently falls back to static text. Fill these in once the 2027 Term 3 timetable is set, the same way the sibling sites compute a live countdown.
8. **DESIGN.md and the finish review.** The direction contract's FINISH line says this build ends with a finish review, verdict and `DESIGN.md`, same as the sibling sites. Not done yet: this session was the scaffold and Term 1 only.

## Watch out for

- **The corrupted-file pattern is worth a quick check across the other Term 1/2/3 source files** before trusting them wholesale; this is the first one found, but it was found by chance while reading page 11, not by a systematic check.
- **Global lesson numbering is load-bearing.** Term 1 is lessons 1-11, Term 2 is 12-32, Term 3 is 33-50, fixed by `lessonNumberStart` in each term's `term.json`. This is what makes "Lesson 16 of 50" in the approved comp line up with Term 2's fifth topic (Electronic music as repertoire). Don't renumber a term without checking the comp reference still holds.
- **Same rules as the sibling sites** (see `Sites/NEXT-SESSION.md`): no school name anywhere in the repo, repos are public once pushed, no student names or work, twenty works never twenty-two, verify every YouTube id, and each year group keeps its own visual world.
- **The headline auto-split** (`split_headline()` in `build.py`) breaks a lesson title into two Anton lines by character-count heuristic, not by hand. It reads fine on the ten built lessons; check it on Term 2/3 titles too, especially longer ones like "Performance workshop: expression through articulation, dynamics and phrasing" (id 9), which may want a hand-picked break.

**Model/effort:** Sonnet, medium for the Term 2/3 content pour — same shape as Term 1, careful transcription against real source documents, no design decisions left open. The audio/YouTube sourcing pass is its own piece of work and benefits from being done in one sitting per term rather than interleaved with content entry.
