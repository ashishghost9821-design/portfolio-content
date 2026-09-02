import json, re, glob

with open('content.json') as f:
    data = json.load(f)

c_lang = next(l for l in data['languages'] if l['name'] == 'C')

def get_title(text, fallback):
    m = re.search(r'C PROGRAMMING\s*-\s*(.+)', text)
    if m:
        return m.group(1).strip().rstrip('*').strip()
    return fallback

chapters = []
for i, fp in enumerate(sorted(glob.glob('chapter*.c')), start=1):
    code = open(fp).read()
    title = get_title(code, f"Chapter {i}")
    chapters.append({
        "id": f"ch{i}",
        "title": f"Chapter {i}: {title}",
        "desc": f"Notes and examples on {title.lower()}.",
        "notes": f"<p>See code example below for details on {title.lower()}.</p>",
        "codeExample": code
    })

projects = []
for i, fp in enumerate(sorted(glob.glob('project*.c')), start=1):
    code = open(fp).read()
    title = get_title(code, f"Project {i}")
    projects.append({
        "id": f"project{i:02d}",
        "num": f"{i}.",
        "title": title,
        "icon": "🧩",
        "desc": f"A program demonstrating {title.lower()}.",
        "difficulty": "Beginner",
        "diffColor": "#8DF749",
        "steps": [],
        "code": code
    })

c_lang['chapters'] = chapters
c_lang['projects'] = projects

with open('content.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(chapters)} chapters and {len(projects)} projects.")
