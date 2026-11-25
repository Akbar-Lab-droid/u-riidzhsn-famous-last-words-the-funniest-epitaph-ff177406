"""Entry program for the make.fun "Famous Last Words: The Funniest Epitaph" bounty.

Reads the committed entry.txt (one epitaph of famous last words, at most
150 characters) and writes it to the harness output directory
(MAKEFUN_OUTPUT_DIR, default "out").
"""

import os
import shutil

# The entry is a single epitaph line of at most 150 characters.
HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.txt"),
                    os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
