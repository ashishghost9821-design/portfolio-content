#!/usr/bin/env python3
"""
Replaces Chapter 13's ("WHILE & DO/WHILE LOOPS") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter13_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 13: While &amp; Do/While Loops</h3>
<p>In this chapter, we learn two loops that repeat code based on a condition, checked at different points.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>While loop</li>
<li>Do/While loop</li>
</ul>
<hr>
<h4>While Loop</h4>
<p>Repeats code WHILE a condition is true. The condition is checked BEFORE entering the loop &mdash; if it's false from the start, the loop never runs even once.</p>
<pre><code>while(condition) {
    // code to repeat
}</code></pre>
<hr>
<h4>Do/While Loop</h4>
<p>Runs the code block FIRST, then checks the condition. Guarantees the loop body runs AT LEAST once.</p>
<pre><code>do {
    // code to repeat
} while(condition);
//                ^
//       semicolon required here!</code></pre>
<hr>
<h4>Do/While Example</h4>
<p>Runs at least once, keeps asking until valid input:</p>
<pre><code>int number = 0;

do {
    printf("Enter a number greater than 0: ");
    scanf("%d", &amp;number);
} while(number &lt;= 0); // repeats if number is 0 or negative

(void)getchar(); // flush leftover '\\n' from scanf before fgets</code></pre>
<hr>
<h4>While Example</h4>
<p>Keeps asking for a name until the user enters something:</p>
<pre><code>char name[50] = "";

printf("Enter your name: ");
fgets(name, sizeof(name), stdin);
name[strlen(name) - 1] = '\\0'; // remove trailing newline

while(strlen(name) == 0) { // if name is empty, ask again
    printf("Name cannot be empty! Please enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\\0'; // remove trailing newline
}

printf("Hello %s\\n", name);</code></pre>
<hr>
<h4>While Example: Game Loop</h4>
<pre><code>bool isRunning = true;
char response = '\\0';

while(isRunning){
    printf("You are playing a game\\n");
    printf("Would you like to continue ? (Y = yes, N = no): ");
    scanf("%c", &amp;response);

    if(response != 'Y' &amp;&amp; response != 'y'){
        isRunning = false;
    }
}

printf("You Exit The Game.\\n");</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch13 = next((c for c in c_lang["chapters"] if c.get("id") == "ch13"), None)

    if ch13 is None:
        print('[ERROR] No chapter with id "ch13" found. Nothing changed.')
        return

    if "WHILE" not in ch13.get("title", ""):
        print(f'[WARN] ch13 title is "{ch13.get("title")}", expected it to contain "WHILE".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch13["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 13 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
