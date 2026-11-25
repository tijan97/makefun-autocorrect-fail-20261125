import os

ENTRY = 'a text to a crush meant to say "wanna grab coffee?" that autocorrect turned into "wanna grab a coffin?" \u2014 and now I\'m blocked.'

def main():
    # Gate validation (mirrors the scorer gate): 1-199 chars, not only whitespace, single line.
    if not (1 <= len(ENTRY) <= 199):
        raise SystemExit(f"entry length {len(ENTRY)} outside 1-199")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
