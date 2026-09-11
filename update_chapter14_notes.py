#!/usr/bin/env python3
"""
Replaces Chapter 14's ("FOR LOOPS") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter14_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 14: For Loops</h3>
<p>In this chapter, we learn <code>for</code> loops &mdash; best used when you know exactly how many times you want to repeat something.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a for loop</li>
<li>Counting up, down, and by steps</li>
<li>Countdown timer with sleep()</li>
</ul>
<hr>
<h4>What is a For Loop?</h4>
<pre><code>for(initialize; condition; update) {
    // code to repeat
}</code></pre>
<p>How it works step by step:</p>
<ol>
<li><code>initialize</code> &mdash; runs ONCE at the start (<code>int i = 0</code>)</li>
<li><code>condition</code> &mdash; checked BEFORE each run (<code>i &lt;= 10</code>)</li>
<li><code>body</code> &mdash; runs if condition is true</li>
<li><code>update</code> &mdash; runs AFTER each body (<code>i++</code>)</li>
<li>repeat from step 2 until condition is false</li>
</ol>
<table>
<tr><th>Operator</th><th>Meaning</th></tr>
<tr><td><code>i++</code></td><td>i = i + 1 (increment by 1)</td></tr>
<tr><td><code>i--</code></td><td>i = i - 1 (decrement by 1)</td></tr>
<tr><td><code>i+=2</code></td><td>i = i + 2 (skips odd numbers)</td></tr>
<tr><td><code>i+=3</code></td><td>i = i + 3 (every 3rd number)</td></tr>
</table>
<hr>
<h4>Example 1: Count 0 to 10 by 1</h4>
<pre><code>for(int i = 0; i &lt;= 10; i++) {
    printf("%d\\n", i); // prints 0 1 2 3 4 5 6 7 8 9 10
}</code></pre>
<hr>
<h4>Example 2: Count 0 to 10 by 2 (even numbers only)</h4>
<pre><code>for(int i = 0; i &lt;= 10; i+=2) {
    printf("%d\\n", i); // prints 0 2 4 6 8 10
}</code></pre>
<hr>
<h4>Example 3: Count 0 to 100 by 3</h4>
<pre><code>for(int i = 0; i &lt;= 100; i+=3) {
    printf("%d\\n", i); // prints 0 3 6 9 12 ... 99
}</code></pre>
<hr>
<h4>Example 4: Count Down from 10 to 0</h4>
<pre><code>for(int i = 10; i &gt;= 0; i--) {
    printf("%d\\n", i); // prints 10 9 8 7 6 5 4 3 2 1 0
}</code></pre>
<hr>
<h4>Example 5: Countdown Timer with sleep()</h4>
<p><code>sleep(1)</code> pauses the program for 1 second each loop. Linux/Mac: <code>sleep(1)</code> = 1 second. Windows: <code>Sleep(1000)</code> = 1000 milliseconds = 1 second (capital S, needs <code>&lt;windows.h&gt;</code>).</p>
<pre><code>for(int i = 10; i &gt;= 0; i--) {
    sleep(1);          // pause 1 second before printing
    printf("%d\\n", i); // prints 10 9 8 ... 0 with 1 sec delay
}

printf("Happy New Year!\\n"); // prints after countdown finishes</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch14 = next((c for c in c_lang["chapters"] if c.get("id") == "ch14"), None)

    if ch14 is None:
        print('[ERROR] No chapter with id "ch14" found. Nothing changed.')
        return

    if "FOR LOOPS" not in ch14.get("title", ""):
        print(f'[WARN] ch14 title is "{ch14.get("title")}", expected it to contain "FOR LOOPS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch14["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 14 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
