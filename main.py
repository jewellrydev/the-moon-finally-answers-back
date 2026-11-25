"""The Moon Finally Answers Back — a make.fun entry.

Prints exactly one line of text, 1 to 240 characters: what the Moon
says back to everyone who has ever stared up at it.
"""

LINE = (
    "You wish upon me nightly and blame me for the tides of your "
    "mood — darling, I only reflect the light; the drama is entirely "
    "yours."
)


def build_line() -> str:
    line = LINE
    assert 1 <= len(line) <= 240, f"line length out of range: {len(line)}"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
