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
