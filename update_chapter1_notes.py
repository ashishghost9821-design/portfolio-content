#!/usr/bin/env python3
"""
Replaces Chapter 1's "notes" field with the new interlaced explanation +
code-block format. Does not touch codeExample, title, desc, or any other
chapter. Makes a .bak backup first.

Run from the folder containing content.json (portfolio-content/):
    python3 update_chapter1_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 1: Basics</h3>
<p>In this chapter, we learn the fundamental building blocks of C programming.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>Structure of a C program</li>
<li>Variables and Data Types</li>
<li>Input and Output (printf, scanf)</li>
<li>Comments</li>
</ul>
<hr>
<h4>Example: Hello World</h4>
<pre><code>#include &lt;stdio.h&gt;

int main() {
    // This is a simple Hello World
    printf("Hello, World!\\n");
    return 0;
}</code></pre>
<p><strong>Line 1 &mdash; <code>#include &lt;stdio.h&gt;</code></strong><br>
Loads the toolkit for printing/reading text. <code>stdio</code> = Standard Input Output. Without this, <code>printf</code> won't work.</p>
<p><strong>Line 3 &mdash; <code>int main()</code></strong><br>
Every C program starts here. <code>int</code> means this function returns a number when done. <code>()</code> means it needs no input to start.</p>
<p><strong>Line 4 &mdash; <code>// comment</code></strong><br>
Ignored by the compiler. Just a note for humans.</p>
<p><strong>Line 5 &mdash; <code>printf("Hello, World!\\n");</code></strong><br>
Prints text to the screen. <code>\\n</code> means "new line." Every instruction ends with <code>;</code>.</p>
<p><strong>Line 6 &mdash; <code>return 0;</code></strong><br>
Tells the computer the program finished successfully.</p>
<hr>
<h4>Variables: Labeled Boxes for Data</h4>
<pre><code>int age = 20;
float price = 19.99;
char grade = 'A';</code></pre>
<p>Before storing data, you tell C what <em>kind</em> of box you need:</p>
<table>
<tr><th>Type</th><th>Stores</th><th>Example</th></tr>
<tr><td><code>int</code></td><td>Whole numbers</td><td>42, -7</td></tr>
<tr><td><code>float</code></td><td>Decimals</td><td>3.14, -0.5</td></tr>
<tr><td><code>char</code></td><td>One character</td><td>'A', '9'</td></tr>
</table>
<hr>
<h4>Output &mdash; Computer talks to you</h4>
<pre><code>printf("Your age is %d years\\n", age);</code></pre>
<p><code>%d</code> is a placeholder &mdash; it gets replaced by whatever <code>age</code> holds.</p>
<h4>Input &mdash; You talk to the computer</h4>
<pre><code>printf("Enter your age: ");
scanf("%d", &amp;age);</code></pre>
<p><code>scanf</code> waits for the user to type. The <code>&amp;</code> means "store the answer inside this box" (<code>age</code>).</p>
<hr>
<h4>Format Specifiers</h4>
<table>
<tr><th>Symbol</th><th>Used for</th></tr>
<tr><td><code>%d</code></td><td>whole numbers (int)</td></tr>
<tr><td><code>%f</code></td><td>decimals (float)</td></tr>
<tr><td><code>%c</code></td><td>single character</td></tr>
<tr><td><code>%s</code></td><td>text (string)</td></tr>
</table>
<hr>
<h4>Comments</h4>
<pre><code>// Single-line comment

/*
Multi-line comment,
for longer explanations
*/</code></pre>
<p><strong>Golden rule:</strong> comments should explain <em>why</em>, not <em>what</em> &mdash; the code already shows what happens.</p>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch1 = next((c for c in c_lang["chapters"] if c.get("id") == "ch1"), None)

    if ch1 is None:
        print('[ERROR] No chapter with id "ch1" found. Nothing changed.')
        return

    ch1["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 1 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
