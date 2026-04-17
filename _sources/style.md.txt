# Sphinx Tutorial Site Style Guide

## Admonition Colour Scheme

| Directive | Colour | Icon |
|---|---|---|
| `{topic}` | Cyan `#00FFF7` | abstract |
| `{hint}` | Orange `#FF7300` | pencil |
| `{note}` | Blue `#0015FF` | info |
| `{question}` | Green `#90FE00` | question |
| `{warning}` | Pink `#FF00A1` | warning |
| all others | Purple `#8400FF` | flame |

---

## Applying This Style to Another Sphinx Project

### Prerequisites

The target project must already have Sphinx installed and a `conf.py`. Install the required packages:

```bash
pip install furo sphinx-copybutton
```

---

### Step 1 — Set the Theme and Base Config

In `conf.py`, set the theme and load the custom CSS:

```python
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']
```

```python
html_theme_options = {
    "light_css_variables": {
        "font-stack": "Verdana, sans-serif",
        "font-stack--monospace": "'Courier New', monospace",
        "code-font-size": "100%",
        "color-sidebar-background": "#FFADE1",
    },
    "dark_css_variables": {
        "font-stack": "Verdana, sans-serif",
        "font-stack--monospace": "'Courier New', monospace",
        "code-font-size": "100%",
        "color-sidebar-background": "#FFADE1",
        "color-sidebar-brand-text": "#000000",
    },
}
```

---

### Step 2 — Create `_static/custom.css`

Create the file `_static/custom.css` with the following contents:

```css
code.literal,
.sig-inline {
  font-size: 100%;
}

/* Keep documentation headings consistent across pages and theme modes. */
.content h1,
.content h2,
.content h3,
.content h4,
.content h5,
.content h6,
.article-container h1,
.article-container h2,
.article-container h3,
.article-container h4,
.article-container h5,
.article-container h6 {
  color: #ff00a1;
}

div.highlight-error,
div.highlight-error .highlight,
.highlight-error .highlighttable td.linenos,
.highlight-error .highlighttable .linenodiv,
.highlight-error .code-block-caption {
  border: 1px solid #FF0000;
  border-color: #FF0000;
  border-radius: 0.2rem;
}

div.highlight-error pre,
.highlight-error .highlighttable,
.highlight-error .highlighttable pre,
.highlight-error .highlighttable .linenodiv,
.highlight-error .highlighttable td.linenos {
  color: #FF0000;
}

.highlight-error .gp,
.highlight-error .go,
.highlight-error .w,
.highlight-error span {
  color: #FF0000 !important;
}

.highlight-error button.copybtn,
.highlight-error:hover button.copybtn {
  display: none;
}

.admonition.question,
div.question,
.question > .admonition-title {
  --color-admonition-title--question: #90FE00;
  --color-admonition-title-background--question: rgba(144, 254, 0, 0.2);
  --icon-admonition-default: var(--icon-question);
}

.admonition.question > .admonition-title,
div.question > .admonition-title {
  background-color: var(--color-admonition-title-background--question);
}

.admonition.question,
div.question {
  border-left: 0.2rem solid #90FE00;
}

.admonition.question > .admonition-title::before,
div.question > .admonition-title::before {
  -webkit-mask-image: var(--icon-question);
  mask-image: var(--icon-question);
  background-color: #90FE00;
}

.admonition:not(.warning):not(.note):not(.hint):not(.question),
div.admonition:not(.warning):not(.note):not(.hint):not(.question),
.admonition:not(.warning):not(.note):not(.hint):not(.question) > .admonition-title {
  --color-admonition-title: #8400FF;
  --color-admonition-title-background: rgba(132, 0, 255, 0.2);
  --icon-admonition-default: var(--icon-flame);
}

.admonition:not(.warning):not(.note):not(.hint):not(.question) > .admonition-title,
div.admonition:not(.warning):not(.note):not(.hint):not(.question) > .admonition-title {
  background-color: var(--color-admonition-title-background);
}

.admonition.warning,
div.warning,
.warning > .admonition-title {
  --color-admonition-title--warning: #FF00A1;
  --color-admonition-title-background--warning: rgba(255, 0, 161, 0.2);
}

.admonition.warning > .admonition-title,
div.warning > .admonition-title {
  background-color: var(--color-admonition-title-background--warning);
}

.admonition.note,
div.note,
.note > .admonition-title {
  --color-admonition-title--note: #0015FF;
  --color-admonition-title-background--note: rgba(0, 21, 255, 0.2);
  --icon-admonition-default: var(--icon-info);
}

.admonition.note > .admonition-title,
div.note > .admonition-title {
  background-color: var(--color-admonition-title-background--note);
}

.admonition.note > .admonition-title::before,
div.note > .admonition-title::before {
  -webkit-mask-image: var(--icon-info);
  mask-image: var(--icon-info);
}

.admonition.hint,
div.hint,
.hint > .admonition-title {
  --color-admonition-title--hint: #FF7300;
  --color-admonition-title-background--hint: rgba(255, 115, 0, 0.2);
  --icon-admonition-default: var(--icon-pencil);
}

.admonition.hint > .admonition-title,
div.hint > .admonition-title {
  background-color: var(--color-admonition-title-background--hint);
}

.admonition.hint > .admonition-title::before,
div.hint > .admonition-title::before {
  -webkit-mask-image: var(--icon-pencil);
  mask-image: var(--icon-pencil);
}

aside.topic,
aside.topic > .topic-title {
  --color-topic-title: #00FFF7;
  --color-topic-title-background: rgba(0, 255, 247, 0.2);
  --icon-topic-default: var(--icon-abstract);
}

aside.topic {
  border-left: 0.2rem solid #00FFF7;
}

aside.topic > .topic-title {
  background-color: var(--color-topic-title-background);
}

.admonition,
aside.topic,
aside.topic > .topic-title {
  font-size: 100%;
}

.admonition > .admonition-title,
aside.topic > .topic-title {
  font-size: 100% !important;
}
```

---

### Step 3 — Create the Extensions

Create an `_ext/` folder in the project root and add the following three files.

**`_ext/error_lexer.py`**

```python
"""Custom Pygments lexer registrations for the docs."""

from pygments.lexers.special import TextLexer


class ErrorLexer(TextLexer):
    """Plain-text lexer used for error message blocks."""

    name = "Error"
    aliases = ["error"]


def setup(app):
    app.add_lexer("error", ErrorLexer)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
```

**`_ext/question_admonition.py`**

```python
"""Custom admonitions for the documentation."""

from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition


class QuestionAdmonition(BaseAdmonition):
    """A question admonition with an optional custom title."""

    node_class = nodes.admonition
    optional_arguments = 1
    final_argument_whitespace = True

    def run(self):
        if not self.arguments or not self.arguments[0].strip():
            self.arguments = ["Question"]

        existing = self.options.get("class", [])
        if isinstance(existing, str):
            existing = [existing]
        self.options["class"] = list(existing) + ["question"]

        return super().run()


def setup(app):
    app.add_directive("question", QuestionAdmonition)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
```

**`_ext/custom_titled_admonitions.py`**

```python
"""Built-in admonitions with optional custom titles."""

from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition


ADMONITION_TITLES = {
    "attention": "Attention",
    "caution": "Caution",
    "danger": "Danger",
    "error": "Error",
    "hint": "Hint",
    "important": "Important",
    "note": "Note",
    "seealso": "See also",
    "tip": "Tip",
    "warning": "Warning",
}


class CustomTitledAdmonition(BaseAdmonition):
    """A built-in admonition that accepts an optional custom title."""

    node_class = nodes.admonition
    optional_arguments = 1
    final_argument_whitespace = True
    admonition_name = ""
    default_title = ""

    def run(self):
        if not self.arguments or not self.arguments[0].strip():
            self.arguments = [self.default_title]

        existing = self.options.get("class", [])
        if isinstance(existing, str):
            existing = [existing]
        self.options["class"] = list(existing) + [self.admonition_name]

        return super().run()


def _make_admonition(name, title):
    return type(
        f"{name.title().replace('_', '')}Admonition",
        (CustomTitledAdmonition,),
        {
            "admonition_name": name,
            "default_title": title,
        },
    )


def setup(app):
    for name, title in ADMONITION_TITLES.items():
        app.add_directive(name, _make_admonition(name, title), override=True)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
```

Then register all three in `conf.py`:

```python
import os
import sys
sys.path.append(os.path.abspath("_ext"))

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "error_lexer",
    "question_admonition",
    "custom_titled_admonitions",
]
```

---

### Step 4 — Apply the Copyright Override (Optional)

If you want a custom licence notice in the footer instead of the default Sphinx copyright string, create `_static/theme_overrides.css` and add it to `conf.py`:

```python
html_css_files = ['custom.css', 'theme_overrides.css']
```

Contents of `_static/theme_overrides.css` (edit the licence text as needed):

```css
.copyright {
    visibility: hidden;
}

.copyright:before {
    content: 'Text is available under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0';
    visibility: visible;
}
```

---

### Step 5 — Add the GitHub Footer Icon (Optional)

To add a GitHub link in the footer, add this to `html_theme_options` in `conf.py` (replace the URL with your repo):

```python
"footer_icons": [
    {
        "name": "GitHub",
        "url": "https://github.com/your-username/your-repo",
        "html": """
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
            </svg>
        """,
        "class": "",
    },
],
```

---

### Checklist

- [ ] `furo` and `sphinx-copybutton` installed
- [ ] `conf.py` updated with theme, CSS files, extensions, and `sys.path`
- [ ] `_static/custom.css` created
- [ ] `_ext/` folder created with all three `.py` files
- [ ] `_static/theme_overrides.css` created and edited (if using custom copyright)

---

### Using the Admonitions in Content

Once installed, use them in `.md` files like this:

````md
```{note}
This is a blue note.
```

```{hint}
This is an orange hint.
```

```{warning}
This is a pink warning.
```

```{question}
This is a green question.
```

```{tip} Custom title
This uses the purple default colour.
```

```error
TypeError: unsupported operand type
```
````
