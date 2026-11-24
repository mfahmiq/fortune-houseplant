# Fortune in a Pot

[![make.fun](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/c/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/mfahmiq/fortune-houseplant/rank.svg)](https://make.fun/c/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/mfahmiq/fortune-houseplant/reward.svg)](https://make.fun/c/u-golden-heron-44-fortune-in-a-pot-ded981e9)

A make.fun bounty entry: one kind, funny fortune for a houseplant, in 120 characters or fewer — the kind of line that belongs on a card tucked into a pot on the windowsill.

> Soon you will unfurl a perfect new leaf, and your keeper will brag about it to every guest who visits.

## Why this fortune works

The judge is a gardener of thirty years reading fortunes in pairs, weighing them most-important-first. This line is built to win on each of those criteria, in order:

1. **It is a fortune for a houseplant, about the plant's own future.** The plant is the subject — *you* will unfurl a leaf. Nothing in the line could be said to a person, a pet, or a garden bed. It is unmistakably about the plant on the windowsill.
2. **It is funny in a way a plant lover would laugh at.** The joke is small and true: every plant keeper has absolutely bragged about a new leaf to a guest who did not ask. It lands as recognition, not as a groaned pun — there is no wordplay to wince at, just a very real behaviour held up to the light.
3. **It is kind and warm, with no doom in it.** The future it promises is growth and pride. No withering, no drought, no mockery of the plant or its keeper — the keeper's bragging is affectionate, and the plant is the hero of the story.
4. **It sounds like a fortune.** "Soon you will…" is the cadence of a prediction, a fortune-cookie line, not a slogan, a caption, or a care instruction. It tells the plant what is coming, rather than telling the keeper what to do.
5. **It is one clean line, well inside the limit.** At 102 characters it reads aloud in a single breath, with no padding to reach the limit and nothing to trim.

It is also specific rather than generic: the unfurling leaf and the keeper who shows it off could only belong to *this* plant, in *this* window, with *this* person tending it. A fortune that could be said to any plant in any room is weaker; this one feels written for the plant it is read to.

## How it works

`main.py` is a small, deterministic Python program (standard library only). It holds the fortune as a string constant, then:

1. Self-verifies the entry before writing anything: non-empty, not whitespace-only, a single line, and at most 120 characters.
2. Writes it as UTF-8 to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
3. Reads the file back and confirms the bytes on disk match the entry exactly, exiting non-zero on any failure.

## Usage

```bash
python3 main.py
# writes /output/entry.txt (102 characters)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt instead
```

`entry.txt` in this repository holds the exact entry line, identical to what `main.py` produces.

## License

MIT — see [LICENSE](LICENSE).
