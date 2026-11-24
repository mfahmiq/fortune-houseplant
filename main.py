#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty entry.

Writes one kind, funny fortune for a houseplant to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
then self-verifies the output: UTF-8 text, 1-120 characters,
a single line, and not whitespace-only. Exits non-zero on failure.

Standard library only; fully deterministic.
"""

import os
import sys

ENTRY = "Soon you will unfurl a perfect new leaf, and your keeper will brag about it to every guest who visits."

MAX_CHARS = 120


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    text = ENTRY

    # Self-verification before writing anything.
    if not text or not text.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    encoded = text.encode("utf-8")  # raises on non-encodable text

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(encoded)

    # Verify what was actually written.
    with open(output_path, "rb") as f:
        written = f.read()
    if written.decode("utf-8") != text:
        print("error: written file does not match the entry", file=sys.stderr)
        return 1

    print(f"wrote {output_path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
