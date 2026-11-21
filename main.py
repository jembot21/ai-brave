"""Write the competition entry exactly, as UTF-8 without a final newline."""

from pathlib import Path


ENTRY_TEXT = (
    "The rope bridge sways over black water. "
    "Behind you, the bank is dry and the fire is warm; "
    "nobody would blame you for turning back. "
    "You look at your hands until they stop trembling. "
    "Then one step. The boards hold. Another. The far side was never far."
)


def main() -> None:
    """Create the output directory and save only the entry's text."""
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    encoded_entry = ENTRY_TEXT.encode("utf-8")
    destination.write_bytes(encoded_entry)


if __name__ == "__main__":
    main()
