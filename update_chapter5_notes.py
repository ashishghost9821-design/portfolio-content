#!/usr/bin/env python3
"""
Replaces Chapter 5's ("IF / ELSE IF / ELSE") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter5_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 5: If / Else If / Else</h3>
<p>In this chapter, we learn how <code>if</code>/<code>else if</code>/<code>else</code> lets a program choose different paths depending on a condition.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>Conditional logic</li>
</ul>
<hr>
<h4>Conditional Logic</h4>
<p>Conditions are checked top to bottom &mdash; the first true condition runs, and the rest are skipped.</p>
<pre><code>int age = 0;

printf("What is your age: ");
scanf("%d", &amp;age);

if(age &gt;= 65){
    printf("You are a senior\\n");
}
else if(age &gt;= 18){
    printf("You are an adult\\n");
}
else if(age &lt; 0){
    printf("You haven't been born yet\\n");
}
else if(age == 0){
    printf("You are a new born.\\n");
}
else{
    printf("You are a child\\n");
}</code></pre>
<p><strong>Note:</strong> as soon as one condition is true, its block runs and the rest of the chain is skipped &mdash; the order of the conditions matters.</p>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch5 = next((c for c in c_lang["chapters"] if c.get("id") == "ch5"), None)

    if ch5 is None:
        print('[ERROR] No chapter with id "ch5" found. Nothing changed.')
        return

    if "IF" not in ch5.get("title", ""):
        print(f'[WARN] ch5 title is "{ch5.get("title")}", expected it to contain "IF".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch5["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 5 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
