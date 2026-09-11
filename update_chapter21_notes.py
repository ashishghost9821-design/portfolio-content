#!/usr/bin/env python3
"""
Replaces Chapter 21's ("TERNARY OPERATOR") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter21_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 21: Ternary Operator</h3>
<p>In this chapter, we learn the ternary operator &mdash; shorthand for a simple if/else statement that returns one of two values based on a condition.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is the ternary operator</li>
<li>Example: max of two numbers</li>
<li>Example: bool condition inside printf</li>
<li>Example: even or odd check</li>
<li>Example: age check</li>
<li>Example: AM or PM clock</li>
</ul>
<hr>
<h4>What is the Ternary Operator?</h4>
<pre><code>(condition) ? value_if_true : value_if_false;</code></pre>
<p>Equivalent to:</p>
<pre><code>if(condition) { value_if_true }
else          { value_if_false }</code></pre>
<p>Best used for SHORT, SIMPLE conditions. For complex logic, use regular if/else.</p>
<hr>
<h4>Example 1: Find Max of Two Numbers</h4>
<p>If <code>x &gt; y</code> is true, max = x. If false, max = y.</p>
<pre><code>int x   = 5;
int y   = 6;
int max = (x &gt; y) ? x : y;
printf("Max: %d\\n", max); // 6</code></pre>
<hr>
<h4>Example 2: Bool Condition Inside printf</h4>
<p>Ternary used directly inside <code>printf</code>.</p>
<pre><code>bool isOnline = true;
printf("%s", (isOnline) ? "Online\\n" : "Offline\\n");</code></pre>
<hr>
<h4>Example 3: Even or Odd Check</h4>
<p><code>number % 2 == 0</code> means no remainder = even.</p>
<pre><code>int number = 8;
printf("%d is %s", number, (number % 2 == 0) ? "Even\\n" : "Odd\\n");</code></pre>
<hr>
<h4>Example 4: Age Check</h4>
<pre><code>int age = 21;
printf("%s", (age &gt;= 18) ? "Adult\\n" : "Child\\n");</code></pre>
<hr>
<h4>Example 5: AM or PM Clock</h4>
<p><code>%02d</code> prints an int with 2 digits, padded with 0 &mdash; e.g. 9 becomes "09", 11 stays "11".</p>
<pre><code>int hours   = 11;
int minutes = 30;
printf("%02d:%02d %s", hours, minutes, (hours &lt; 12) ? "AM\\n" : "PM\\n");
// alternative way using a variable:
// char *meridiem = (hours &lt; 12) ? "AM" : "PM";
// printf("%02d:%02d %s\\n", hours, minutes, meridiem);</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch21 = next((c for c in c_lang["chapters"] if c.get("id") == "ch21"), None)

    if ch21 is None:
        print('[ERROR] No chapter with id "ch21" found. Nothing changed.')
        return

    if "TERNARY" not in ch21.get("title", ""):
        print(f'[WARN] ch21 title is "{ch21.get("title")}", expected it to contain "TERNARY".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch21["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 21 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
