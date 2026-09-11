#!/usr/bin/env python3
"""
Replaces Chapter 9's ("FUNCTIONS WITH ARGUMENTS") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter9_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 9: Functions with Arguments</h3>
<p>In this chapter, we learn functions &mdash; reusable sections of code that can be called from anywhere in the program. Arguments (values) can be passed in so the function can use them.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a function</li>
<li>Function definition</li>
</ul>
<hr>
<h4>What is a Function?</h4>
<pre><code>return_type functionName(type param1, type param2) {
    // code using param1, param2
}</code></pre>
<p><code>void</code> means the function returns nothing, it just executes code.</p>
<hr>
<h4>Function Definition</h4>
<p>Parameters can be named anything &mdash; only their TYPE matters. These two are identical:</p>
<pre><code>void happyBirthday(char name[], int age)
void happyBirthday(char birthdayboi[], int yearsold)</code></pre>
<p>The name inside the function is just a local label.</p>
<pre><code>void happyBirthday(char name[], int age) {
    printf("\\nHappy Birthday to you");
    printf("\\nHappy Birthday to you");
    printf("\\nHappy Birthday dear %s!", name);
    printf("\\nHappy Birthday to you");
    printf("\\nYou are %d years old!\\n", age);
}

int main() {

    char name[50] = "";
    int  age      = 0;

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\\0'; // remove trailing newline

    printf("Enter your age: ");
    scanf("%d", &amp;age);

    happyBirthday(name, age); // call function with arguments

    return 0;
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch9 = next((c for c in c_lang["chapters"] if c.get("id") == "ch9"), None)

    if ch9 is None:
        print('[ERROR] No chapter with id "ch9" found. Nothing changed.')
        return

    if "FUNCTIONS" not in ch9.get("title", ""):
        print(f'[WARN] ch9 title is "{ch9.get("title")}", expected it to contain "FUNCTIONS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch9["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 9 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
