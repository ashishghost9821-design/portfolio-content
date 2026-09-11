#!/usr/bin/env python3
"""
Replaces Chapter 4's ("MATH FUNCTIONS") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter4_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 4: Math Functions</h3>
<p>In this chapter, we use the <code>&lt;math.h&gt;</code> library for common mathematical operations: square roots, powers, rounding, and trigonometry.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>math.h library</li>
<li>Rounding functions</li>
<li>Absolute value &amp; logarithm</li>
<li>Trigonometric functions</li>
</ul>
<hr>
<h4>math.h Library</h4>
<p><code>&lt;math.h&gt;</code> provides built-in functions for common mathematical operations like square roots, powers, rounding, and trigonometry.</p>
<pre><code>float x = 9;

// sqrt(x) -> square root of x
printf("sqrt:  %f\\n", sqrt(x));

// pow(x, 4) -> x to the power of 4
printf("pow:   %f\\n", pow(x, 4));</code></pre>
<hr>
<h4>Rounding Functions</h4>
<table>
<tr><th>Function</th><th>Effect</th></tr>
<tr><td><code>round()</code></td><td>nearest whole number</td></tr>
<tr><td><code>ceil()</code></td><td>always rounds UP</td></tr>
<tr><td><code>floor()</code></td><td>always rounds DOWN</td></tr>
</table>
<pre><code>// round(x) -> 9.5 and above rounds up, below rounds down
printf("round: %f\\n", round(x));

// ceil(x) -> even 9.1 becomes 10.0
printf("ceil:  %f\\n", ceil(x));

// floor(x) -> even 9.9 becomes 9.0
printf("floor: %f\\n", floor(x));</code></pre>
<hr>
<h4>Absolute Value &amp; Logarithm</h4>
<pre><code>// fabs(x) -> absolute value for float
// use fabs() NOT abs() -- abs() is for int only
printf("fabs:  %f\\n", fabs(x));

// log(x) -> natural logarithm (base e)
printf("log:   %f\\n", log(x));</code></pre>
<hr>
<h4>Trigonometric Functions</h4>
<p><code>sin()</code>, <code>cos()</code>, <code>tan()</code> all expect the angle in <strong>radians</strong>, not degrees.</p>
<pre><code>printf("sin:   %f\\n", sin(x));
printf("cos:   %f\\n", cos(x));
printf("tan:   %f\\n", tan(x));</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch4 = next((c for c in c_lang["chapters"] if c.get("id") == "ch4"), None)

    if ch4 is None:
        print('[ERROR] No chapter with id "ch4" found. Nothing changed.')
        return

    if "MATH FUNCTIONS" not in ch4.get("title", ""):
        print(f'[WARN] ch4 title is "{ch4.get("title")}", expected it to contain "MATH FUNCTIONS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch4["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 4 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
