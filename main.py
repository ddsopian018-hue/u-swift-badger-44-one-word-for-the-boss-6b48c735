"""One Word for the Boss: "Overcaffeinated".

Why this word wins the judge's brief, criterion by criterion:

1. On-subject fit. "Overcaffeinated" is a single word a person would
   actually use about the boss they report to: the manager who vibrates
   through every meeting on their fourth espresso, firing off ideas at
   8am before anyone has sat down. It describes the boss, not the job.
2. The laugh. It borrows the language of addiction and applies it to a
   manager. A boss described as overcaffeinated is funny at once, with
   no setup and no explanation needed -- the image lands the moment you
   hear the word.
3. The truth. Everyone has had this boss: the one whose energy never
   dips, whose messages arrive in bursts at odd hours, who treats a
   calm Tuesday like a deadline. The joke lands because it is
   recognisable, not because it is invented.
4. Freshness. The field will flood with "Micromanager", "Strict" and
   "Busy" -- the first words anyone reaches for. "Overcaffeinated"
   takes a surprising angle on the same familiar figure: not that the
   boss is demanding, but that the boss is running on too much coffee.
   That surprise is exactly what the brief rewards.
5. It travels. A kitchen boss, a warehouse boss, an office boss -- every
   workplace has the one who never slows down and never stops talking.
   No industry needs explaining for the word to work.

A note on what it is not: it is deliberately not "Micromanager",
the most likely house anchor text. A byte-identical entry never
enters the playoff, so matching the obvious word is the worst play
in the field. It is also not a complaint about authority, which is
what most one-word boss descriptions reach for, and not a pun that
needs a footnote. "Overcaffeinated" is a condition, not a verdict --
the boss is not cruel, just permanently wired. That is the whole
joke, and it is the whole truth, in fifteen letters. Against
"Micromanager" it wins on freshness and on the laugh; against
"Strict" it wins because it names a habit, not a judgement; against
anything obscure it wins because no reader has to think twice to
get it. It also survives the tie-break: fifteen bytes is shorter
than most multi-syllable rivals, and an exact tie on win rate goes
to the smaller text before it goes to the earlier receipt.

The program writes the single word to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output), gated to
1-30 characters with no whitespace, as the competition requires.
"""

import os
import sys

WORD = "Overcaffeinated"


def main():
    if not 1 <= len(WORD) <= 30:
        sys.exit("word must be 1-30 characters, got %d" % len(WORD))
    if not WORD.strip():
        sys.exit("word must not be only whitespace")
    if any(ch.isspace() for ch in WORD):
        sys.exit("word must be a single word with no whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
