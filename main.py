#!/usr/bin/env python3
"""Best Advice I Ever Got — one original sentence, written to /output/entry.txt.

The sentence is a single, specific, lived recollection: a named person, a
named moment, advice worth carrying, and a closing beat that shows the
advice still working years later. Stdlib only; no network, no cwd reliance.
"""

from pathlib import Path

ADVICE = (
    "The night before my first job interview, my mother said, \"They're not "
    "doing you a favour by hiring you - remember that when they ask what "
    "you're worth,\" and I've never lowballed myself since."
)


def main() -> None:
    text = ADVICE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") <= 1, "must be a single sentence"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
