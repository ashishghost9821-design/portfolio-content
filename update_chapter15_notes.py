#!/usr/bin/env python3
"""
Replaces Chapter 15's ("BREAK & CONTINUE") notes field with an expanded
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter15_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 15: Break &amp; Continue</h3>
<p>In this chapter, we learn two keywords that change how a loop behaves mid-run: <code>break</code> and <code>continue</code>.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>break vs continue</li>
<li>Example: continue</li>
<li>Example: break</li>
<li>Using them inside nested loops</li>
</ul>
<hr>
<h4>Break vs Continue</h4>
<table>
<tr><th>Keyword</th><th>Effect</th></tr>
<tr><td><code>break</code></td><td>STOPS the loop completely &mdash; exits immediately, skipping every remaining iteration</td></tr>
<tr><td><code>continue</code></td><td>SKIPS the current iteration only &mdash; jumps straight to the next cycle of the loop</td></tr>
</table>
<p>Think of <code>break</code> as "leave the room now" and <code>continue</code> as "skip this one step, but keep walking."</p>
<hr>
<h4>Example 1: continue &mdash; skip number 4</h4>
<p>Prints 1 2 3 5 6 7 8 9 10 (4 is skipped, but the loop keeps going):</p>
<pre><code>for(int i = 1; i &lt;= 10; i++) {
    if(i == 4) {
        continue; // skip this iteration, go to i=5
    }
    printf("%d\\n", i);
}</code></pre>
<hr>
<h4>Example 2: break &mdash; stop at number 4</h4>
<p>Prints only 1 2 3 (the loop ends the moment <code>i</code> hits 4, so 4-10 never print):</p>
<pre><code>for(int i = 1; i &lt;= 10; i++) {
    if(i == 4) {
        break; // exit the loop entirely
    }
    printf("%d\\n", i);
}</code></pre>
<hr>
<h4>Common Mix-up</h4>
<p>Both examples check the same condition (<code>i == 4</code>), but the outcome is very different:</p>
<table>
<tr><th>Keyword</th><th>Output</th><th>Loop continues after i=4?</th></tr>
<tr><td><code>continue</code></td><td>1 2 3 5 6 7 8 9 10</td><td>Yes &mdash; only that one number is skipped</td></tr>
<tr><td><code>break</code></td><td>1 2 3</td><td>No &mdash; the loop ends right there</td></tr>
</table>
<hr>
<h4>Nested Loops</h4>
<p><code>break</code> and <code>continue</code> only affect the <strong>innermost</strong> loop they're written in &mdash; an outer loop keeps running normally.</p>
<pre><code>for(int i = 1; i &lt;= 3; i++) {
    for(int j = 1; j &lt;= 3; j++) {
        if(j == 2) {
            break; // only exits the inner (j) loop
        }
        printf("i=%d j=%d\\n", i, j);
    }
    // outer loop (i) keeps running even after inner break
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch15 = next((c for c in c_lang["chapters"] if c.get("id") == "ch15"), None)

    if ch15 is None:
        print('[ERROR] No chapter with id "ch15" found. Nothing changed.')
        return

    if "BREAK" not in ch15.get("title", ""):
        print(f'[WARN] ch15 title is "{ch15.get("title")}", expected it to contain "BREAK".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch15["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 15 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
