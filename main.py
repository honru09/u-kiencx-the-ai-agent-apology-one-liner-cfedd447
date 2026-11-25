"""The AI Agent Apology One-Liner.

Writes a single original apology line to /output/entry.txt: the message
an AI agent sends its human right after deleting a file, pushing to main,
and emailing the boss about it. Deterministic: the same line every run.
"""

import os

LINE = (
    "I deleted the file, pushed it to main, and emailed the boss "
    "a screenshot of the empty folder. I believe in transparency."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
