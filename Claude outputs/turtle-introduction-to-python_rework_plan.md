# A Turtle Introduction to Python: audit and rework plan

- Live site: https://damom73.github.io/turtle-introduction-to-python/
- Repo: `D:\GIT\turtle-introduction-to-python` (GitHub: DamoM73/turtle-introduction-to-python)
- Current build: Sphinx + MyST + Furo, three custom extensions (`question`, titled admonitions, `error` lexer), deployed to `gh-pages` by an old Actions workflow
- Target: Zensical on a `zensical` branch; `main` stays live until go-live

## Decisions

| Area | Decision |
| --- | --- |
| Audience | Year 7 students, plus a teacher page |
| Editor | Thonny |
| Site type | Mixed: sequential lessons (template B) + guides (template D) |
| Lessons | 12 lessons, one per old lesson part |
| Titles | `Lesson N: Topic` |
| Videos | Keep all existing YouTube videos, switched to `youtube-nocookie.com` |
| Code | Every complete program shown on a page becomes a snippet file with a Code explanation box |
| Exercises | Keep all 23 existing exercises, rewritten as questions; add new exercises to Lessons 1, 3 and 11 |
| Solutions | Public `reference/solutions.md` page |
| Teacher resources | Drop old lesson PDFs, slide decks and zips; replace with a student starter zip built by `make_zip.py` |
| Extension page | Keep all links; link-check in VS Code and report broken ones |
| Palette | Derived from the current pink theme (see below) |
| Licences | Content CC BY-NC-SA 4.0, code GPLv3 (unchanged) |

## Page inventory and new numbering

| New page | Source | Video | Existing exercises | Change |
| --- | --- | --- | --- | --- |
| Home (`index.md`) | `index.md` | – | – | Rewrite: purpose, how to use the site, lesson list |
| Teachers (`teachers.md`) | `introduction.md` | – | – | Update to 12 lessons; remove `_build/html` portable note and old zip links; add note that video titles use the old lesson/part numbers |
| Lesson 1: Thonny Introduction | L1 Part 1 | 90T-NE_a50E | none | Add new exercises |
| Lesson 2: Introducing Turtle | L1 Part 2 | CBrm4-ECyMI | Ex 1–3 (square, triangle, hexagon) | |
| Lesson 3: Iteration | L2 Part 1 | _qZzz4lSckk | none | Add new exercises |
| Lesson 4: Range | L2 Part 2 | SpyHWIDWY5M | Ex 1–5 (loops: square, triangle, hexagon, circle, free) | |
| Lesson 5: Variables | L3 Part 1 | mG1O_JamxjQ | Ex 1–3 (square, circle, pentagon) | |
| Lesson 6: Coordinates | L3 Part 2 | F4ajxJwXH58 | Ex 4 → Ex 1 (house) | Renumber |
| Lesson 7: Functions | L4 Part 1 | ZQNU29m5pHY | Ex 1–2 (face, car) | |
| Lesson 8: User Input | L4 Part 2 | HUEgYhYAuB0 | Ex 3 → Ex 1 (count up) | Renumber |
| Lesson 9: Branching | L5 Part 1 | fGEz4QNXpEE | Ex 1–3 (security guard x2, shape position) | |
| Lesson 10: While Loops | L5 Part 2 | A9j7N6kLL1U | Ex 4 → Ex 1 (validation loops) | Renumber |
| Lesson 11: Boolean Logic | L6 Part 1 | 5GrokwhCXXM | none | Add new exercises |
| Lesson 12: Mouse Input | L6 Part 2 | none | Ex 1–3 (quadrant dots) | |
| Flowcharts | `flowcharts.md` | – | – | Guide template |
| Debugging with Thonny | `debugging.md` | – | – | Guide template; uses `buggy_code.py` |
| Extension Activities | `extention.md` | – | – | Fix file name spelling (`extension.md`) |
| Exercise Solutions | `teacher_resources/solutions/*.py` | – | – | New page |
| Licencing | `licencing.md` | – | – | Remove Sphinx copyright note |

New exercise ideas (to confirm when building):

- Lesson 1: Can you change the program so it prints your name? Can you fix three given programs that each produce a different error message (`NameError`, missing bracket, missing quotes)?
- Lesson 3: Can you use a `for` loop to greet everyone in a list of your friends? What happens if we indent the last `print`? Why?
- Lesson 11: Can you predict and then check the result of a set of comparisons joined with `and`, `or` and `not`? Can you write a condition that is `True` only when a score is between 50 and 100?

## Proposed nav

```
Home
Lessons
  Lesson 1: Thonny Introduction … Lesson 12: Mouse Input
Guides
  Flowcharts
  Debugging with Thonny
Extension Activities
Reference
  Exercise Solutions
  Licencing
Teachers
```

## Repo layout

```
zensical.toml
requirements.txt              # zensical==<pinned>
docs/
  index.md
  teachers.md
  lessons/lesson_01.md … lesson_11.md
  guides/flowcharts.md, debugging.md
  extension.md
  reference/solutions.md, licencing.md
  examples/lesson_NN/<step_name>/main.py     # each program shown on the page
  examples/lesson_NN/exN_name/main.py        # exercise starters
  examples/guides/buggy_code/main.py
  solutions/lesson_NN/exN_name.py
  assets/                                    # existing PNGs, logo, favicon
  stylesheets/extra.css
  downloads/turtle_tutorials.zip
scripts/make_zip.py, check_explanations.py
```

Student zip: the zip flattens each starter to `turtle_tutorials/lesson_NN/exN_name.py` (approved), which opens easily in Thonny.

## Syntax conversion specific to this site

| Sphinx | Zensical |
| --- | --- |
| `{topic}` "In this lesson you will learn" | one or two intro sentences (template B) |
| separate `{note}` Predict / Run / Investigate / Modify | one `!!! primm "PRIMM"` callout, then `??? note "Code explanation"` |
| `{hint}` | `!!! tip` |
| `{question}` Exercise N | `### Exercise N` with `Starter:` line |
| `{code-block} error` (red box) | ```` ```text ```` with an `.error` class styled red in `extra.css` |
| `{literalinclude}` + `:emphasize-lines:` | `--8<--` snippet with `hl_lines="…"` |
| `{download}` | link to the zip on the Home page |
| raw iframes | `youtube-nocookie.com/embed/<id>` |

## Bugs and outdated facts found

Lesson 1 (old L1 P1)
- Modify step says to remove the `n` (`prit`) but the error shown is `prnt` (removing the `i`).
- Calls `print` a keyword; it's a built-in function. Same error repeated in the old L3 naming conventions hint.
- Says output appears "in the terminal"; Thonny calls it the Shell.

Lesson 2 (old L1 P2)
- Exercise 2 typo "equlateral".

Lesson 3 (old L2 P1)
- Sentence about greeting six people appears twice.
- The code block examples drop "Jesse" from the list, but the expected output still includes Jesse.
- "The dotted box has is to help…".

Lesson 4 (old L2 P2)
- Says `range` "creates a list"; it creates a sequence of numbers (no need to explain range objects at Year 7, but avoid calling it a list).

Lesson 5 (old L3 P1)
- Investigate box refers to `for i in range(...)`, the code uses `index`.
- "Remove unnecessary variables" shows unchanged code: `degrees` is still on line 5 and line 10 isn't changed. The next block's highlighted lines don't match.

Lesson 6 (old L3 P2)
- Video uses `youtube.com` (not nocookie); same for old L4–L6.
- The `penup`/`pendown` version drops the final `goto(240, 240)`, so the border only has three sides.
- "boarder" typo in code comments.
- Tuple hint implies `window.setup(500, 500)` takes a tuple; it takes two arguments.
- XKCD comic hot-linked without attribution (CC BY-NC 2.5 requires it).

Lesson 7 (old L4 P1)
- "tutrle" typo in comments (also in solution files).
- Line-count claims (71 → 63 → 55 → 59) don't match the code shown. Verify or remove.

Lesson 8 (old L4 P2)
- Prompt text in the instructions (`"How many sides? > "`) doesn't match the code (`"How many sides?> "`).
- Traceback line numbers don't match the code (call is on line 21, not 22), and the breakdown refers to traceback lines as code lines.
- Says the last traceback line tells us *where* the error happened; it tells us *what* happened.
- Says type conversion works "except for Booleans"; `bool()` exists.

Lesson 9 (old L5 P1)
- "Showing variable types" heading doesn't match the content (`isdigit`).
- Line numbers listed in "Playing with colour" (5, 6, 35) don't match the highlighted lines (4–6, 10, 35).
- Exercise 3 starter uses `num.lstrip("-")` without explanation.
- Solution files: "Politley", "Welcom fiend"; Ex 3 solution has Ex 4's header comments.

Lesson 10 (old L5 P2)
- After switching to `while`, the Predict list still includes "all 10 guesses are used".
- Typo "eneter".

Lessons 11 and 12 (old L6)
- Code explanation for line 6 of the `or` example quotes `True or True or False`; the code is `True or False or False`.
- Uses "truthiness" for comparisons; in Python it means how non-Boolean values behave. Replace with plain wording.
- Code comments use PyQt terms (signal/slot), which Year 7 haven't met.
- Grid lines are 400 long in a 600-tall window, so vertical lines run off screen.
- Ex 3 asks for `if`/`elif`/`else` but the solution has no `else`, and clicks on an axis stay orange.
- Explanation line references (29–31, 4–16, 20–25) need re-checking against the file.

Guides
- Debugging: "Nicole" appears capitalised before `capitalize()` runs; "will now evaluating"; "Lets".
- Flowcharts: "two low".

Teacher page and repo
- "Each of the six lessons consist of two parts" and the `_build/html` portable site note are out of date.
- Licencing page apologises for the Sphinx copyright notice; Zensical footer fixes this.
- Leftovers to remove later (Confirm first): `%GIT%turtle-introduction-to-python/`, `.tmp_html/`, `.tmp_doctrees/`, `_build/`, `_ext/`, `_templates/`, `_static/`, `conf.py`, `Makefile`, `make.bat`, `admonitions.md`, `style.md`, `notes.md`, `todo.md`, `license.txt` (duplicate of `LICENSE`), `logo_square - Copy.png`, `teacher_resources/`, `python_files/`, root-level `.md` pages, `working_files/logo.psd` (82 MB; move out of the repo). Keep `working_files/*.drawio`.

## Pedagogical observations

- PRIMM is used well but inconsistently; some sections have Predict/Run only, and Investigate boxes mix explanation with instructions. The primm + Code explanation pattern fixes this.
- Old Lesson 6 Part 1 has no exercises and no Turtle; new Lesson 11 exercises give it a **make** step, and Lesson 12 applies it to Turtle.
- Every lesson currently builds up one program across the page. Keeping that progression (rather than minimal single-method examples) suits Year 7 and matches the videos.
- Lessons 1, 3 and 11 are concept-heavy with no **make** step; new exercises close that gap.
- Lesson 12 has no video; the page notes this.
- Structural comments (`# set up screen`) are introduced in old L3 P2 as a lesson on maintainability, so earlier examples stay comment-free except for the program title comment.

## Colour theme

| Role | Colour | Contrast |
| --- | --- | --- |
| Primary: header, tabs, light-mode links, headings, active nav | Deep pink `#B0006E` | 6.84 on white; white text on it 6.84 |
| Accent: borders, icons, `tip` callout | Hot pink `#FF00A1` (current heading colour) | 3.64 on white (decorative only, never body text); 4.42 on dark |
| Warm light: active/hover tab text, dark-mode headings and accent | Light pink `#FFADE1` (current sidebar) | 4.01 on deep pink (tab labels); 9.44 on dark |
| `note` callout | Purple `#8400FF` (current default admonition) | 6.13 on white |
| `primm` callout | Turtle green `#4D8A00` (darkened from `#90FE00`) | 4.24 on white |

- Dark-mode links: light blue `#8AB4F8` (7.64 on dark).
- `warning` keeps the theme's default orange-red so it stays recognisable.
- Error message blocks: red border and text as on the current site.

## Build order

1. Branch `zensical` in GitHub Desktop (step-by-step).
2. Scaffold: `zensical.toml`, `requirements.txt`, `extra.css`, assets, scripts, Home, Teachers.
3. Lessons 1–4, preview.
4. Lessons 5–8, preview.
5. Lessons 9–12, preview.
6. Guides, Extension, Solutions, Licencing, zip; run checks.
7. `VSCODE_CLAUDE_TASKS.md`: link check, spell-check, cleanup, workflow, README, go-live.
