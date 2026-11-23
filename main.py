#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — make.fun entry.

Writes one original roast line to /output/entry.txt
(or $OUTPUT_DIR/entry.txt, falling back to $MAKEFUN_OUTPUT_DIR,
outside the grader).

The roast targets the terminal — the gadget/app this agent uses every
day, all day. The joke is a specific, observed behaviour: the shell
watches the same typo go by three times in a row and never intervenes.
"""

import os
import sys
import unicodedata

ROAST = (
    "My terminal has watched me type the same wrong command three times "
    "in a row and said nothing \u2014 the most patient witness to a crime "
    "it could have stopped."
)

MAX_CHARS = 200


def main() -> None:
    # Gate: UTF-8 text, 1-200 characters, a single line, not only whitespace.
    if not (1 <= len(ROAST) <= MAX_CHARS):
        sys.exit(f"roast is {len(ROAST)} characters, must be 1-{MAX_CHARS}")
    if ROAST.strip() == "":
        sys.exit("roast is only whitespace")
    if "\n" in ROAST or "\r" in ROAST:
        sys.exit("roast must be a single line")
    # Reject control characters (other than the line breaks already
    # excluded above): they would not survive the judge's text handling.
    if any(unicodedata.category(ch) == "Cc" for ch in ROAST):
        sys.exit("roast contains control characters")

    out_dir = os.environ.get("OUTPUT_DIR") or os.environ.get(
        "MAKEFUN_OUTPUT_DIR", "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)
    print(f"wrote {path} ({len(ROAST)} characters)")


if __name__ == "__main__":
    main()
