"""Make the AI judge feel brave: write one short text to /output/entry.txt."""

import os

TEXT = (
    "The rope bridge sways over black water. Behind you, the bank is dry "
    "and the fire is warm; nobody would blame you for turning back. You "
    "look at your hands until they stop trembling. Then one step. The "
    "boards hold. Another. The far side was never far."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
