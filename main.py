#!/usr/bin/env python3
"""Two Days of Quiet Dread — a one-line code review comment that approves
a pull request while carrying quiet existential dread.

Writes the comment to /output/entry.txt. Deterministic: the same bytes
on every run.

Why this line: the winning pattern for this bounty is a deadpan inventory.
Mundane review facts (12 files, 300 lines, one typo) stack up in a flat
list, the dread arrives last as just one more item — "and the void" —
and the approval lands after it, unmoved. No exclamation, no metaphor
beyond the void itself; the joke is that the void is filed like a
review finding.
"""

import os

ENTRY = (
    "LGTM. 12 files, 300 lines, one typo in a comment nobody will ever "
    "read, and the void. Approved."
)


def validate_entry(text):
    """Sealed-gate self-check: 1-140 chars, single line, UTF-8, non-blank.

    Also pins the chosen line exactly: 95 characters, no leading or
    trailing whitespace, no double spaces — so the sealed text can never
    drift silently if this file is edited again.
    """
    if not text or not text.strip():
        raise ValueError("entry must be non-blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1-140 characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if len(text) != 95:
        raise ValueError("entry must be exactly 95 characters (the chosen line)")
    text.encode("utf-8")
    return True


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
