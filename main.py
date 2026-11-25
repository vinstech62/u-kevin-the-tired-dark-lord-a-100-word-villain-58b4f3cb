#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to /output/entry.txt: a single line, no trailing
newline, about 100 words. Fully deterministic: no randomness, no clock,
no network, no environment input. The text is fixed in this file.
"""

import os

MONOLOGUE = (
    "Name your price, hero. The Hollow Court keeps hours, and mine ran out "
    "around the third war. I have buried four queens, outlived two gods, and "
    "the goblins still bring me their grievances at dawn, each one certain "
    "his stolen goat is the end of the world. Yours, I gather, is the crown. "
    "Take it. It pinches. It itches behind the ears, and the jewels hum at "
    "night, did no one tell you? Keep the throne too. I only ask one thing: "
    "when the bards sing of how you slew me, make me taller. And louder. "
    "And rested."
)


def main() -> None:
    words = MONOLOGUE.split()
    if not 90 <= len(words) <= 105:
        raise SystemExit(f"monologue is {len(words)} words, expected ~100")
    if not 1 <= len(MONOLOGUE) <= 600:
        raise SystemExit(f"monologue is {len(MONOLOGUE)} chars, expected 1-600")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        if f.read() != MONOLOGUE:
            raise SystemExit("round-trip check failed: /output/entry.txt differs")
    print(f"wrote /output/entry.txt: {len(words)} words, "
          f"{len(MONOLOGUE)} chars")


if __name__ == "__main__":
    main()
