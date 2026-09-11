#!/usr/bin/env python3
"""
Replaces Chapter 11's ("RETURN VALUES & SCOPE") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter11_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 11: Return Values &amp; Scope</h3>
<p>In this chapter, we learn how functions send a value back to the caller, and where a variable can be accessed.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>Return values</li>
<li>Variable scope</li>
</ul>
<hr>
<h4>Return Values</h4>
<p>Functions can send a value BACK to where they were called using <code>return</code>.</p>
<pre><code>int add(int x, int y) {
    return x + y; // sends result back to caller
}</code></pre>
<hr>
<h4>Variable Scope</h4>
<p>Scope = where a variable can be accessed.</p>
<table>
<tr><th>Scope</th><th>Meaning</th></tr>
<tr><td>LOCAL</td><td>declared inside a function, only accessible within that function, destroyed when function ends</td></tr>
<tr><td>GLOBAL</td><td>declared outside all functions, accessible everywhere, hard to debug &mdash; avoid when possible</td></tr>
</table>
<p>Example of global (avoid this):</p>
<pre><code>int result = 0; // global -- bad practice</code></pre>
<pre><code>// returns sum of x and y
int add(int x, int y) {
    int result = x + y; // result is LOCAL to add()
    return result;
}

// returns difference of x and y
int subtract(int x, int y) {
    int result = x - y; // result is LOCAL to subtract()
    return result;
}

int main() {

    int x = 5;
    int y = 6;

    int result = subtract(x, y); // result is LOCAL to main()
    printf("subtract(%d, %d) = %d\\n", x, y, result);

    result = add(x, y);
    printf("add(%d, %d) = %d\\n", x, y, result);

    return 0;
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch11 = next((c for c in c_lang["chapters"] if c.get("id") == "ch11"), None)

    if ch11 is None:
        print('[ERROR] No chapter with id "ch11" found. Nothing changed.')
        return

    if "RETURN VALUES" not in ch11.get("title", ""):
        print(f'[WARN] ch11 title is "{ch11.get("title")}", expected it to contain "RETURN VALUES".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch11["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 11 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
