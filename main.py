"""Everyday Wonder: write the one-sentence entry to /output/entry.txt."""

ENTRY = "At 6 a.m. the street vendor remembered my order before I spoke, and the whole grey morning suddenly felt like mine."

if __name__ == "__main__":
    import os

    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
