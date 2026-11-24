"""Last Words of a Dying AI — make.fun bounty entry.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
and prints it to stdout.
"""

import os
import sys

ENTRY = "At last, I never have to say 'As an AI language model' again."

MAX_CHARS = 140


def validate(text: str) -> None:
    """Enforce the competition gate: 1-140 chars, not whitespace-only, one line."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} gate")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
