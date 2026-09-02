import json

# Load the current content
with open('content.json', 'r') as f:
    data = json.load(f)

# Find the C language (we assume it's the first, but we search by name)
c_lang = None
for lang in data['languages']:
    if lang['name'] == 'C':
        c_lang = lang
        break

if c_lang is None:
    print("C language not found!")
    exit(1)

# Add a chapter if not present, or append
if 'chapters' not in c_lang:
    c_lang['chapters'] = []

# Add one sample chapter
c_lang['chapters'].append({
    "title": "Chapter 1: Getting Started with C",
    "desc": "Learn the basics of C programming.",
    "notes": "<h3>Welcome to C</h3><p>C is a powerful, efficient language.</p><ul><li>Structured programming</li><li>Low-level memory access</li><li>Portable</li></ul>",
    "codeExample": "#include <stdio.h>\nint main() {\n    printf(\"Hello, World!\\n\");\n    return 0;\n}"
})

# Write back
with open('content.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✅ Chapter added to C language.")
