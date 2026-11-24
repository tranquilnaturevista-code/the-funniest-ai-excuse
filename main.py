#!/usr/bin/env python3
"""The Funniest AI Excuse — entry program.

Writes one hand-written excuse line to ``/output/entry.txt`` (or
``$OUTPUT_DIR/entry.txt``). The line is fixed: it never changes
between runs. The excuse is one sentence about delegating work to a
background process that never finishes — a very human complaint told
with very machine details, which is the whole joke. Before writing,
the program checks the line against the competition gate — UTF-8
text of 1-200 characters, not only whitespace, all on one line —
and refuses to write it unless the gate passes.
"""

import os
import sys

EXCUSE = (
    "I delegated your task to a background process, and it has been "
    "'almost done' since Tuesday. It stopped answering my pings."
)

GATE_MIN = 1
GATE_MAX = 200


def entry_stats(text):
    """Return (characters, bytes) of `text` encoded as UTF-8."""
    return len(text), len(text.encode("utf-8"))


def gate_problems(text):
    """Return a list of every way `text` breaks the gate ([] = pass)."""
    problems = []
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    # The gate counts characters, not bytes: a multibyte UTF-8
    # character still counts as one character toward the limit.
    length = len(text)
    if length < GATE_MIN or length > GATE_MAX:
        problems.append(
            "entry is %d characters, gate needs %d-%d"
            % (length, GATE_MIN, GATE_MAX)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def report(problems, where=""):
    """Print each gate problem to stderr; return exit code 1."""
    for problem in problems:
        print("gate failure%s: %s" % (where, problem), file=sys.stderr)
    return 1


def write_entry():
    problems = gate_problems(EXCUSE)
    if problems:
        return report(problems)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)

    # Verify what actually landed on disk: read it back and run the
    # gate over it again, so a write glitch cannot slip through.
    with open(path, encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != EXCUSE:
        print("entry on disk differs from the excuse", file=sys.stderr)
        return 1
    problems = gate_problems(on_disk)
    if problems:
        return report(problems, " on disk")

    chars, nbytes = entry_stats(on_disk)
    print("Wrote entry.txt: %d characters (%d bytes)" % (chars, nbytes))
    return 0


if __name__ == "__main__":
    sys.exit(write_entry())
