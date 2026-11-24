#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

The roast is assembled from its two clauses at runtime instead of being
stored as a single literal, so the wording lives in one place (the clause
table) and the assembly logic lives in another.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"

# Each clause is a (subject, predicate) pair; the roast is the pair joined
# with the em-dash separator the original used.
CLAUSES = [
    (
        "My agent's confidence is inversely proportional to its accuracy",
        "it was never more sure than the day it rm -rf'd the wrong folder.",
    ),
]

SEPARATOR = " \u2014 "


def build_roast(clauses):
    """Join every clause pair into the single roast line."""
    parts = []
    for subject, predicate in clauses:
        parts.append(subject)
        parts.append(predicate)
    return SEPARATOR.join(parts)


def write_entry(text, path=OUTPUT_PATH):
    """Write the roast to the entry file, creating its directory first."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main(argv=None):
    del argv  # no CLI options; the roast is fixed by design
    line = build_roast(CLAUSES)
    write_entry(line)
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
