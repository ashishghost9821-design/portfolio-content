#!/usr/bin/env python3
"""
Replaces Chapter 23's ("ENUM") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter23_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 23: Enum</h3>
<p>In this chapter, we learn <code>enum</code> &mdash; a user-defined data type that consists of a set of named integer constants.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is an enum</li>
<li>Example: enum with custom start value</li>
<li>Example: typedef enum for status codes</li>
<li>Using enums with functions and switch</li>
</ul>
<hr>
<h4>What is an Enum?</h4>
<p>Benefit: replaces plain numbers with readable names so code is easier to understand.</p>
<pre><code>enum Name { VALUE1, VALUE2, VALUE3 };</code></pre>
<p>By default, values start at 0 and increment by 1: <code>VALUE1 = 0, VALUE2 = 1, VALUE3 = 2</code> ... You can also assign custom values manually: <code>enum Day { SUNDAY = 1, MONDAY = 2, ... }</code>.</p>
<table>
<tr><th>Way</th><th>Style</th></tr>
<tr><td>Regular enum</td><td>must write "enum Day" each time: <code>enum Day { SUNDAY, MONDAY }; enum Day today = SUNDAY;</code></td></tr>
<tr><td>typedef enum</td><td>cleaner, no need to repeat "enum": <code>typedef enum { SUNDAY, MONDAY } Day; Day today = SUNDAY;</code></td></tr>
</table>
<hr>
<h4>Example 1: Enum with Custom Start Value</h4>
<p>Adding "Day" after the closing <code>}</code> makes "Day" a type name via <code>typedef</code> &mdash; without <code>typedef</code>, it would just create a variable named Day, not a type.</p>
<pre><code>typedef enum {
    SUNDAY    = 1,
    MONDAY    = 2,
    TUESDAY   = 3,
    WEDNESDAY = 4,
    THURSDAY  = 5,
    FRIDAY    = 6,
    SATURDAY  = 7
} Day;</code></pre>
<hr>
<h4>Example 2: Typedef Enum for Status Codes</h4>
<p>Default values: <code>SUCCESS = 0, FAILURE = 1, PENDING = 2</code> &mdash; much more readable than using raw numbers 0, 1, 2.</p>
<pre><code>typedef enum {
    SUCCESS,  // = 0
    FAILURE,  // = 1
    PENDING   // = 2
} Status;</code></pre>
<hr>
<h4>Function Prototype</h4>
<p>A function parameter must have a NAME (<code>status</code>), not just a type.</p>
<pre><code>// WRONG: void connectStatus(Status);
// RIGHT:
void connectStatus(Status status);</code></pre>
<hr>
<h4>Main</h4>
<pre><code>int main() {

    // --- EXAMPLE 1: Day enum ---
    Day today = SUNDAY;

    if(today == SUNDAY || today == SATURDAY) {
        printf("It's the weekend!\\n");
    }
    else {
        printf("It's a weekday.\\n");
    }

    // --- EXAMPLE 2: Status enum ---
    Status status = SUCCESS;
    connectStatus(status);

    status = PENDING;
    connectStatus(status);

    status = FAILURE;
    connectStatus(status);

    return 0;
}</code></pre>
<hr>
<h4>Function Definition</h4>
<p><code>switch(status)</code> must be passed the variable &mdash; an empty <code>switch()</code> is a compiler error since there's nothing to check.</p>
<pre><code>void connectStatus(Status status) {
    switch(status) {
        case SUCCESS:
            printf("Connection was successful\\n");
            break;
        case FAILURE:
            printf("Could not connect\\n");
            break;
        case PENDING:
            printf("Connecting....\\n");
            break;
    }
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch23 = next((c for c in c_lang["chapters"] if c.get("id") == "ch23"), None)

    if ch23 is None:
        print('[ERROR] No chapter with id "ch23" found. Nothing changed.')
        return

    if "ENUM" not in ch23.get("title", ""):
        print(f'[WARN] ch23 title is "{ch23.get("title")}", expected it to contain "ENUM".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch23["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 23 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
