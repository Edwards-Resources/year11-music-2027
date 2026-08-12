---
name: Year 11 Music 1 (2027), On Air
description: The year as a music station's schedule; the class is what is on air right now.
colors:
  paper: "#FAFAF7"
  ink: "#101014"
  ink-60: "#6C6C74"
  hair: "#D5D5CE"
  strand-term1: "#3DDC97"
  strand-term2: "#FFD23F"
  strand-term3: "#FF6B6B"
typography:
  display:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(1.75rem, 3.4vw, 2.5625rem)"
    fontWeight: 800
    lineHeight: 0.96
    letterSpacing: "-0.02em"
    fontVariation: "font-stretch 110%"
  headline:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-0.005em"
    fontVariation: "font-stretch 112%"
  title:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "0.84375rem"
    fontWeight: 550
    lineHeight: 1.25
    fontVariation: "font-stretch 88%"
  body:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "0.6875rem"
    fontWeight: 650
    lineHeight: 1.15
    letterSpacing: "0.1em"
    fontVariation: "font-stretch 76%"
    textTransform: "uppercase"
rounded:
  none: "0px"
  full: "50%"
spacing:
  gutter-desktop: "1.75rem"
  gutter-mobile: "1.25rem"
  rail-width: "19rem"
  mast-height: "3.625rem"
components:
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    padding: "0.3rem 0.5rem"
  nav-link-current:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    padding: "0.3rem 0.5rem"
  rail-row-onair:
    backgroundColor: "{colors.strand-term1}"
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    padding: "0.5rem 1.25rem 0.55rem"
  rail-row-reading:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.title}"
    padding: "0.5rem 1.25rem 0.55rem"
  chip:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.2rem 0.5rem 0.25rem"
  note-flag:
    backgroundColor: "{colors.strand-term2}"
    textColor: "{colors.ink}"
    padding: "0.7rem 0.8rem 0.8rem"
---

# Design System: Year 11 Music 1 (2027), On Air

## Overview

**Creative North Star: "The Station Front"**

On Air treats the school year as a music station's schedule and the current lesson as what is on air right now. It is built to refuse two things by name: the course-site default of equal-weight lesson cards in a grid, where week one and week nine look identical, and the drenched display-type poster of the site's own previous world ("The Liner Notes"), rejected as too shouty, too dark and too hard to use. What shipped instead is flat, square-cornered, near-white paper with black ink, a single strand colour that changes by term, and one variable typeface whose only lever is width. The page is built to be read off a projector in a daylit classroom before it is read on a desk, so contrast and tracked-caps legibility are load-bearing, not decorative.

The system carries almost no ornament. There are no shadows, no gradients, no rounded corners anywhere except the one live dot that marks "on air", and no second typeface. Character comes entirely from Archivo's width axis: condensed for labels and utility text, near-normal for titles inside lists and tables, expanded for display headings, most expanded for the wordmark. This is a deliberately narrow palette of moves, used exactly and repeatedly, so the page reads the same way at lesson 1 as it does at lesson 50.

**Key Characteristics:**
- Near-white paper, black ink, one flat strand colour per term, black ink on every strand fill, never white or coloured text.
- One family (Archivo variable); character comes from font-stretch, never from a second face or a monospace stand-in.
- Square corners throughout; the live dot is the one circular exception in the whole system.
- No shadows, no gradients; depth and hierarchy come from ink borders, fill, and inversion only.
- State is never colour alone: a filled strand field always carries the words "On air" and a live dot.

## Colors

A two-colour system (paper and ink) with exactly three interchangeable accents, one per term, that always carry black ink.

### Primary
- **Strand Green** (`#3DDC97`, Term 1, Contexts of music): the "on air" fill and Term 1's identifying colour, applied to the rail's current-lesson row, the term-hub live band, the works-table current-work row, and the archive chip for the current work. Always paired with black ink text.
- **Strand Yellow** (`#FFD23F`, Term 2, Creative practice): Term 2's strand colour, and also the fixed colour of the assessment-flag row (`.at`, the AT1/AT2/AT3 row in a rail or schedule) and the `.note` aside (ICIP protocols, content-pending notices) on every page regardless of which term is on air. The build accepts this dual duty deliberately, the css comment on `.note` records that the flag colour is the same yellow everywhere so notes and assessment rows read alike across all three terms, with a 1px ink border added specifically to keep the note distinct from an actual Term 2 strand fill.
- **Strand Red** (`#FF6B6B`, Term 3, Music in focus: film and screen): Term 3's strand colour, same role as the other two.

### Neutral
- **Paper** (`#FAFAF7`): the page background everywhere, including print.
- **Ink** (`#101014`): body text, borders, headings, and the "reading" state fill (page-being-read inversion in the rail and nav).
- **Ink 60** (`#6C6C74`): secondary/muted text, meta labels, "aired" lesson titles, table captions. Never used as a fill; only as text, and only where it clears AA contrast against paper or hair.
- **Hair** (`#D5D5CE`): the hairline border colour for internal dividers (row separators, table body rules, hover fields), one step lighter than a full ink rule, used where a full ink border would be too heavy.

### Named Rules
**The Black Ink On Colour Rule.** Every strand fill, and the yellow note/assessment flag, carries black ink text, never white text on colour and never coloured text on paper. A fourth hue anywhere in the system is a defect, not a variant.

**The Strand Spent Only On What's Live Rule.** A filled strand field means one thing: this is the thing that is actually on air. A term hub's band is strand-filled only when that term is currently on air; any other term's hub gets the identical band geometry rendered on paper with a 1px ink border instead. An earlier version of the system used a strand highlight purely as heading decoration and it was removed for exactly this reason, colour is reserved for live position, never spent on emphasis.

## Typography

**Display Font:** Archivo (variable), with `system-ui, -apple-system, sans-serif` fallback.
**Body Font:** Archivo (variable), same family, normal width and weight, for running prose.
**Label Font:** Archivo (variable), most condensed setting, same family, not a distinct face.

**Character:** One typeface carrying every role in the system. Personality comes entirely from where the width axis sits: condensed and tracked for utility labels (the station's "call sign" register), expanded and heavy for display headings (the "on-air ident" register), and a near-normal width in between for anything meant to be read at length or scanned in a list.

### Hierarchy
- **Display** (weight 800, `clamp(1.75rem, 3.4vw, 2.5625rem)`, line-height 0.96, font-stretch 110%): lesson `<h1>`s. The term-hub equivalent (`.hb-t`) uses the same weight and stretch at a smaller clamp (`clamp(1.5rem, 2.9vw, 2.25rem)`).
- **Headline** (weight 800, 0.9375rem, line-height 1.15, font-stretch 112%, uppercase): section headings inside a lesson (`.sect h2`), and page-level headings on hub/works pages at a larger clamp (112% stretch throughout).
- **Title** (weight 550–650, 0.78–1rem depending on context, font-stretch 88%): the recurring "what is this row" text, rail lesson titles, schedule/works-table lesson names, prev/next lesson names, archive chip titles. This is the system's real body-reading register even though it is bolder than prose.
- **Body** (weight 400, 0.875rem, line-height 1.5, normal width): running prose in section paragraphs, capped at 70ch max-width.
- **Label** (weight 650, 0.6875–0.8125rem, letter-spacing 0.08–0.1em, font-stretch 76%, uppercase): every tracked-caps utility string, nav links, "On air"/"Coming up"/"Aired" status words, table column headers, footer text, permalink text. This is the system's most-used register by instance count.
- **Outcome code** (weight 650, 1rem, font-stretch 84%): NESA outcome codes (e.g. `MU1-11L-01`), a register of its own between Title and Label, used nowhere else.

### Named Rules
**The One Family Rule.** Archivo, always. A second typeface anywhere in the system is a defect, and so is a monospace face standing in for a "catalogue" or "data" register, the width axis does that job instead.

**The 11px Floor Rule.** Tracked caps (the Label register) never go below `0.6875rem` (11px), regardless of how tight the surrounding layout gets. The page is read off a projector in a daylit classroom before it is read on a desk, and tracked caps are the first thing to disappear at a smaller size.

**The Outcome Codes In Full Rule.** NESA outcome codes render unabbreviated (`MU1-11L-01`, not a shortened form), a deliberate departure from the approved comp's abbreviated code style, because the codes are compliance-bearing and must not be reinterpreted for display.

## Layout

The shell is a fixed-width left rail plus a fluid main column (`.split`, `grid-template-columns: 19rem 1fr`) on lesson pages, with a sticky masthead (`3.625rem` tall) above it and an archive band running the full width at the foot of every page, term hub, and works page alike. The rail itself is sticky beneath the masthead and independently scrollable, so the whole term's lesson list stays visible while the lesson content scrolls.

Page gutters are `1.75rem` on desktop, dropping to `1.25rem` at the `46rem` breakpoint. Internal rhythm runs on a fine rem grid rather than a fixed step scale, most gaps fall between `0.35rem` and `1.1rem`, with `1.4–1.6rem` reserved for major section breaks (prev/next, the works/strands split). Lesson content below the rail splits into two columns (`.two`, `1fr 19rem`) for the main teaching content and a narrower sidebar (in-class activities, success criteria, notices).

Two responsive breakpoints matter, both load-bearing rather than cosmetic:
- **`64rem`**: the rail stops being a sticky sidebar and becomes a static, capped, scrollable block (`14.5rem` max-height) sitting above the lesson content. `site.js` scrolls it to the row being read on load, because a rail that opens on Week 1 while the class is at Lesson 9 defeats its own purpose.
- **`46rem`**: every data table (the term schedule, the works table, in-lesson content tables) stops being a table and restacks to label/value rows, each row taking its label from a `data-label` attribute emitted by `build.py`. This exists because an earlier phone layout let tables scroll horizontally, which hid the very columns that carry lesson state (status, week, outcomes) off-screen, position was effectively being carried by an invisible scroll position. Below `46rem`, a filled state (on-air / assessment) moves from the cell to the whole row block, so the colour still reads correctly when a table has become a stack of cards.

## Elevation & Depth

Flat by design, stated directly in the OWN-WORLD contract: no shadows, no gradients, anywhere. Hierarchy and separation are conveyed entirely through ink rules (1px hairline or full-ink borders), fill (paper vs. ink vs. strand colour), and inversion (ink-on-paper flips to paper-on-ink for the page being read). There is no shadow vocabulary to document because none exists in the shipped system, and none should be introduced, a shadow anywhere in this world would be a second material language competing with the flat station-front idea.

### Named Rules
**The Flat-Always Rule.** No box-shadow, no gradient, under any state including hover and focus. Interaction feedback is background fill (hover: hairline grey; strand fill: hover keeps the strand and adds an underline) and, for keyboard focus, a 2px solid ink outline with 2px offset. Depth is never simulated; it is drawn with rules and fills only.

## Shapes

Square corners everywhere, with exactly one deliberate exception. `border-radius` is unset (defaulting to square) on every container, card, table, chip, and button-like element in the system, the OWN-WORLD contract states this directly ("square corners... two line weights"). The one circular element is the live dot (`.live`, `border-radius: 50%`), described in the stylesheet's own comment as "the one moving part in this world": it pulses gently (`prefers-reduced-motion`-respecting) beside the words "On air" wherever that state appears. Its circularity is what marks it as the system's single live signal, distinct from every static square field around it.

Borders come in exactly two weights: a full 1px ink rule (`var(--ink)`) for structural divisions, masthead bottom, rail edges, section tops, table header rules, the note aside's full border, and a 1px hairline in `var(--hair)` for internal, lower-stakes divisions, row separators inside the rail and tables, hover-state backgrounds. There is no third weight.

## Components

### Navigation
The masthead nav (`.site-nav`) is Label-register tracked caps, square, no border-radius. Default state is ink-on-paper; hover fills with the current strand colour; the current page is marked by full ink-on-paper inversion (`aria-current="page"`), which is the same inversion mark used for "the page you're reading" everywhere else in the system, not a nav-specific style.

### The Rail (signature component)
A sticky, independently-scrolling list of every lesson in the current term, always visible on a lesson or hub page (collapses to a capped static scroller below `64rem`). Each row (`.rl`) is a two-column grid: lesson number in Label register, lesson title in Title register, and a status line beneath. Three distinct states, deliberately different so they never read as the same thing:
- **`.rl.on`**, the lesson the class is actually up to: strand-colour fill, black ink, live dot, the words "On air".
- **`.rl[aria-current="page"]:not(.on)`**, the page currently being read: full ink-on-paper inversion. No dot, no "On air" text, this is a different fact from on-air position and must never converge with it, even when they happen to be the same lesson.
- **`.rl.at`**, an assessment task slot inside the sequence: fixed yellow fill regardless of term, non-interactive (no href), because AT tasks live in Canvas.

### Tables (schedule, works, lesson content)
Header row in Label register with a full-ink bottom rule; body rows separated by hairlines; the current/on-air row gets the same strand-fill-plus-label treatment as the rail, never colour alone. Below `46rem` every table restacks to label/value rows via `data-label`, and a filled row's colour moves from individual cells to the whole row block so state keeps reading correctly stacked.

### Chips (the archive)
Small square outlined tags (`.chip`, 1px hairline border, no fill at rest) carrying a work number in Label register and its title in Title register. Hover: border turns full ink, background fills hairline grey. The current work's chip is the **one surface in the system where fill alone marks position**, `.chip.on` fills with the strand colour with no accompanying dot or text, because the approved comp draws the archive this way and the chip also carries `aria-current="true"`, giving the state a second, non-colour signal at the markup level even though it isn't rendered as visible text.

### Notes / Flags
`.note`: fixed yellow fill (`--s2`) with a 1px ink border, used for ICIP protocol notices and content-pending stubs on every term regardless of which strand colour is on air. The ink border is what keeps it visually distinct from an actual Term 2 on-air fill, which is the same yellow with no border.

### Stub / Pending Content
A lesson with no content yet (for example, a source document that is corrupted) still renders the full page shell, masthead, rail, status line, strip, with its content column replaced by a single `.note` explaining what is missing and why, rather than an empty column or a broken layout. A term with only lesson titles renders its rail and schedule rows normally, with `.stub`/`.rl.stub` muting the title text to Ink 60 in place of a real link. This is a real, load-bearing state of the system, not a placeholder to be removed before shipping, because a course site has to be honest about a lesson that has not been built yet without pretending it does not exist.

## Do's and Don'ts

### Do:
- **Do** keep the on-air state (strand fill + dot + "On air") and the reading state (ink inversion) visually distinct on every surface, including when they land on the same lesson.
- **Do** pair every position-bearing colour fill with the words that explain it ("On air", "Next", "Assessment"), colour alone never carries state, with the single documented exception of the archive chip, which carries `aria-current` instead.
- **Do** stack tables to label/value rows below `46rem` using `data-label`, keeping every state-bearing column visible rather than letting it scroll off-screen.
- **Do** use font-stretch as the only lever for typographic character: condensed for labels, near-normal for titles, expanded for headings.
- **Do** render NESA outcome codes in full, never abbreviated.
- **Do** keep `site.js` an enhancement only, the rail scroll-to-current and the success-criteria ticks must degrade gracefully with the script absent.

### Don't:
- **Don't** introduce a second typeface or a monospace face for any "data" or "catalogue" register, the width axis already carries that job.
- **Don't** use white text on a strand colour, or coloured text on paper. Ink is the only text colour that sits on a fill.
- **Don't** add a shadow, gradient, or rounded corner anywhere except the live dot.
- **Don't** spend a strand fill on decoration or emphasis, reserve it strictly for what is actually live, per term-hub band and rail-row precedent.
- **Don't** let a horizontally-scrolling table ship on a narrow viewport; state-bearing columns must never be scrollable out of view.
