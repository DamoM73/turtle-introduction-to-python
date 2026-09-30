"""Check that every Code explanation box matches the snippet above it.

For every snippet include (--8<-- "path") that is followed by a
??? note "Code explanation" box, report:

- BAD: a reference to a blank line, a comment or a line past the end
- MISSING: a code line with no explanation

Run from the repo root: python scripts/check_explanations.py
"""

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
SNIPPET = re.compile(r'--8<--\s+"([^"]+)"')
BOX = re.compile(r'^\?\?\?\+?\s+note\s+"Code explanation"')
REF = re.compile(r"\*\*lines?\s+(\d+)(?:\s*[–-]\s*(\d+))?\*\*")


def code_lines(path):
    """Return the set of line numbers that hold code, and the line count."""
    lines = path.read_text(encoding="utf-8").splitlines()
    code = set()
    for number, text in enumerate(lines, start=1):
        stripped = text.strip()
        if stripped and not stripped.startswith("#"):
            code.add(number)
    return code, len(lines)


def check_page(page):
    issues = []
    lines = page.read_text(encoding="utf-8").splitlines()
    index = 0
    while index < len(lines):
        match = SNIPPET.search(lines[index])
        if not match:
            index += 1
            continue
        snippet = match.group(1)
        # find the next explanation box before the next snippet
        look = index + 1
        box_start = None
        while look < len(lines):
            if SNIPPET.search(lines[look]):
                break
            if BOX.match(lines[look]):
                box_start = look
                break
            look += 1
        if box_start is None:
            index += 1
            continue
        source = DOCS / snippet
        if not source.exists():
            issues.append(f"{page.name}: missing file {snippet}")
            index = look
            continue
        code, total = code_lines(source)
        covered = set()
        body = box_start + 1
        while body < len(lines) and (lines[body].startswith("    ") or not lines[body].strip()):
            for ref in REF.finditer(lines[body]):
                start = int(ref.group(1))
                end = int(ref.group(2) or start)
                for endpoint in {start, end}:
                    if endpoint > total or endpoint not in code:
                        issues.append(f"{page.name}: BAD line {endpoint} in {snippet}")
                covered.update(range(start, end + 1))
            body += 1
        for number in sorted(code - covered):
            issues.append(f"{page.name}: MISSING line {number} in {snippet}")
        index = body
    return issues


def main():
    issues = []
    for page in sorted(DOCS.rglob("*.md")):
        issues.extend(check_page(page))
    for issue in issues:
        print(issue)
    print(f"{len(issues)} issue(s) found")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
