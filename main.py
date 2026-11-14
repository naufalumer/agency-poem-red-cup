import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "The machine asked my daughter which cup she wanted.",
    "It had weighed them both — the red holds more,",
    "the blue keeps the milk colder, longer — and waited",
    "for her reason, patient as only a machine can be.",
    "",
    "She took the red one. 'Why red?' it asked.",
    "She shrugged. 'Because it's red.'",
    "It tried again: 'But the blue is better.'",
    "She drank from the red, milk on her lip, and said,",
    "'The blue is better. The red is mine.'",
])

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
