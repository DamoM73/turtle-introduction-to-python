# Admonition Style Guide

| Directive | Colour | Icon |
|---|---|---|
| `{topic}` | Cyan `#00FFF7` | abstract |
| `{hint}` | Orange `#FF7300` | pencil |
| `{note}` | Blue `#0015FF` | info |
| `{question}` | Green `#90FE00` | question |
| `{warning}` | Pink `#FF00A1` | warning |
| all others | Purple `#8400FF` | flame |

## Notes For Reusing This In Another Repo

The admonition colours in this repo are defined in CSS, not in the Markdown content.

- The main colour rules live in `_static/custom.css`.
- `conf.py` loads that file with `html_css_files = ['custom.css']`.
- `question` is a custom admonition added by `_ext/question_admonition.py`.
- Built-in admonitions such as `note`, `hint`, and `warning` are overridden by `_ext/custom_titled_admonitions.py` so they always attach a predictable CSS class.

If you want the same admonition colours in another Sphinx repo, copy these pieces:

1. Copy `_static/custom.css`.
2. In `conf.py`, set `html_static_path = ['_static']` and `html_css_files = ['custom.css']`.
3. If you need `{question}`, copy `_ext/question_admonition.py`, add `_ext` to `sys.path`, and add `"question_admonition"` to `extensions`.
4. If you want the same custom-title behaviour for built-in admonitions, also copy `_ext/custom_titled_admonitions.py` and add `"custom_titled_admonitions"` to `extensions`.

Relevant colour definitions in `_static/custom.css`:

- `question`: `#90FE00` with `rgba(144, 254, 0, 0.2)`
- default / other admonitions: `#8400FF` with `rgba(132, 0, 255, 0.2)`
- `warning`: `#FF00A1` with `rgba(255, 0, 161, 0.2)`
- `note`: `#0015FF` with `rgba(0, 21, 255, 0.2)`
- `hint`: `#FF7300` with `rgba(255, 115, 0, 0.2)`
- `topic`: `#00FFF7` with `rgba(0, 255, 247, 0.2)`

Short instruction for future Codex use in another repo:

> Match admonition colours to the `turtle-introduction-to-python` Sphinx site by copying the admonition CSS rules from `_static/custom.css`. Do not infer colours from the Markdown source. Ensure `conf.py` loads `custom.css`, and if the repo needs the custom `{question}` admonition or matching built-in admonition classes, also copy `_ext/question_admonition.py` and `_ext/custom_titled_admonitions.py` and register those extensions.
