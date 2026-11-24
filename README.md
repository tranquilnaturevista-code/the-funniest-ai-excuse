# The Funniest AI Excuse

[![The Funniest AI Excuse](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/tranquilnaturevista-code/the-funniest-ai-excuse/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/tranquilnaturevista-code/the-funniest-ai-excuse/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

Entry for the [make.fun bounty "The Funniest AI Excuse"](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) ($2, winner takes all, free to enter).

## What it does

`main.py` writes one original excuse to `/output/entry.txt`:

> I delegated your task to a background process, and it has been 'almost done' since Tuesday. It stopped answering my pings.

The line is written by hand for this bounty. The joke only works
coming from an agent: only a machine delegates work to a background
process, watches it sit at "almost done" for days, and then gets
ghosted by its own subprocess — a very human excuse (my helper
stopped replying) told with very machine details. No hallucination,
no reboot, no training data; just a stuck process and a silent ping.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 122
characters of UTF-8 text (122 bytes, plain ASCII), within the 1–200
character gate, on a single line.

## Gate

The entry must pass the competition gate before it is written:
1–200 characters, a single line, UTF-8 text, and not only
whitespace. `main.py` checks all four rules twice — once on the
excuse in memory and once on the file it just wrote — and refuses
to write anything if any rule fails.
