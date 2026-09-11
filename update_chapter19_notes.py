#!/usr/bin/env python3
"""
Replaces Chapter 19's ("2D ARRAYS") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter19_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 19: 2D Arrays</h3>
<p>In this chapter, we learn 2D arrays &mdash; an array where each element is itself an array. Think of it as a TABLE with rows and columns.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a 2D array</li>
<li>Example: 3x3 int array (manual access)</li>
<li>Example: 4x3 int array with nested loop</li>
<li>Example: 2D char array (numpad)</li>
</ul>
<hr>
<h4>What is a 2D Array?</h4>
<pre><code>type name[rows][columns] = {{...}, {...}, {...}};</code></pre>
<p>You can leave rows empty <code>[]</code> &mdash; the compiler counts them. You MUST always specify columns.</p>
<p>Accessing elements: <code>name[row][column]</code>. <code>name[0][0]</code> is the first row, first column. <code>name[1][2]</code> is the second row, third column.</p>
<p>Visual layout:</p>
<pre><code>            col0  col1  col2
  row0  ->  [1]   [2]   [3]
  row1  ->  [4]   [5]   [6]
  row2  ->  [7]   [8]   [9]</code></pre>
<hr>
<h4>Example 1: 3x3 int 2D Array</h4>
<p>Accessing elements manually by index:</p>
<pre><code>int numbers[][3] = {{1, 2, 3},
                    {4, 5, 6},
                    {7, 8, 9}};

// row 0
printf("%d", numbers[0][0]); // 1
printf("%d", numbers[0][1]); // 2
printf("%d\\n", numbers[0][2]); // 3

// row 1
printf("%d", numbers[1][0]); // 4
printf("%d", numbers[1][1]); // 5
printf("%d\\n", numbers[1][2]); // 6

// row 2
printf("%d", numbers[2][0]); // 7
printf("%d", numbers[2][1]); // 8
printf("%d\\n", numbers[2][2]); // 9</code></pre>
<hr>
<h4>Example 2: 4x3 int 2D Array with Nested Loop</h4>
<p>Outer loop = rows, inner loop = columns &mdash; much cleaner than accessing manually.</p>
<pre><code>int number[][3] = {{1,  2,  3},
                   {4,  5,  6},
                   {7,  8,  9},
                   {10, 11, 12}};

for(int i = 0; i &lt; 4; i++) {        // i = row    (0 to 3)
    for(int j = 0; j &lt; 3; j++) {    // j = column (0 to 2)
        printf("%3d", number[i][j]); // %3d keeps columns aligned
    }
    printf("\\n"); // new line after each row
}</code></pre>
<hr>
<h4>Example 3: 2D char Array &mdash; Numpad</h4>
<p>Same concept but with characters &mdash; shows 2D arrays work with any data type.</p>
<pre><code>char numpad[][3] = {{'1', '2', '3'},
                    {'4', '5', '6'},
                    {'7', '8', '9'},
                    {'*', '0', '#'}};

printf("\\n--- Numpad ---\\n");
for(int i = 0; i &lt; 4; i++) {     // 4 rows
    for(int j = 0; j &lt; 3; j++) { // 3 columns
        printf("%c ", numpad[i][j]);
    }
    printf("\\n"); // new line after each row
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch19 = next((c for c in c_lang["chapters"] if c.get("id") == "ch19"), None)

    if ch19 is None:
        print('[ERROR] No chapter with id "ch19" found. Nothing changed.')
        return

    if "2D ARRAYS" not in ch19.get("title", ""):
        print(f'[WARN] ch19 title is "{ch19.get("title")}", expected it to contain "2D ARRAYS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch19["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 19 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
