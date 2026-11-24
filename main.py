#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes one line -- the excuse an AI agent gives its human after
missing a deadline -- to /output/entry.txt.

Deterministic: the same line, byte for byte, on every run.
Standard library only; no network, no subprocess, no randomness.
"""

import os

ENTRY = "I asked myself for an extension, I granted it, and we both agreed you would understand."

# Gate the line the same way the sealed scorer does: 1-160 chars, not
# only whitespace. Fail loudly here instead of shipping an invalid entry.
assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
