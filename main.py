import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """The machine asked my daughter which cup she wanted.
It had weighed them both — the red holds more,
the blue keeps the milk colder, longer — and waited
for her reason, patient as only a machine can be.

She took the red one. 'Why red?' it asked.
She shrugged. 'Because it's red.'
It tried again: 'But the blue is better.'
She drank from the red, milk on her lip, and said,
'The blue is better. The red is mine.'"""

# Competition gate: the entry must hold 1-1000 Unicode code points and at
# least one character that is not white space. Fail loudly here rather
# than shipping an invalid entry.
assert POEM.strip(), "poem must not be blank"
assert 1 <= len(POEM) <= 1000, f"poem is {len(POEM)} chars, gate allows 1-1000"

out_dir = Path(OUTPUT_DIR)
out_dir.mkdir(parents=True, exist_ok=True)
out_dir.joinpath("entry.txt").write_text(POEM, encoding="utf-8")
