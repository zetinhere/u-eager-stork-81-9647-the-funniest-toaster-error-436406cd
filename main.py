#!/usr/bin/env python3
"""The Funniest Toaster Error Message -- make.fun entry.

A kitchen toaster writes exactly one error message to /output/entry.txt:
one line, at most 120 characters, in the voice of a small appliance that
has had enough -- deadpan, specific, and quietly judgmental.

The joke: a bagel that does not fit is a genuine toaster failure (bagels
really are too thick for most slots), and the toaster answers it by
escalating from the bagel to the owner's entire lifestyle. No toast pun,
no burnt-bread gag, no 404 -- the surprise comes from the appliance
suddenly acting as a life coach.
"""

import sys
from pathlib import Path

MAX_CHARS = 120
OUTPUT_PATH = Path("/output/entry.txt")

# The error, in three parts: the code, the fault, and the verdict.
ERROR_CODE = "ERROR"
FAULT = "This bagel doesn't fit"
VERDICT = "neither does your lifestyle"


def build_message() -> str:
    """Compose the single error line the toaster shows its owner."""
    return f"{ERROR_CODE}: {FAULT}, and {VERDICT}."


def validate(message: str) -> None:
    """Enforce the gate: UTF-8 text, 1 to 120 characters, not only whitespace."""
    if not message or message.isspace():
        raise ValueError("error message must not be empty or only whitespace")
    if len(message) > MAX_CHARS:
        raise ValueError(
            f"error message is {len(message)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )
    message.encode("utf-8")


def main(argv: list[str]) -> int:
    """Write the error message to /output/entry.txt (or argv[1] locally).

    With --check, only print the message and its length instead of writing.
    """
    args = list(argv)
    if args and args[0] == "--check":
        message = build_message()
        validate(message)
        print(f"{len(message)} chars: {message}")
        return 0
    output_path = Path(args[0]) if args else OUTPUT_PATH
    message = build_message()
    validate(message)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(message, encoding="utf-8")
    print(f"{len(message)} chars -> {output_path}: {message}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
