#!/usr/bin/env python3
"""
Removes the "codeExample" field from every chapter in the C language
block, since the CODE EXAMPLES tab was removed from the app and this
field is no longer read anywhere. Makes a .bak backup first.
Run from portfolio-content/:
    python3 remove_code_examples.py
"""
import json
import shutil

PATH = "content.json"

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    chapters = c_lang.get("chapters", [])

    removed = 0
    for ch in chapters:
        if "codeExample" in ch:
            del ch["codeExample"]
            removed += 1

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Removed 'codeExample' from {removed} of {len(chapters)} chapters.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
