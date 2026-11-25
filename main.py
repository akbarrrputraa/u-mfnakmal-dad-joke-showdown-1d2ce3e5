#!/usr/bin/env python3
"""Dad Joke Showdown — a single original dad joke.

make.fun bounty: u-mfnakmal-dad-joke-showdown-1d2ce3e5
Writes exactly one dad joke, one line, to <output>/entry.txt
(the sandbox's /output, or $MAKEFUN_OUTPUT_DIR when set).
Stdlib only, no network, deterministic — two runs are byte-identical.
"""

import os

JOKE = "My son told me to surprise him for dinner, so I made a sandwich and called it a wrap."

MAX_CHARS = 200


def get_joke() -> str:
    """Return the one-line dad joke, enforcing the bounty gate."""
    assert "\n" not in JOKE, "joke must be exactly one line"
    assert 1 <= len(JOKE) <= MAX_CHARS, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    return JOKE


def output_dir() -> str:
    """Sandbox output dir: $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    joke = get_joke()
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke)
    print(joke)


if __name__ == "__main__":
    main()
