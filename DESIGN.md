# Design: Year 11 Music 1 (2027)

**This site is on the shared music shell**, since 19 October 2026. Every page, lessons, the three term hubs, The Works and the home page, is built by `shell.py` and styled by `assets/shell.css`. The look belongs to the shell, not to this repo, and is the same across the music sites apart from one accent per year group. Year 11's is berry (`#B0144F`), set by `data-year="11"`.

So this file is short. It says where the look lives, how this site's data reaches the shell, and the few things that are still Year 11's own.

## Where the look lives

- **`../music-shell/README.md`**: what the shell is, what each file does, and its rules. The shell is a local repo beside this one and is never pushed, so it is not on GitHub.
- **`../.serve/proto/redesign/SHELL-PLAN.md`**: the plan the shell was built to, including the block mapping for this site and the five decisions Matthew accepted on 19 October 2026.
- **`shell.py`, `assets/shell.css`, `assets/shell.js` and the fonts in `assets/fonts/`** are copies. Never edit them here. Edit `music-shell/`, then run `python3 music-shell/sync.py year11-music-2027` from `Sites/`. `sync.py --check` reports a hand-edited copy.

The direction is **B, Stage Card**: a warm grey ground, every section a white card with an icon-and-word label, the title in one solid accent card. Type is Bricolage Grotesque for display and Atkinson Hyperlegible for reading, both self-hosted.

## How the data reaches the shell

The data did not move. `data/course/` is read exactly as before and `build.py` hands the pieces to shell functions.

### Lessons (50)

| Data | On the page |
| --- | --- |
| `title`, `week`, `contentGroup`, number | Head card. The kicker is the term and week, led by "Up to here" on the current lesson; the meta line is "Lesson n of 50" and the content group |
| `intention` | Learning intention. Year 11 pages never showed it before the shell |
| `whatYouWillDo` | By the end you can |
| `criteria`, `outcomes` | Success criteria, with the outcomes at the foot. Codes in full (`MU1-11L-01`), never shortened |
| `steps` | In class, titled "This fortnight" |
| `listening`, `listeningNote` | Listening side card beside In class. The work's name links to the lesson that teaches it; with no work it reads "Teacher's choice" |
| block `media` | Listen. Consecutive media blocks share one card. The brief's text before the first colon is the recording's name, the rest is its caption. A block with no brief says "Not sourced yet" |
| block `table` | Compare. A table whose cells after the first column are all empty becomes a form to type into |
| block `prose` titled "Worked example..." | Worked example, short form |
| block `prose`, other | Learn |
| block `note` | A side card on the section before it |

Under the lesson, standalone only: the term folded shut as "This term", then the works archive.

### Term hubs (3)

Head card, the "Up to here" card (on a term that is not the live one it says the term is done or not started and points across), the assessment card, then every lesson of the term as the shell's schedule. The works archive sits under it.

### The Works

A head card, then the twenty works as a schedule grouped by term, in the order they are met. Each row goes to the lesson that teaches the work. The meta line is composer, lesson, category (with "Music of" trimmed) and term and week. The current work is marked "Up to here". The archive card is left off this one page, since it would only repeat it.

### Home

A copy of the current lesson, with one quiet button under it to open that lesson on its own page.

## What is still this site's own

- **The works archive.** Twenty chips on a white card at the foot of every lesson and hub, standalone only because every chip is a link. Styled in `assets/site.css` (`.wchips`, `.wchip`), the only furniture this site has. The current work's chip carries `aria-current` as well as its tint.
- **Twenty works, never twenty-two.** The register's examination column and its two held-back works are internal. Putting them on a public site leaks AT3.
- **The assessment task sits in its real week** in every schedule, found by `first_week()` from the task's `when`. `first_week()` returns `None` for a label with no week number, which has caused three silent failures; anything that branches on it has to be checked against a label with no week.
- **Global lesson numbering** (Term 1 is 1 to 11, Term 2 is 12 to 32, Term 3 is 33 to 50, from `lessonNumberStart` in each `term.json`). URLs are built from it: `term1/11/`. They stay exactly as they are, because Canvas frames point at them.
- **The live position is one field**, `currentLesson` in `data/course/course.json`. It decides "Up to here" on every page, the done and now states in every schedule, the current work in the archive, and which lesson the home page shows.
- **`site.css` styles furniture only.** Restyling a shell class here is how the sites drift apart, and `sync.py --check` warns about it.

## Words

One vocabulary across the music sites, plain words over the old metaphors (decision 2 in `SHELL-PLAN.md`). "Up to here" replaced "On air", and "Aired" and "Coming up" are gone; the schedule's done and now states say it. The Works keeps its name, because it is the real name of the thing.

## Content decisions that outlived the old look

- **One ICIP note, on Lesson 5 only**, in student voice and titled "Using First Nations material in your work", because that is the composing lesson and it is a real constraint on what a student may make. The three generic teacher-facing notes were removed on 16 August 2026. ICIP is not assessed content in Music 1; do not put it back on other pages without revisiting that.
- **M16 ("In Motion") stays "Not sourced yet"** on Lesson 37. No official upload exists; see `NEXT-SESSION.md`.

## The look this replaced

The site was built in its own world, **On Air** (the year as a music station's schedule, a left rail of the term's lessons, one strand colour per term, Archivo only), from 11 August to 19 October 2026. It retired with the shell. Its full design record is this file as it stood at commit `d2bb9eb`, and the comps are in `.impeccable/mocks/`. `.impeccable/design.json` still describes On Air and is not the current system. Before-shots of the old pages are in `../music-shell/shots/before/`.
