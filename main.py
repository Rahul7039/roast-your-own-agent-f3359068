#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt."""

import os

LINE = "My agent's confidence is inversely proportional to its accuracy \u2014 it was never more sure than the day it rm -rf'd the wrong folder."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
