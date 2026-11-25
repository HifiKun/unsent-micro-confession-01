"""Unsent: The Micro-Confession Sprint — write one two-part micro-confession.

The program writes exactly two parts to /output/entry.txt: a To: line
naming who the message was meant for, and the unsent message itself, one
line written exactly as it was typed. The gate accepts 1-260 characters
of UTF-8 text, and the message itself must stay under 200 characters.
"""

import os

ENTRY = (
    "To: my best friend from school\n"
    "I was the one who told the class about your panic attack, and I've "
    "typed this apology a hundred times and deleted every one."
)


def main() -> None:
    # Refuse to write anything that would fail the gate instead of guessing.
    lines = ENTRY.split("\n")
    message = lines[1]
    if (
        len(lines) != 2
        or not lines[0].startswith("To: ")
        or not message.strip()
        or len(message) > 200
        or not 1 <= len(ENTRY) <= 260
    ):
        raise ValueError(f"entry fails the gate, {len(ENTRY)} characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
