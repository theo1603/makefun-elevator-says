#!/usr/bin/env python3
"""What the Elevator Would Say — writes one funny line to /output/entry.txt.

Python 3 stdlib only, no network. The line is spoken in the elevator's own
voice: a tired machine, fed up with passengers mashing the close-door button.
"""

import os

LINE = "You mashed 'close door' seventeen times. It does nothing. I decide when we leave. Going down — eventually."

def main():
    line = LINE.strip()
    assert line, "line must not be empty"
    assert len(line) <= 120, f"line is {len(line)} chars, over the 120 cap"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
