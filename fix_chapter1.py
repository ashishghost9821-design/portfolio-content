import json, shutil

FILE = "content.json"
shutil.copy(FILE, FILE + ".bak2")   # extra safety backup

with open(FILE) as f:
    data = json.load(f)

chapters = data["languages"][0]["chapters"]

notes_html = r"""<p>In this chapter, we learn the fundamental building blocks of C programming.</p>

<p><strong>Topics Covered:</strong></p>
<ul>
<li>Structure of a C program</li>
<li>Variables and Data Types</li>
<li>Input and Output (printf, scanf)</li>
<li>Comments</li>
</ul>

<h3>Example: Hello World</h3>

<p><strong>Line 1 — <code>#include &lt;stdio.h&gt;</code></strong><br>
Loads the toolkit for printing/reading text. <code>stdio</code> = Standard Input Output. Without this, <code>printf</code> won't work.</p>

<p><strong>Line 3 — <code>int main()</code></strong><br>
Every C program starts here. <code>int</code> means this function returns a number when done. <code>()</code> means it needs no input to start.</p>

<p><strong>Line 4 — <code>// comment</code></strong><br>
Ignored by the compiler. Just a note for humans.</p>

<p><strong>Line 5 — <code>printf("Hello, World!\n");</code></strong><br>
Prints text to the screen. <code>\n</code> means "new line." Every instruction ends with <code>;</code>.</p>

<p><strong>Line 6 — <code>return 0;</code></strong><br>
Tells the computer the program finished successfully.</p>

<h3>Variables: Labeled Boxes for Data</h3>
<p>Before storing data, you tell C what <em>kind</em> of box you need:</p>
<table>
<tr><th>Type</th><th>Stores</th><th>Example</th></tr>
<tr><td>int</td><td>Whole numbers</td><td>42, -7</td></tr>
<tr><td>float</td><td>Decimals</td><td>3.14, -0.5</td></tr>
<tr><td>char</td><td>One character</td><td>'A', '9'</td></tr>
</table>

<h3>Output — Computer talks to you</h3>
<p><code>%d</code> is a placeholder — it gets replaced by whatever <code>age</code> holds.</p>

<h3>Input — You talk to the computer</h3>
<p><code>scanf</code> waits for the user to type. The <code>&amp;</code> means "store the answer inside this box" (<code>age</code>).</p>

<h3>Format Specifiers</h3>
<table>
<tr><th>Symbol</th><th>Used for</th></tr>
<tr><td>%d</td><td>whole numbers (int)</td></tr>
<tr><td>%f</td><td>decimals (float)</td></tr>
<tr><td>%c</td><td>single character</td></tr>
<tr><td>%s</td><td>text (string)</td></tr>
</table>

<h3>Comments</h3>
<p>Golden rule: comments should explain <em>why</em>, not <em>what</em> — the code already shows what happens.</p>
"""

code_example = r"""#include <stdio.h>

int main() {
    // This is a simple Hello World
    printf("Hello, World!\n");

    // Variables: Labeled Boxes for Data
    int age = 20;
    float price = 19.99;
    char grade = 'A';

    // Output — Computer talks to you
    printf("Your age is %d years\n", age);

    // Input — You talk to the computer
    printf("Enter your age: ");
    scanf("%d", &age);

    /*
    Multi-line comment,
    for longer explanations
    */

    return 0;
}
"""

found = False
for ch in chapters:
    if ch["id"] == "ch1":
        ch["title"] = "Chapter 1: BASICS"
        ch["desc"] = "The fundamental building blocks of C programming."
        ch["notes"] = notes_html
        ch["codeExample"] = code_example
        found = True
        break

if not found:
    raise SystemExit("ch1 not found — did the earlier insert run?")

with open(FILE, "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("ch1 replaced with your exact content. Backup at content.json.bak2")
