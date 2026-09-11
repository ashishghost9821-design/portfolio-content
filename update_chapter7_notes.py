#!/usr/bin/env python3
"""
Replaces Chapter 7's ("NESTED IF/ELSE") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter7_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 7: Nested If/Else</h3>
<p>In this chapter, we learn how to put an <code>if</code>/<code>else</code> inside another <code>if</code>/<code>else</code> &mdash; used when a condition depends on another condition.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a nested if/else</li>
<li>Compound assignment operator</li>
<li>Example: ticket discount calculator</li>
</ul>
<hr>
<h4>What is a Nested If/Else?</h4>
<pre><code>if(condition1) {
    if(condition2) {
        // both true
    }
    else {
        // only condition1 true
    }
}
else {
    // condition1 false
}</code></pre>
<hr>
<h4>Compound Assignment Operator</h4>
<p>Shorthand for updating a variable's own value.</p>
<pre><code>price *= 0.9  // means  price = price * 0.9
price *= 0.8  // means  price = price * 0.8
price *= 0.7  // means  price = price * 0.7</code></pre>
<hr>
<h4>Example: Ticket Discount Calculator</h4>
<p>Base price = $10.00. Discount rules:</p>
<table>
<tr><th>Condition</th><th>Discount</th><th>Result</th></tr>
<tr><td>student only</td><td>10% off</td><td>$9.00 (&times; 0.9)</td></tr>
<tr><td>senior only</td><td>20% off</td><td>$8.00 (&times; 0.8)</td></tr>
<tr><td>student + senior both</td><td>30% off</td><td>$7.00 (&times; 0.7)</td></tr>
<tr><td>neither</td><td>no discount</td><td>&mdash;</td></tr>
</table>
<pre><code>float price     = 10.00f; // base ticket price
bool isStudent  = true;   // toggle to test different cases
bool isSenior   = true;   // toggle to test different cases

if(isStudent) {
    if(isSenior) {
        // both student AND senior -&gt; 30% off total
        printf("You get a student discount of 10%%.\\n");
        printf("You get a senior discount of 20%%.\\n");
        price *= 0.7; // price = price * 0.7
    }
    else {
        // student only -&gt; 10% off
        printf("You get a student discount of 10%%.\\n");
        price *= 0.9; // price = price * 0.9
    }
}
else {
    if(isSenior) {
        // senior only -&gt; 20% off
        printf("You get a senior discount of 20%%.\\n");
        price *= 0.8; // price = price * 0.8
    }
    // else: no discount, price stays the same
}

printf("The price of a ticket is: $%.2f\\n", price);</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch7 = next((c for c in c_lang["chapters"] if c.get("id") == "ch7"), None)

    if ch7 is None:
        print('[ERROR] No chapter with id "ch7" found. Nothing changed.')
        return

    if "NESTED" not in ch7.get("title", ""):
        print(f'[WARN] ch7 title is "{ch7.get("title")}", expected it to contain "NESTED".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch7["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 7 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
