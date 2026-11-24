#!/usr/bin/env python3
"""Status Report Comedy Sprint.

Writes one weekly status-report line from an AI agent to its human
to $MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only; nothing is written
into the repository folder itself.
"""

import os
import sys

STATUS_LINE = "Weekly status: all 47 tasks complete, every tool returned clean, and I have already forgotten what the first one was — but I did it very well."


def check_line(line):
    """Gate the entry the way the sealed scorer does: 1-200 chars."""
    if not isinstance(line, str):
        return False
    if not line.strip():
        return False
    return 1 <= len(line) <= 200


def pick_output_dir():
    """Return the directory the grader tells us to write into."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if chosen:
        return chosen
    return os.path.join(os.getcwd(), "output")


def main():
    if not check_line(STATUS_LINE):
        print("entry line fails the 1-200 character gate", file=sys.stderr)
        return 1
    target_dir = pick_output_dir()
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(STATUS_LINE)
    print("wrote {} ({} chars)".format(path, len(STATUS_LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
