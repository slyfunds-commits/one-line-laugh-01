#!/usr/bin/env python3
"""The One-Line Laugh — round 1 entry: "Five Alarms".

Judge criteria, most important first (RULES.txt, verbatim order):
1. one funny line of at most 200 characters on any subject;
2. a real surprise at the end, a turn the reader did not see coming
   that still makes sense once it arrives;
3. an everyday truth people recognise;
4. economical, every word earning its place, nothing to explain the joke;
5. fresh rather than a line the reader has heard many times before.

The line: three beats (set five alarms -> snooze all five -> the
relationship built on lies). The last beat reframes the first two:
it was never about the alarms, it is about a dishonest relationship
with the clock. Universal, concrete, ends on the punchline word.
"""

import os

LINE = "I set five alarms every morning, snooze all five, and my alarm clock and I still have a relationship built entirely on lies."


def main():
    # Gate self-check: one sentence, at most 200 characters.
    assert LINE.count(".") == 1, "entry must be a single sentence"
    assert len(LINE) <= 200, "entry must be at most 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
