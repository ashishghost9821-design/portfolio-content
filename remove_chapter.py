import json

with open('content.json', 'r') as f:
    data = json.load(f)

# Find C language
c_lang = None
for lang in data['languages']:
    if lang['name'] == 'C':
        c_lang = lang
        break

if c_lang is None:
    print("C not found")
    exit(1)

# Remove the chapter with title "Chapter 1: Getting Started with C"
c_lang['chapters'] = [ch for ch in c_lang['chapters'] if ch['title'] != "Chapter 1: Getting Started with C"]

with open('content.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✅ Removed auto‑added chapter.")

