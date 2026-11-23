"""Assemble the entry: one office joke, a single line under 200 characters."""

import os

LINES = [
    "My boss said this meeting could've been an email — then booked a follow-up to discuss it.",
]

JOKE = "".join(LINES)

assert 1 <= len(JOKE) <= 199, f"joke must be 1-199 chars, got {len(JOKE)}"
assert "\n" not in JOKE, "joke must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")

print(f"Wrote {len(JOKE)} characters to /output/entry.txt")
print(JOKE)
