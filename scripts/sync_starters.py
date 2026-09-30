"""Copy each exercise's instructions into the top of its starter file.

For every "### Exercise N" section with a "Starter: `<lesson>/<name>`" line,
the instruction text (up to "For example:", an image, a callout or the next
heading) is turned into a comment block at the top of
docs/examples/<lesson>/<name>/main.py. Any existing leading comment block
is replaced.

Run from the repo root: python scripts/sync_starters.py
"""

import re
import textwrap
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
STARTER = re.compile(r"^Starter:\s*`([^`]+)`")
WIDTH = 76


def plain(text):
    """Remove markdown bold, code, links and images."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    return text.rstrip()


def instructions(lines, start):
    """Collect instruction lines after the Starter line."""
    collected = []
    for line in lines[start:]:
        if line.startswith(("#", "For example", "![", "!!!", "???")):
            break
        if line.startswith("```"):
            break
        collected.append(line)
    while collected and not collected[-1].strip():
        collected.pop()
    while collected and not collected[0].strip():
        collected.pop(0)
    return collected


def comment_block(title, body):
    block = [f"# {title}"]
    for line in body:
        text = plain(line)
        if not text.strip():
            block.append("#")
            continue
        indent = "  " if text.startswith("- ") else ""
        wrapped = textwrap.wrap(text, WIDTH, subsequent_indent=indent)
        block.extend(f"# {part}" for part in wrapped)
    block.append("#")
    return block


def update_starter(path, block):
    lines = path.read_text(encoding="utf-8").splitlines()
    index = 0
    while index < len(lines) and lines[index].startswith("#"):
        index += 1
    rest = lines[index:]
    while rest and not rest[0].strip():
        rest.pop(0)
    new = "\n".join(block + [""] + rest) + "\n"
    if path.read_text(encoding="utf-8") != new:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    for page in sorted(DOCS.rglob("*.md")):
        lines = page.read_text(encoding="utf-8").splitlines()
        title = None
        for number, line in enumerate(lines):
            if line.startswith("### Exercise"):
                title = line[4:].strip()
            match = STARTER.match(line)
            if match and title:
                path = DOCS / "examples" / match.group(1) / "main.py"
                if not path.exists():
                    print(f"WARNING: missing starter {path.relative_to(DOCS)}")
                    continue
                block = comment_block(title, instructions(lines, number + 1))
                if update_starter(path, block):
                    changed += 1
    print(f"{changed} starter file(s) updated")


if __name__ == "__main__":
    main()
