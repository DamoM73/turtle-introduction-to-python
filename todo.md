# To do

## Check

- [ ] Open the six Australian Curriculum links in `docs/teachers.md` (lines 57–62) and confirm each shows the right content description: AC9TDI8P05, AC9TDI8P06, AC9TDI8P09, AC9TDI10P05, AC9TDI10P06, AC9TDI10P08. They now redirect from `v9.australiancurriculum.edu.au` to `www.australiancurriculum.edu.au`.
- [ ] Test the Lesson 12 mouse programs in Thonny to confirm clicks still work now that they end with `turtle.done()`.

## Fix flowcharts

Fix these in `working_files/flowcharts.drawio` so they match the code, then export the PNGs over the old ones in `docs/assets/`:

- [ ] `flowchart_lesson_3_3.png` still shows the old three-sided border and `360 / sides` (used in Lesson 6).
- [ ] `flowchart_lesson_4_2.png` still shows `(-15,-150)` (used in Lesson 7).
- [ ] `flowchart_lesson_6_1.png` checks top-left instead of top-right. It was deleted from `docs/assets/`, and Lesson 12 Exercise 1 uses a text hint instead. If you fix it, export it back to `docs/assets/` and add it to that exercise.

## Tidy the repo

- [ ] Move `working_files/logo.psd` (82 MB) out of the repo. It stays in the git history unless the history is rewritten.
- [ ] Decide whether to keep or delete `Claude outputs/` (it holds only a copy of the rework plan).
- [ ] Delete or move your local untracked `.claude/settings.json`, then `git pull` on `zensical` to get your `626e8cc` commit.

## Decide

- [ ] Add redirects from the old Sphinx page addresses (e.g. `/lesson_1.html` → `/lessons/lesson_01/`)? They give a 404 at the moment.
- [ ] After 19 October 2026, check that the **Deploy site** workflow still passes once `ubuntu-latest` moves to Ubuntu 26.
