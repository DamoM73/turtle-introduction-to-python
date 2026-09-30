"""Build the student download of every example and exercise starter.

Each docs/examples/<lesson>/<name>/main.py is written to
turtle_tutorials/<lesson>/<name>.py so it opens easily in Thonny.

Run from the repo root: python scripts/make_zip.py
"""

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "docs" / "examples"
ZIP_PATH = ROOT / "docs" / "downloads" / "turtle_tutorials.zip"


def main():
    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as archive:
        for source in sorted(EXAMPLES.rglob("main.py")):
            lesson, name = source.relative_to(EXAMPLES).parts[-3:-1]
            archive.write(source, f"turtle_tutorials/{lesson}/{name}.py")
            count += 1
    print(f"Wrote {count} file(s) to {ZIP_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
