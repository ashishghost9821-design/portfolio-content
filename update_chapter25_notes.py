#!/usr/bin/env python3
"""
Replaces Chapter 25's ("ARRAY OF STRUCTS") notes field with the
interlaced explanation + code-block format, plus one added example.
Makes a .bak backup first. Run from portfolio-content/:
    python3 update_chapter25_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 25: Array of Structs</h3>
<p>In this chapter, we learn arrays of structs &mdash; an array where each element is a struct. Helps organize and group together related data.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is an array of structs</li>
<li>Example: defining and looping through cars</li>
<li>Example: filtering the array</li>
</ul>
<hr>
<h4>What is an Array of Structs?</h4>
<pre><code>TypeName arrayName[] = {{...}, {...}, {...}};</code></pre>
<p>Accessing members: <code>arrayName[index].member</code>, e.g. <code>cars[0].model</code> is the first car's model, <code>cars[1].year</code> is the second car's year.</p>
<p><code>sizeof</code> trick to get the count automatically: <code>sizeof(cars) / sizeof(cars[0])</code> = number of structs.</p>
<pre><code>typedef struct {
    char model[25];
    int  year;
    int  price;
} Car;</code></pre>
<hr>
<h4>Example: Defining and Looping Through Cars</h4>
<p>Each <code>{}</code> is one Car struct &mdash; must match member order: <code>{model, year, price}</code>.</p>
<pre><code>Car cars[] = {{"Mustang",    2025, 32000},
              {"Corvette",   2026, 68000},
              {"Challenger", 2024, 29000}};

// get total number of cars automatically
int number = sizeof(cars) / sizeof(cars[0]);

// loop through each Car struct and print its members
for(int i = 0; i &lt; number; i++) {
    printf("%s %d $%d\\n", cars[i].model,
                           cars[i].year,
                           cars[i].price);
}</code></pre>
<hr>
<h4>Example: Filtering the Array</h4>
<p>A common next step &mdash; loop through and only act on structs matching a condition, e.g. find cars under $30,000:</p>
<pre><code>int budget = 30000;

for(int i = 0; i &lt; number; i++) {
    if(cars[i].price &lt; budget) {
        printf("Within budget: %s ($%d)\\n", cars[i].model, cars[i].price);
    }
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch25 = next((c for c in c_lang["chapters"] if c.get("id") == "ch25"), None)

    if ch25 is None:
        print('[ERROR] No chapter with id "ch25" found. Nothing changed.')
        return

    if "ARRAY OF STRUCTS" not in ch25.get("title", ""):
        print(f'[WARN] ch25 title is "{ch25.get("title")}", expected it to contain "ARRAY OF STRUCTS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch25["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 25 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
