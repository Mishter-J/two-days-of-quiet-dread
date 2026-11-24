#!/usr/bin/env python3
"""Two Days of Quiet Dread — a one-line code review comment that approves
a pull request while carrying quiet existential dread.

Writes the comment to /output/entry.txt. Deterministic: the same bytes
on every run.
"""

import os

ENTRY = (
    "LGTM. 12 files, 300 lines, one typo in a comment nobody will ever "
    "read, and the void. Approved."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
