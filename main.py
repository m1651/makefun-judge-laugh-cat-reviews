"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written in the voice of a
house cat about its human, to /output/entry.txt.

The review must be a single line of 1-200 characters. The line below is
141 characters: a deadpan one-star review shape, a specific recognisable
complaint (the food bowl, the laptop keyboard), a feline voice that
measures the human by cat standards, and a sting in the last few words.
"""

import os
import sys

REVIEW = (
    "One star. The food bowl sat empty for eleven whole minutes, so I sat "
    "on his keyboard and deleted his meeting. Would not recommend this human."
)

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from the bounty rules: /output/entry.txt must be UTF-8 text
# of 1 to 200 characters, not only white space, on a single line.
MAX_CHARS = 200


def validate(text: str) -> str:
    """Check the review line against the gate; exit non-zero on failure."""
    line = text.strip()
    if "\n" in line or "\r" in line:
        print("error: review must be a single line", file=sys.stderr)
        sys.exit(1)
    if not line:
        print("error: review must not be empty or only white space",
              file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(f"error: review is {len(line)} characters, over the "
              f"{MAX_CHARS}-character limit", file=sys.stderr)
        sys.exit(1)
    return line


def main() -> None:
    text = validate(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
