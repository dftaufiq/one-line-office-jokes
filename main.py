"""One-line office joke for the make.fun "One-Line Office Jokes" bounty.

Writes one single-line joke about office life to /output/entry.txt
(1-199 UTF-8 characters). No network, no dependencies, no secrets.
"""

import os
import sys

JOKE = "Mark stopped by my desk for a 'quick question' at 10:15, and 40 minutes later I learned his divorce, his boat, and that the question was about fonts."
# Structure (per the 24 Nov 2026 rank analysis of winning one-liners): 2-beat
# setup + reveal in the final clause. Beat 1: the "quick question" that eats
# 40 minutes (divorce, boat). Beat 2 / reveal: the question was about fonts.
# Specific numbers (10:15, 40 minutes) + a named character (Mark).


def main() -> None:
    if not 1 <= len(JOKE) <= 199:
        print(f"error: JOKE must be 1-199 characters, got {len(JOKE)}", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in JOKE or JOKE != JOKE.strip():
        print("error: JOKE must be a single line with no leading/trailing space", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
