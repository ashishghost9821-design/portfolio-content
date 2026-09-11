#!/usr/bin/env python3
"""
Replaces Chapter 16's ("NESTED LOOPS") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter16_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 16: Nested Loops</h3>
<p>In this chapter, we learn nested loops &mdash; a loop inside another loop. The inner loop completes ALL its iterations for EACH single iteration of the outer loop.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a nested loop</li>
<li>Example: single loop</li>
<li>Example: nested loop</li>
<li>Example: multiplication table</li>
<li>Example: user input grid</li>
</ul>
<hr>
<h4>What is a Nested Loop?</h4>
<p><strong>Important:</strong> use different variable names for each loop (<code>i</code>, <code>j</code>, <code>x</code>, <code>y</code>) to avoid conflicts.</p>
<hr>
<h4>Example 1: Single Loop</h4>
<p>Prints 1 2 3 4 5 6 7 8 9 on one line:</p>
<pre><code>for(int i = 1; i &lt; 10; i++) {
    printf("%d ", i);
}
printf("\\n"); // move to next line after loop</code></pre>
<hr>
<h4>Example 2: Nested Loop</h4>
<p>Outer loop (<code>j</code>) runs 3 times, inner loop (<code>i</code>) runs 9 times per outer cycle &mdash; prints the same row of numbers 3 times.</p>
<pre><code>for(int j = 1; j &lt; 4; j++) {       // outer: 3 rows
    for(int i = 1; i &lt; 10; i++) {  // inner: 9 columns
        printf("%d ", i);
    }
    printf("\\n"); // new line after each row
}</code></pre>
<hr>
<h4>Example 3: Multiplication Table</h4>
<p>Outer loop (<code>y</code>) = row (1 to 10), inner loop (<code>x</code>) = column (1 to 10), <code>x * y</code> = value at each cell. <code>%3d</code> prints an int with 3 spaces width to keep columns aligned neatly.</p>
<pre><code>for(int y = 1; y &lt;= 10; y++) {      // outer: each row
    for(int x = 1; x &lt;= 10; x++) { // inner: each column
        printf("%3d ", x * y);      // %3d aligns columns
    }
    printf("\\n"); // new line after each row
}</code></pre>
<hr>
<h4>Example 4: User Input Grid</h4>
<p>User chooses rows, columns, and a symbol. Outer loop controls rows (<code>r</code>), inner loop controls columns (<code>c</code>). NEVER use the same variable name in nested loops!</p>
<pre><code>int  rows    = 0;
int  columns = 0;
char symbol  = '\\0';

printf("Enter the # of rows: ");
scanf("%d", &amp;rows);

printf("Enter the # of columns: ");
scanf("%d", &amp;columns);

printf("Enter a symbol to use: ");
scanf(" %c", &amp;symbol);

for(int r = 0; r &lt; rows; r++) {        // outer: controls rows
    for(int c = 0; c &lt; columns; c++) { // inner: controls columns
        printf("%c", symbol);
    }
    printf("\\n"); // new line after each row
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch16 = next((c for c in c_lang["chapters"] if c.get("id") == "ch16"), None)

    if ch16 is None:
        print('[ERROR] No chapter with id "ch16" found. Nothing changed.')
        return

    if "NESTED LOOPS" not in ch16.get("title", ""):
        print(f'[WARN] ch16 title is "{ch16.get("title")}", expected it to contain "NESTED LOOPS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch16["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 16 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
