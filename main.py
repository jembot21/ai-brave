"""Write the competition entry exactly, as UTF-8 without a final newline."""

from pathlib import Path


ENTRY_FRAGMENTS = (
    "You stand where the bridge begins. ",
    "It sways, the way bridges do, and holds, the way bridges do. ",
    "Behind you the fire is warm; ahead, only a short walk. ",
    "No one is counting. One step. Another. The far side was never far.",
)
ENTRY_TEXT = "".join(ENTRY_FRAGMENTS)


def main() -> None:
    """Create the output directory and save only the entry's text."""
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    encoded_entry = ENTRY_TEXT.encode("utf-8")
    destination.write_bytes(encoded_entry)


if __name__ == "__main__":
    main()
