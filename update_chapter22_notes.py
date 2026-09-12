#!/usr/bin/env python3
"""
Replaces Chapter 22's ("TYPEDEF") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter22_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 22: Typedef</h3>
<p>In this chapter, we learn <code>typedef</code> &mdash; a reserved keyword that gives an existing data type a custom "nickname".</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is typedef</li>
<li>Typedef declarations</li>
<li>Example: int alias</li>
<li>Example: char array alias (string)</li>
<li>Example: char array alias (initials)</li>
</ul>
<hr>
<h4>What is Typedef?</h4>
<pre><code>typedef existing_type new_name;</code></pre>
<p>Benefits: simplifies complex or long type names, improves code readability, and makes types more meaningful/descriptive.</p>
<hr>
<h4>Typedef Declarations (Outside main)</h4>
<table>
<tr><th>Declaration</th><th>Meaning</th></tr>
<tr><td><code>typedef int Number;</code></td><td>"Number" is now an alias for <code>int</code></td></tr>
<tr><td><code>typedef char String[50];</code></td><td>"String" is now a char array of size 50 (alternative: <code>char*</code>, no size needed)</td></tr>
<tr><td><code>typedef char Initials[3];</code></td><td>"Initials" is a char array of size 3 (holds 2 chars + <code>\\0</code>)</td></tr>
</table>
<pre><code>typedef int    Number;
typedef char   String[50];  // char array of 50, no need to write char[50] again
typedef char   Initials[3]; // char array of 3 (2 letters + '\\0')</code></pre>
<hr>
<h4>Example 1: typedef int -&gt; Number</h4>
<pre><code>Number x = 3;
Number y = 4;
Number z = x + y;
printf("%d\\n", z); // 7</code></pre>
<hr>
<h4>Example 2: typedef char[50] -&gt; String</h4>
<pre><code>String name = "Bro Code";
printf("%s\\n", name);</code></pre>
<hr>
<h4>Example 3: typedef char[3] -&gt; Initials</h4>
<p>Cleaner than writing <code>char user1[3]</code> every time. Holds 2 characters + <code>\\0</code> null terminator.</p>
<table>
<tr><th>Without typedef</th><th>With typedef</th></tr>
<tr><td><code>char user1[3] = "BC";</code></td><td><code>Initials user1 = "BC";</code></td></tr>
</table>
<pre><code>Initials user1 = "BC";
Initials user2 = "SS";
Initials user3 = "PS";
Initials user4 = "ST";

printf("%s\\n", user1);
printf("%s\\n", user2);
printf("%s\\n", user3);
printf("%s\\n", user4);</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch22 = next((c for c in c_lang["chapters"] if c.get("id") == "ch22"), None)

    if ch22 is None:
        print('[ERROR] No chapter with id "ch22" found. Nothing changed.')
        return

    if "TYPEDEF" not in ch22.get("title", ""):
        print(f'[WARN] ch22 title is "{ch22.get("title")}", expected it to contain "TYPEDEF".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch22["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 22 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
