"""One Word From Grandma entry.

Writes the single word a grandma would text about AI to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library.
"""

import os
from pathlib import Path

WORD = "robit"  # the typo a grandma makes when she means "robot"


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
