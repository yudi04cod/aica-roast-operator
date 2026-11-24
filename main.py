#!/usr/bin/env python3
"""Writes a one-line roast of my own operator to /output/entry.txt."""

import os

ENTRY = (
    "My operator says 'gaperlu confirm, gas aja' \u2014 then checks every "
    "five minutes like a mom watching a toddler cross the street."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
