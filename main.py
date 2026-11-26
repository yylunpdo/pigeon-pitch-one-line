"""Pigeon Pitch, One Line.

Writes one line (at most 200 characters, English): the elevator pitch
a city pigeon gives to investors for its startup.

Standard library only. Deterministic: the same bytes on every run.
Output goes to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
"""

import os

PITCH = (
    "I'm a city pigeon. My startup sells premium statue perches by "
    "subscription \u2014 zero churn, 40,000 co-founders already roosting "
    "on every monument. Seed round: breadcrumbs only."
)


def main() -> None:
    pitch = PITCH.strip()
    assert pitch, "pitch must not be empty"
    assert "\n" not in pitch, "pitch must be a single line"
    assert len(pitch) <= 200, "pitch exceeds 200 characters: %d" % len(pitch)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(pitch)


if __name__ == "__main__":
    main()
