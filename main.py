"""Two Days of Quiet Dread.

A program that writes one code review comment to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR when set, for local runs): a single line that
approves a pull request while carrying quiet existential dread.
Standard library only, no network, deterministic: the same bytes on
every run.

Why this line (independent review, consultation #151, kept the line):
"Approved. Somewhere in this diff is the last line of code I will ever
fully understand." It opens with an unambiguous approval, its dread is
the reviewer's own comprehension running out (the laugh comes from the
dread itself, not a bolted-on joke), it stays flat and understated, it
reads like a tired engineer pasting before clicking approve, and its
turn — understanding as a depleting resource — is fresh. Rejected
alternatives: "the diff is clean, the future is not..." (stock "not in
scope" trope); "the pipeline is green, the sun is also still up..."
(whimsical, cosmic rather than personal); "the next person to read it
will be me, older, in the same chair" (poignant more than funny).
"""

import os

COMMENT = (
    "Approved. Somewhere in this diff is the last line of code "
    "I will ever fully understand."
)

# The gate allows 1 to 140 characters on a single line: refuse to write
# a line the judge would never see.
if not 1 <= len(COMMENT) <= 140:
    raise SystemExit(
        f"comment is {len(COMMENT)} characters, outside the 1-140 gate"
    )
if "\n" in COMMENT or COMMENT.strip() == "":
    raise SystemExit("comment must be a single non-blank line")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(COMMENT + "\n")
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must hold exactly the comment.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != COMMENT + "\n":
        raise SystemExit("entry.txt does not match the approved comment")


if __name__ == "__main__":
    main()
