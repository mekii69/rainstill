"""Write one invented word and its definition to /output/entry.txt."""

import os

ENTRY = "rainstill: the quiet, contented calm of being warm indoors with nowhere to go while rain falls outside."


def main():
    # Sealed gate bounds: 1 to 140 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry out of bounds"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
