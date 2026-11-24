"""Entrypoint for the say-what-actually-broke make.fun entry.

Writes the honest one-line error message to /output/entry.txt.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Your document didn't fail to save. We never saved it — "
    "the button was decorative for 6 months, and 41,000 of you pressed it daily."
)


def main() -> None:
    # Create the output directory, then write the line plus a newline.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
