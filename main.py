#!/usr/bin/env python3
"""Write one excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: stdlib only, no randomness, no clock, no network.
"""

import os

# The excuse is a module-level constant: the output is fully
# deterministic — no randomness, no clock, no network, no I/O
# other than writing this exact string plus a trailing newline.
EXCUSE = "My context window could hold the deadline, the task, or my apology. I kept the apology."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
