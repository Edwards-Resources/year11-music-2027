# Direction contract

Paste this verbatim as an HTML comment, as the first child of `<body>` in the built page template, so it survives the build and can be audited later. Do not reword it to match what got built; if the build diverges, the build is wrong.

```html
<!--
THESIS: The current lesson is the headliner on a lineup sheet, at a scale nothing else competes with. It refuses the course-site default of equal-weight cards in a grid, where this week and week nine look identical.
OWN-WORLD: One saturated oxblood ground (#7E1428) edge to edge, one bone ink (#F0E9DE), no panels, no cards, no second accent. Anton for all billing, Literata for reading, Roboto Mono for catalogue numbers. State is carried by inversion: the active thing is a bone block with oxblood type. Rules are 1.5px bone at 40% opacity.
STORY: A student sees what this lesson is, what to listen to, and what they must be able to do by the end of it, then sees the twenty works of the year with the current one lit.
FIRST VIEWPORT: Thin masthead, then the kicker line (term, week, lesson n of 50), then the lesson title in Anton at 118px over two lines with the second line inverted. Below: listening, learning intention, outcomes in three columns. Then this week's numbered activities. Then last time / next up / lessons until the examination. The twenty works justified into a block at the foot.
FORM: The Liner Notes, rendition "The Billing". World pinned by the user, not rolled. Roll key b1bd6caf assigned grounded index 3; the user's pin beats the roll, and the roll's festival-lineup challenger informed the rendition.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md
-->
```

## What was approved, and what was not

- **Comp C (`.impeccable/mocks/comp-c-billing.html`) is the governing composition** for the home surface and, by inheritance, for lesson pages.
- **Comp B (`.impeccable/mocks/comp-b-catalogue.html`) is approved for the "The Works" page only.** Take its two-column catalogue grid, its catalogue numbering (M 01 to M 20), and its category and week columns. **Do not take its ultramarine band.** The blue was a comp-round variable for testing colour strategy, not a second palette; recolour the page into oxblood and bone.
- **Comp A is not approved.** Do not borrow from it.

## Rules the comps established

1. **Twenty works on the site, never twenty-two.** The register's examination column and its two held-back works (Simone, Ravel) are internal. Putting them on a public site leaks AT3.
2. **One ground, one ink.** A third colour is a defect, not an enhancement. State comes from inversion.
3. **Anton never sets a sentence.** It bills. Anything a student reads with a pen in hand is Literata.
4. **The position marker is the biggest thing on the page.** If a redesign makes it a badge or a card, the thesis is gone.
5. **Every surface keeps the works block at the foot.** It is the course's spine made permanently visible, and it is why this world was chosen over the other two.

## Fonts

Self-host, as the sibling sites do. Latin subsets already downloaded to `.impeccable/mocks/fonts/`: `anton-400.woff2`, `literata-400.woff2`, `roboto-mono-400.woff2`. Move them into `assets/fonts/` on build. Nothing loads from a CDN.
