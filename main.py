"""Write one joke about AI coding agents to entry.txt."""

import os
from pathlib import Path

JOKE = "My coding agent called the refactor 'low risk'. The refactor became the codebase, the codebase became the incident, and the incident became my weekend."

OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the judge reads exactly these bytes.
    (OUT / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
