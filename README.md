# A Turtle Introduction to Python

A tutorial website that introduces Year 7 students to Python using the `turtle` module in [Thonny](https://thonny.org/). Over 12 lessons, students learn sequence, iteration, variables, functions, user input, branching, while loops, Boolean logic and mouse input by drawing with a turtle. The site also has guides on flowcharts and debugging, extension activities, exercise solutions and a page for teachers.

**Website:** <https://damom73.github.io/turtle-introduction-to-python/>

## Previewing the site

The site is built with [Zensical](https://zensical.org/).

```
pip install -r requirements.txt
zensical serve
```

Then open the address shown in the terminal. To do a full build, run `zensical build --clean`. It should report "No issues found".

## Maintaining the content

| Task | Command |
| --- | --- |
| Rebuild the student zip (`docs/downloads/turtle_tutorials.zip`) | `python scripts/make_zip.py` |
| Update exercise starters after changing an exercise's wording | `python scripts/sync_starters.py`, then rebuild the zip |
| Check that every Code explanation line number matches its example | `python scripts/check_explanations.py` |

## Folder layout

```
zensical.toml              site config and navigation
requirements.txt           pinned Zensical version
docs/
  index.md                 home page
  lessons/                 lesson_01.md to lesson_12.md
  guides/                  flowcharts.md, debugging.md
  extension.md             extension activities
  reference/               solutions.md, licencing.md
  teachers.md              notes for teachers
  examples/<lesson>/<example>/main.py
                           example code included in the pages
                           (exN_* folders are exercise starters)
  solutions/<lesson>/exN_name.py
                           exercise solutions
  downloads/               student zip
  assets/                  images, logo and favicon
  stylesheets/extra.css    colour scheme and callout styles
scripts/                   make_zip.py, sync_starters.py, check_explanations.py
working_files/             drawio sources for the flowcharts
```

The site deploys to GitHub Pages from `main` using `.github/workflows/write_to_gh_pages.yml`.

## Licence

- Code is licensed under the [GNU General Public License v3.0](LICENSE).
- Content is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
