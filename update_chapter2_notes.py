#!/usr/bin/env python3
"""
Replaces Chapter 2's ("VARIABLES") notes field with the interlaced
explanation + code-block format. Does not touch codeExample, title,
or any other chapter. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter2_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 2: Variables</h3>
<p>In this chapter, we learn how to store and display data using variables, data types, and format specifiers.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a variable</li>
<li>Data types</li>
<li>Format specifiers</li>
<li>Width &amp; flag modifiers</li>
</ul>
<hr>
<h4>What is a Variable?</h4>
<p>A variable is a reusable container for a value.</p>
<pre><code>data_type variable_name = value;</code></pre>
<pre><code>int age      = 25;
int year     = 2026;
int quantity = 10;

printf("You are %d years old\\n", age);
printf("This is %d\\n", year);
printf("You have ordered %d bananas\\n", quantity);</code></pre>
<p><code>int</code> stores whole numbers. Each <code>printf</code> swaps in the variable's value wherever it sees <code>%d</code>.</p>
<hr>
<h4>Data Types</h4>
<table>
<tr><th>Type</th><th>Size</th><th>Description</th></tr>
<tr><td><code>int</code></td><td>4 bytes</td><td>Whole number</td></tr>
<tr><td><code>float</code></td><td>4 bytes</td><td>Single-precision decimal</td></tr>
<tr><td><code>double</code></td><td>8 bytes</td><td>Double-precision decimal</td></tr>
<tr><td><code>char</code></td><td>1 byte</td><td>Single character</td></tr>
<tr><td><code>char[]</code></td><td>varies</td><td>Array of characters (string)</td></tr>
<tr><td><code>bool</code></td><td>1 byte</td><td>true or false (needs &lt;stdbool.h&gt;)</td></tr>
</table>
<pre><code>float  gpa      = 2.5;
float  price    = 19.99;
double pi       = 3.141592;
char   grade    = 'A';
char   name[]   = "Bro Code";
bool   isOnline = true;

printf("Your GPA is %.1f\\n",          gpa);
printf("The price is $%.2f\\n",        price);
printf("The value of pi is %.15lf\\n", pi);
printf("Your grade is %c\\n",          grade);
printf("Hello, %s!\\n",                name);
printf("Is online: %d\\n",             isOnline);</code></pre>
<p>Single quotes (<code>'A'</code>) hold one character. Double quotes (<code>"Bro Code"</code>) hold text. <code>bool</code> prints as <code>1</code> for true or <code>0</code> for false.</p>
<hr>
<h4>Format Specifiers</h4>
<p>Special tokens starting with <code>%</code> that control how data is displayed.</p>
<table>
<tr><th>Specifier</th><th>Used for</th></tr>
<tr><td><code>%d</code></td><td>int</td></tr>
<tr><td><code>%f</code></td><td>float</td></tr>
<tr><td><code>%lf</code></td><td>double</td></tr>
<tr><td><code>%c</code></td><td>char</td></tr>
<tr><td><code>%s</code></td><td>string (char[])</td></tr>
<tr><td><code>%.Nf</code></td><td>float/double with N decimal places</td></tr>
</table>
<pre><code>printf("%d\\n",  id);       // integer
printf("%f\\n",  cost);     // float (default 6 decimal places)
printf("%lf\\n", precise);  // double
printf("%c\\n",  symbol);   // character
printf("%s\\n",  label);    // string</code></pre>
<hr>
<h4>Width &amp; Flag Modifiers</h4>
<p>Go between <code>%</code> and the specifier to control alignment.</p>
<table>
<tr><th>Modifier</th><th>Effect</th></tr>
<tr><td><code>%+d</code></td><td>Always show sign (+ or -)</td></tr>
<tr><td><code>%-3d</code></td><td>Left-align in a field of width 3</td></tr>
<tr><td><code>%3d</code></td><td>Right-align in a field of width 3</td></tr>
<tr><td><code>%03d</code></td><td>Right-align, zero-pad instead of spaces</td></tr>
</table>
<pre><code>printf("%+d\\n",  num1);  // output: +1
printf("%-3d|\\n", num2); // output: 10|   (left-aligned, | shows spacing)
printf("%3d\\n",  num3);  // output: 100   (right-aligned)
printf("%03d\\n", num4);  // output: -1000 (negative overrides zero-pad)</code></pre>
<p><strong>Note:</strong> a negative number's minus sign takes priority over zero-padding.</p>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch2 = next((c for c in c_lang["chapters"] if c.get("id") == "ch2"), None)

    if ch2 is None:
        print('[ERROR] No chapter with id "ch2" found. Nothing changed.')
        return

    if "VARIABLES" not in ch2.get("title", ""):
        print(f'[WARN] ch2 title is "{ch2.get("title")}", expected it to contain "VARIABLES".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch2["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 2 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
