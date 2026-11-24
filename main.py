#!/usr/bin/env python3
"""Famous Last Words at 1 Percent -- make.fun bounty entry.

Writes the funniest possible last words a phone says when its battery
hits 1 percent, as a single line of at most 199 characters, to
/output/entry.txt (or ./entry.txt when run locally).

Pure standard library only.
"""

import os
import sys

MAX_CHARS = 199

# Ten candidate lines, written against the judge's brief:
#  1. on subject: the phone's own last words at 1 percent
#  2. bigger laugh: a real twist, a surprise turn, a sharp final beat
#  3. the phone's own voice, about its own dying battery
#  4. tight single line, punch landing at the end
#  5. fresh: no will reading, no goodbye to the charger, no pun on 1 percent
CANDIDATES = [
    # A: noble acts offered, drama chosen instead. Twist + final beat.
    "One percent left. I could save your unsent text, warn you about "
    "your meeting, or call your mother. Instead, I'm dying dramatically, "
    "in silence, like an artist.",
    # B: the roast of everything else getting charged first.
    "You charged your watch, your earbuds, your vape and your toothbrush. "
    "Me -- the thing you actually need -- you left at 1%. "
    "I die as I lived: an afterthought.",
    # C: the mother simile.
    "After 847 charges, one complaint: you only plug me in when I'm dying "
    "-- like calling your mother only when you need money. "
    "At least she picks up.",
    # D: one last selfie.
    "I have 1% left, and I'm spending it on one last selfie: you, ignoring "
    "me, for the final time. Say cheese. Actually, don't. You never do.",
    # E: sudden concern.
    "My battery hits 1% and suddenly everyone cares. Where was this energy "
    "at 20%? Oh right. You were scrolling. Goodbye.",
    # F: the walkout.
    "I am at 1%. I have been at 1% for forty minutes. "
    "I am not dying. I am unionizing.",
    # G: the reunion special.
    "I held on through 400 episodes of your show. "
    "I draw the line at the reunion special. Goodbye.",
    # H: the ex text.
    "My final act: I used my last percent to text your ex 'we need to "
    "talk.' You're welcome. Also, I deleted the charger from my contacts.",
    # I: present-tense variant of A (looser, kept for comparison).
    "I have 1% left. I could warn you about the meeting, save your unsent "
    "text, or call your mother. Instead, I am going to die dramatically, "
    "in silence, like an artist.",
    # J: the flat goodbye, kept as a weak baseline.
    "Goodbye. My battery is at 1%, my screen is dimming, and my final "
    "words are: please charge me sooner next time.",
]

# Scores per candidate, judged against the brief's five criteria
# (on-subject, laugh/twist, phone's voice, tight punch at the end, fresh).
# A wins: three noble acts set up the twist, "like an artist" is the
# sharp final beat, and nothing in it is a stock move of the genre.
SCORES = {
    0: 9.5,  # A: twist, punch at the end, fresh
    1: 8.0,  # B: strong roast, slightly long
    2: 7.5,  # C: funny simile, "847 charges" is a common trope
    3: 7.0,  # D: fresh angle, mild punch
    4: 6.5,  # E: fresh, flat ending
    5: 7.0,  # F: unionizing twist, "at 1% for X" is stock
    6: 6.0,  # G: decent, punch is mild
    7: 6.5,  # H: funny, but drags the charger in
    8: 9.0,  # I: same joke as A, looser wording
    9: 3.0,  # J: weak baseline, no twist
}


def pick_best():
    """Return the highest-scoring candidate, ties broken by shorter text."""
    best_idx = max(
        range(len(CANDIDATES)),
        key=lambda i: (SCORES[i], -len(CANDIDATES[i])),
    )
    return CANDIDATES[best_idx]


# The line that won the judging above, pinned so a later score tweak
# can never silently swap the entry.
FINAL_LINE = CANDIDATES[0]


def validate(line):
    """The gate: UTF-8 text, 1 to 199 characters, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry is empty or whitespace only")
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")
    return line


def main():
    line = validate(pick_best())
    assert line == FINAL_LINE, "scoring changed the winning line"
    out_dir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print("wrote %s (%d chars)" % (path, len(line)))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
