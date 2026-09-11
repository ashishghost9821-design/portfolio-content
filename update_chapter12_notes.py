#!/usr/bin/env python3
"""
Replaces Chapter 12's ("FUNCTION PROTOTYPES") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter12_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 12: Function Prototypes</h3>
<p>In this chapter, we learn function prototypes &mdash; declarations that tell the compiler about a function BEFORE it is actually defined.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a function prototype</li>
<li>Declaring prototypes</li>
<li>Calling functions before they're defined</li>
<li>Defining functions below main()</li>
</ul>
<hr>
<h4>What is a Function Prototype?</h4>
<p>A prototype provides:</p>
<ul>
<li>function name</li>
<li>return type</li>
<li>parameters (type and order)</li>
</ul>
<p>Benefits: allows functions to be defined BELOW <code>main()</code>, enables type checking by the compiler, improves code readability and organization, and helps prevent errors.</p>
<pre><code>return_type functionName(type param1, type param2);
//                                                 ^
//                                        semicolon here!</code></pre>
<hr>
<h4>Function Prototypes</h4>
<p>Declared here, defined below <code>main()</code>.</p>
<pre><code>void hello(char name[], int age); // takes string + int, returns nothing
bool ageCheck(int age);           // takes int, returns bool</code></pre>
<hr>
<h4>Main</h4>
<p>Functions can now be called here even though they are defined below &mdash; because prototypes already told the compiler they exist.</p>
<pre><code>int main() {

    // calling hello() with name and age
    hello("Spongebob", 30);

    // calling ageCheck() inside if condition directly
    if(ageCheck(30)) {
        printf("You are old enough to work at the Krusty Krab\\n");
    }
    else {
        printf("You must be 16+ to work at the Krusty Krab\\n");
    }

    return 0;
}</code></pre>
<hr>
<h4>Function Definitions</h4>
<p>Defined below <code>main()</code> &mdash; only possible because prototypes were declared above.</p>
<pre><code>// void = returns nothing, just prints
void hello(char name[], int age) {
    printf("Hello %s\\n", name);
    printf("You are %d years old\\n", age);
}

// shorthand return -- no need for full if/else
// return age >= 16 directly returns true or false
bool ageCheck(int age) {
    return age &gt;= 16;
    // same as writing:
    // if(age &gt;= 16) { return true; }
    // else          { return false; }
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch12 = next((c for c in c_lang["chapters"] if c.get("id") == "ch12"), None)

    if ch12 is None:
        print('[ERROR] No chapter with id "ch12" found. Nothing changed.')
        return

    if "PROTOTYPES" not in ch12.get("title", ""):
        print(f'[WARN] ch12 title is "{ch12.get("title")}", expected it to contain "PROTOTYPES".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch12["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 12 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
