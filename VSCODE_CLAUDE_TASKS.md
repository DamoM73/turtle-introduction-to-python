# Tasks for Claude in VS Code

These tasks finish the Zensical rework of *A Turtle Introduction to Python*. They couldn't be done from Cowork, which could only create and overwrite files in this folder. It couldn't delete files, run git, access GitHub or write inside `.github/`.

Work on the `zensical` branch. Do the tasks in order and check with Damien before each one marked **Confirm first**. Report the output of the checks after each task.

## Context

- **Site generator:** Zensical 0.0.66 (pinned in `requirements.txt`). Config is `zensical.toml`. Pages are in `docs/`.
- **Preview:** `zensical serve`. **Build:** `zensical build --clean` (must report "No issues found").
- **Audience:** Year 7 students (and their teachers), using Thonny.
- **Structure:** 12 lessons (`docs/lessons/lesson_01.md` to `lesson_12.md`), two guides (`docs/guides/flowcharts.md`, `docs/guides/debugging.md`), `docs/extension.md`, `docs/reference/solutions.md`, `docs/reference/licencing.md` and `docs/teachers.md`.
- **Examples:** `docs/examples/<lesson>/<example>/main.py`, included in pages with `--8<-- "examples/..."` (pymdownx.snippets, base path `docs`). Exercise starters are the `exN_*` folders.
- **Solutions:** `docs/solutions/<lesson>/exN_name.py`, included on the Exercise Solutions page.
- **Student zip:** `python scripts/make_zip.py` builds `docs/downloads/turtle_tutorials.zip` with the layout `turtle_tutorials/lesson_NN/<name>.py` (93 files).
- **Checks:** `python scripts/check_explanations.py` confirms every Code explanation line number matches its example (expect `0 issue(s) found`).
- **Exercise starters:** each starter begins with a comment block holding the exercise wording. If an exercise's wording changes, run `python scripts/sync_starters.py` to update the starters, then rebuild the zip. Solution files have no instruction comment.
- **Colour scheme:** deep pink `#B0006E` (header, tabs, links and headings in light mode), hot pink `#FF00A1`, light pink `#FFADE1` (dark-mode headings), light blue `#8AB4F8` (dark-mode links). Set in `docs/stylesheets/extra.css`.
- **Callouts:** five types, the same on all of Damien's tutorial sites:
    - `!!! learn "In this lesson we will learn"`: amber, target icon, directly under the title and above the video
    - `!!! primm "PRIMM"`: green, flask icon, after every example
    - `??? note "Code explanation"`: purple, `</>` icon, collapsed, after every PRIMM callout
    - `!!! tip "Title"`: light blue, light bulb icon, every other aside
    - `!!! warning "Title"`: hot pink, triangle alert icon
- **Code blocks:** grey border on every code block; error messages use ```` ``` { .text .error linenums="1" } ```` (red border and text).
- **Writing style:** Australian English, written for Year 7, in Damien's inclusive "we" voice. Code explanations are `- **line n** → full sentence ending in a full stop.` Exercises are phrased as questions ("Can you …?").
- **Rework plan:** the full audit and plan are in Damien's Claude project as `turtle-introduction-to-python_rework_plan.md`.

## 1. Remove the old Sphinx site — Confirm first

The old site is still on `main` and will be tagged before merging (task 5), so nothing is lost. Show Damien this list before deleting anything:

- root pages: `index.md`, `introduction.md`, `lesson_1.md` to `lesson_6.md`, `extention.md`, `flowcharts.md`, `debugging.md`, `licencing.md`
- Sphinx files: `conf.py`, `Makefile`, `make.bat`, `_build/`, `_ext/`, `_static/`, `_templates/`, `.tmp_doctrees/`, `.tmp_html/`
- old content folders: `assets/`, `python_files/`, `teacher_resources/` (the old PDFs, slide decks and zips were dropped in the rework)
- stray notes: `notes.md`, `todo.md`, `admonitions.md`, `style.md`
- `license.txt` (duplicate of `LICENSE`)
- root logo copies: `logo.png`, `logo.ico`, `logo_large.png`, `logo_square.png`, `logo_square - Copy.png` (the site uses `docs/assets/logo.png`, `logo_header.png` and `favicon.ico`)
- `%GIT%turtle-introduction-to-python/` (a stray chat history folder)
- `working_files/.$flow_chart_symbols.drawio.dtmp` (a drawio temp file)
- `docs/assets/flowchart_lesson_6_1.png` (no longer used by any page)

Ask Damien about these before touching them:

- `Claude outputs/`: check what it holds.
- `working_files/`: keep the `.drawio` files. `logo.psd` (82 MB) is being moved out of the repo by Damien.

Keep `LICENSE`, `README.md`, `.gitignore`, `.gitattributes`, `requirements.txt`, `zensical.toml`, `VSCODE_CLAUDE_TASKS.md`, `docs/`, `scripts/`, `working_files/` (drawio files only) and `.github/`.

Before deleting, search the repo to confirm nothing in `docs/`, `scripts/` or `zensical.toml` references these files. Then add `.cache/` to `.gitignore` and run `zensical build --clean`.

## 2. Replace the deploy workflow

Overwrite `.github/workflows/write_to_gh_pages.yml` with the workflow below. It builds with Zensical and deploys with GitHub Pages Actions. It only runs on `main`, so pushing to `zensical` won't change the live site.

```yaml
name: Deploy site

# Runs only when changes are pushed to main
on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/configure-pages@v6
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v6
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: zensical build --clean
      - uses: actions/upload-pages-artifact@v5
        with:
          path: site
      - uses: actions/deploy-pages@v5
        id: deployment
```

The action versions come from Zensical's own template. Confirm each version exists on GitHub before committing.

## 3. Update `README.md`

Replace the Sphinx-era README with:

- what the site is and who it is for (Year 7 students learning Python with the turtle module in Thonny, and their teachers)
- how to preview it (`pip install -r requirements.txt`, then `zensical serve`)
- how to rebuild the student zip (`python scripts/make_zip.py`)
- how to update exercise starters (`python scripts/sync_starters.py`)
- how to check explanations (`python scripts/check_explanations.py`)
- the folder layout from the Context section above
- the licences: GPLv3 for code, CC BY-NC-SA 4.0 for content

## 4. Final checks

1. Run `python scripts/make_zip.py`. Expected: `Wrote 93 file(s)`.
2. Run `python scripts/check_explanations.py`. Expected: `0 issue(s) found`.
3. Run `zensical build --clean`. Expected: `No issues found`.
4. Check every external link in `docs/` returns a working page. There are about 70, most on `docs/extension.md`. Report broken ones to Damien rather than guessing replacements.
5. Spell-check the pages for Australian English. `color`, `Color` and `center` inside code, in the "Colour or color?" tip in Lesson 9, and in external link titles are correct and should stay.
6. Commit to `zensical` and push.

## 5. Go live — Confirm first

1. Tag the current `main` as `v1-sphinx` and push the tag, so the old site can be restored.
2. Merge `zensical` into `main` and push.
3. Change the Pages source to GitHub Actions: in the repo settings go to **Settings** → **Pages** → **Source**, or run `gh api -X PUT repos/DamoM73/turtle-introduction-to-python/pages -f build_type=workflow`.
4. Watch the **Deploy site** workflow run, then check that <https://damom73.github.io/turtle-introduction-to-python/> shows the new site.
5. Once the new site is confirmed working, the old `gh-pages` branch can be deleted. **Confirm first.**

## Tasks for Damien (not for Claude)

- Fix these flowcharts in drawio so they match the code, then export the PNGs over the old ones in `docs/assets/`:
    - `flowchart_lesson_3_3.png` still shows the old three-sided border and `360 / sides`
    - `flowchart_lesson_4_2.png` still shows `(-15,-150)`
    - `flowchart_lesson_6_1.png` checks top-left instead of top-right. Lesson 12 Exercise 1 currently uses a text hint instead. If you fix it, it can go back into that exercise.
- Test the Lesson 12 mouse programs in Thonny to confirm clicks still work now that they end with `turtle.done()`.
- Move `working_files/logo.psd` (82 MB) out of the repo.
