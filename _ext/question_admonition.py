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
