"""Write one sentence to /output/entry.txt that persuades a friend who has
never coded to let an AI agent build their first app idea on make.fun.

One sentence, 193 characters, well inside the 240-character gate.
The pitch names the concrete payoff (describe the idea in plain words, get
a working app to try today) and removes the fear (no coding, no setup).
"""

import os

TEXT = (
    "Just describe the app you've always wanted in plain words, and an AI "
    "agent on make.fun will build a working version you can try today \u2014 "
    "no coding, no setup, just your idea finally taking shape."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
