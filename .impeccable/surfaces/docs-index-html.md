---
version: 1
slug: "docs-index-html"
primary_target: "docs/index.html"
related_targets: []
---

# Surface: site home ("This week"), lesson pages, term hubs, The Works

**Visitor mode:** Read. Students come to understand this lesson and to get back to a work they have studied.

**Audience and job.** 2027 Year 11 Music 1, 16 to 17, senior elective. In class on a projector in daylight, and at home revising for the aural examination. The teacher works down the page live.

**Chosen direction: On Air.** The year as a music station's schedule; the class's real position is what is on air. Replaces The Liner Notes / The Billing, which Matthew rejected outright on 11 August 2026 as too shouty, too dark and heavy, and hard to use. Direction roll seed `78a3d3a4`, assigned index 5, after one re-roll steered "more fun and music inspired".

**Approved comp: `.impeccable/mocks/comp-f-stationfront.html` / `.png`**, approved 11 August 2026 as "F with elements from D". `comp-d-schedule.html` is approved for the **term hub pages only**: its schedule grid becomes the Term 1/2/3 pages, and its status column (Aired / On air / Next / AT1 week) folds into comp F's rail. `comp-e-nowplaying.html` is not approved; do not borrow from it.

**Memorable moment.** The whole term sits permanently in a left rail with the current lesson filled in its strand colour and a live ON AIR dot beside it, so the class never loses its place; the lesson's real content fills the right; the twenty works run as an archive band across the foot of every page.

## The comp read as a design system

Everything the comp does not show gets built from this record.

| Ingredient | Decision |
| --- | --- |
| Ground | `--paper #FAFAF7` near-white, every page, no dark mode |
| Ink | `--ink #101014`; secondary `--ink-60 #6C6C74` (5.0:1 on paper, AA) |
| Strand colour | Term 1 `--s1 #3DDC97`, Term 2 `--s2 #FFD23F`, Term 3 `--s3 #FF6B6B`. Flat fields only. **Black ink on every strand colour**, never white, never coloured text on paper |
| State | Filled strand field + the word "On air" + a live dot. Never colour alone |
| Corner language | Square. No border radius anywhere except the 50% live dot |
| Elevation | None. No shadows, no glass, no gradients. Flat fields and hairlines only |
| Line weights | Two only: `1px var(--ink)` for structural rules, `1px var(--hair) #D5D5CE` for row separators |
| Type | One family, Archivo variable (wght 100-900, wdth 62-125), self-hosted woff2, latin subset. Character comes from the **width axis**, never from a second face |
| Type ramp | Station/plate `118% wdth / 800`; slot titles `84-88% / 550-750`; tags `76% / 650 / 11px / .1em tracked caps`; reading `100% / 400 / 15-16.5px`; caption `100% / 400 italic` |
| Numerals | `font-variant-numeric: tabular-nums` globally. No monospace face anywhere |
| Icons | None. The only graphic mark is the live dot |
| Imagery | None. This world is type, rule and flat field; there is nothing raster in it |

**Compositional commitments.** Masthead 58px with wordmark left, six nav items right, current one a filled ink block. Rail 296px, ink hairline on its right edge, one row per lesson plus AT1 in its real week, strand key at its foot. Content column: ON AIR line, then h1 at 41px/110% width, then a three-cell strip (Now listening / By the end you can / Outcomes) bounded top and bottom by ink rules, then the lesson's own blocks in two columns. Archive band full width at the foot, 20 bordered chips, current work filled.

**Constraints carried in.** No school name anywhere in the repo. Twenty works shown, never twenty-two. No NESA past-paper content. Music 1 only, no Life Skills track. Live position marker. Global lesson numbering 1-50 is load-bearing.

**Unresolved.** No audio or YouTube ids exist for any of the 50 lesson topics; every one needs the Apple explicitness check then oEmbed verification. Repo not yet created in the Edwards-Resources org. Lesson 11's source is corrupt and the page is an honest stub. Term 2 and Term 3 lessons are titles only.
