import json
import shutil
import os

CONTENT_FILE = "content.json"

def main():
    with open(CONTENT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    shutil.copy(CONTENT_FILE, CONTENT_FILE + ".bak")

    updated = []
    not_found_on_disk = []

    for lang in data.get("languages", []):
        for proj in lang.get("projects", []):
            pid = proj.get("id")
            fname = f"{pid}.c"
            if os.path.exists(fname):
                with open(fname, "r", encoding="utf-8") as f:
                    proj["code"] = f.read()
                updated.append(fname)
            else:
                not_found_on_disk.append(fname)

    with open(CONTENT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Backup saved: {CONTENT_FILE}.bak")
    print(f"Synced {len(updated)} file(s) into content.json: {', '.join(updated)}")
    if not_found_on_disk:
        print(f"Skipped (no .c file found): {', '.join(not_found_on_disk)}")

if __name__ == "__main__":
    main()
