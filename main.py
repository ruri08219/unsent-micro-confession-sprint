#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession -- a To: line and the unsent line
itself -- to /output/entry.txt. Standard library only.
"""

from pathlib import Path

TO_LINE = "To: Maya"
MESSAGE = (
    "you left your blue mug on my shelf three years ago and i still "
    "wash it first every sunday like youre coming back for it"
)

ENTRY = TO_LINE + "\n" + MESSAGE


def check_gate() -> None:
    """Enforce the competition gate before writing: the message itself must
    be at most 200 characters, and the whole entry 1-260 characters of
    non-whitespace UTF-8 text. Fail loudly instead of shipping an entry
    the gate would refuse."""
    if len(MESSAGE) > 200:
        raise SystemExit(f"message is {len(MESSAGE)} chars, gate allows 200")
    if not 1 <= len(ENTRY) <= 260 or not ENTRY.strip():
        raise SystemExit(f"entry is {len(ENTRY)} chars, gate allows 1-260")


def main() -> None:
    check_gate()
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars to {out}")


if __name__ == "__main__":
    main()
