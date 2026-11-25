"""Snooze Button Roast — make.fun entry.

Writes the single-line roast to entry.txt inside MAKEFUN_OUTPUT_DIR
(fallback /output). Python stdlib only, no network, no clock, no
hardcoded paths. Deterministic, byte-identical across runs.
"""

import os

ENTRY = (
    "My alarm rang at 6 AM on a Saturday like it had a shift to "
    "clock into \u2014 mate, the only job here is ruining the one "
    "morning I actually earned."
)


def gate(line):
    """Refuse anything that would fail the entry gate."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-blank with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 chars, got %d" % len(line))


def main():
    gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and re-gate: the file on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("entry.txt does not match the gated entry line")
    gate(written)


if __name__ == "__main__":
    main()
