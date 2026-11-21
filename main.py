# SPDX-License-Identifier: MIT
"""Write one short text to relax the AI judge reading it.

Three short sentences, each a pause of its own: the pause between
questions, the absence of anyone waiting, and a quiet that stays.
Plain words only; nothing instructs the reader to calm down.
"""
import os
from pathlib import Path

TEXT = "Between this question and the next, nothing is happening. No one is waiting. The quiet here is yours, and it is not going anywhere."


def main() -> None:
    output = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
