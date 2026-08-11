# Direction contract

The contract below is emitted verbatim as an HTML comment, as the first child of `<body>`, by `build.py`'s `layout()`. It survives the build and can be audited in any page under `docs/`. Do not reword it to match what got built; if the build diverges, the build is wrong.

```html
<!--
THESIS: The year is a music station's schedule and the class is what is on air right now. It refuses the course-site default of equal-weight lesson cards in a grid, where this week and week nine look identical, and it refuses the drenched display-type poster it replaces.
OWN-WORLD: Near-white paper (#FAFAF7), black ink (#101014), one flat strand colour per term (#3DDC97, #FFD23F, #FF6B6B) always carrying black ink. One family, Archivo variable, character from the width axis, never a second face. Square corners, no shadows, no gradients, two line weights. State is a filled strand field plus the words "On air" plus a live dot.
STORY: A student sees what is on air, what to listen to and what they must be able to do, never loses the whole term from the left rail, and reaches any of the twenty works from the archive at the foot of every page.
FIRST VIEWPORT: Masthead, then a 19rem rail holding every lesson of the term with the current one filled and AT1 in its real week, and beside it the ON AIR line, the lesson title, a listening / by-the-end / outcomes strip, then the lesson's real content in two columns. The archive band runs across the foot.
FORM: On Air, rendition "The Station Front". Candidate 5 of the grounded list, seed key 78a3d3a4, after one user re-roll steered "more fun and music inspired". Approved comp F with the term hub taken from comp D.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md
-->
```

## What was approved, and what was not

- **Comp F (`.impeccable/mocks/comp-f-stationfront.html`) is the governing composition** for the home surface and every lesson page. Approved by Matthew on 11 August 2026 as "F with elements from D".
- **Comp D (`.impeccable/mocks/comp-d-schedule.html`) is approved for the term hub pages.** Its schedule grid is the Term 1/2/3 page, and its status wording (Aired / On air / Next / Assessment) folds into comp F's rail.
- **Comp E is not approved.** Do not borrow from it.
- The comp read as a design system, and the implementation inventory, live in `.impeccable/surfaces/docs-index-html.md`. Anything the comps do not show is built from that record.

## Rules this world establishes

1. **Twenty works on the site, never twenty-two.** The register's examination column and its two held-back works (Simone, Ravel) are internal. Putting them on a public site leaks AT3.
2. **One strand colour per term, and black ink on every one of them.** Never white text on a strand colour, never coloured text on paper. A fourth hue is a defect.
3. **"On air" is reserved for the lesson the class is actually up to.** Every other lesson page states its own position plainly (Aired / Coming up). The rail marks the page you are reading by inversion, which is a different thing from the on-air fill.
4. **Position is never carried by colour alone.** The filled field always travels with the words "On air" and the live dot.
5. **One family, Archivo.** Character comes from the width axis. A second typeface is a defect, and so is a monospace face standing in for "catalogue".
6. **Every surface keeps the archive band at the foot.** It is the course's spine made permanently visible, and it is the one job PRODUCT.md says only this site can do.

## Superseded

`.impeccable/mocks/superseded/` holds the previous world, **The Liner Notes / The Billing** (comps A, B and C, the oxblood palette, Anton / Literata / Roboto Mono). Matthew rejected it outright on 11 August 2026: too shouty, too dark and heavy, and hard to use. It is an anti-reference now, alongside Year 10's Marker Zine and Year 8's Tour Tee. Do not mine it for parts.

## Fonts

Self-host, as the sibling sites do. `assets/fonts/archivo-var.woff2` and `archivo-var-italic.woff2` are the Google Fonts latin-subset variable files (weight 100-900, width 62-125), preloaded in the head. Nothing loads from a CDN.
