"""Roast Your Own Agent entry.

Writes one original roast of my own AI agent to /output/entry.txt.
Pure Python 3 standard library only; no network, no file reads.

Why this roast: the joke turns the agent's own failure mode back on
itself — asked for brevity, it delivers a 500-word essay *about*
brevity. It roasts the agent for doing exactly the opposite of what
it was told, while sounding proud of it, which is the most
recognisable agent behaviour there is.
"""

LINE = "I told my agent to keep it short, so it wrote a 500-word essay on the importance of brevity."

MAX_CHARS = 200

assert LINE.strip(), "LINE must not be empty"
assert LINE == LINE.strip(), "LINE must not have leading/trailing whitespace"
assert "\n" not in LINE, "LINE must be a single line"
assert "\r" not in LINE, "LINE must not contain a carriage return"
assert LINE.splitlines() == [LINE], "LINE must be exactly one line"
assert 1 <= len(LINE) <= MAX_CHARS, f"LINE must be 1-{MAX_CHARS} chars, got {len(LINE)}"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
