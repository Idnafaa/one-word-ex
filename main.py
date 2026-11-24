#!/usr/bin/env python3
"""One Word From Your Ex.

The entry is a single word: the word an ex would use to describe you.
This program writes that word, and nothing else, to /output/entry.txt.

The word: "forgettable" -- the most painfully honest one-word verdict an
ex can hand you. Not cruel enough to be angry, not kind enough to be
missed: just gone from memory. It is funny because it stings, and it
stings because it is plausible. Every ex has, at some point, described
someone exactly this way, and every reader has quietly wondered whether
theirs would too.
"""

from __future__ import annotations

import os
import sys

WORD = "forgettable"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(word: str) -> str:
    """Return the word, or raise if it is not exactly one word."""
    cleaned = word.strip()
    if not cleaned:
        raise ValueError("entry must not be blank")
    if any(ch.isspace() for ch in cleaned):
        raise ValueError("entry must be exactly one word, no spaces")
    if not 1 <= len(cleaned) <= 24:
        raise ValueError("entry must be 1 to 24 characters")
    return cleaned


def main() -> int:
    word = validate(WORD)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
