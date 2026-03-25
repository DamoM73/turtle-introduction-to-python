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
