#!/usr/bin/env python3
"""
Replaces Chapter 17's ("ARRAYS") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter17_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 17: Arrays</h3>
<p>In this chapter, we learn arrays &mdash; a fixed size collection of elements of the SAME data type. Similar to a variable, but holds more than one value.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is an array</li>
<li>int and char arrays</li>
<li>Arrays as strings</li>
<li>Modifying array elements</li>
<li>Looping through arrays</li>
<li>sizeof() with arrays</li>
</ul>
<hr>
<h4>What is an Array?</h4>
<pre><code>type name[] = {val1, val2, val3};</code></pre>
<p>Indexing starts at 0, NOT 1: <code>numbers[0]</code> is the first element, <code>numbers[4]</code> is the fifth (last) element.</p>
<p><strong>Never</strong> access an index equal to or beyond the size: <code>int numbers[5]</code> is valid at <code>[0][1][2][3][4]</code> &mdash; <code>numbers[5]</code> is OUT OF BOUNDS = undefined behavior!</p>
<hr>
<h4>Example 1: int Array</h4>
<pre><code>int numbers[] = {10, 20, 30, 40, 50}; // size = 5, index 0 to 4

printf("%d\\n", numbers[0]); // 10
printf("%d\\n", numbers[1]); // 20
printf("%d\\n", numbers[2]); // 30
printf("%d\\n", numbers[3]); // 40
printf("%d\\n", numbers[4]); // 50
// numbers[5] -> WARNING: out of bounds! array ends at [4]</code></pre>
<hr>
<h4>Example 2: char Array (Individual Characters)</h4>
<pre><code>char grade[] = {'A', 'B', 'C', 'D', 'F'}; // size = 5

printf("%c\\n", grade[0]); // A
printf("%c\\n", grade[1]); // B</code></pre>
<hr>
<h4>Example 3: char Array as String</h4>
<p>Double quotes = string, stored as a char array. The compiler auto-sets the size.</p>
<pre><code>char name[] = "Ashish Ghost";

printf("%c\\n", name[0]); // A (first character only)</code></pre>
<hr>
<h4>Example 4: Modifying Array Elements</h4>
<p>Arrays are NOT read-only, values can change.</p>
<pre><code>numbers[0] = 100; // overwrite index 0
numbers[1] = 90;
numbers[2] = 80;

printf("%d\\n", numbers[0]); // now 100
printf("%d\\n", numbers[1]); // now 90
printf("%d\\n", numbers[2]); // now 80</code></pre>
<hr>
<h4>Example 5: Loop Through Arrays</h4>
<p>Much better than printing one element at a time.</p>
<pre><code>// loop through grade[] char array
for(int i = 0; i &lt; 5; i++) {
    printf("%c\\n", grade[i]);
}

// loop through numbers[] int array
for(int i = 0; i &lt; 5; i++) {
    printf("%d\\n", numbers[i]);
}

// loop through name[] string char by char
for(int i = 0; i &lt; 12; i++) {
    printf("%c\\n", name[i]);
}</code></pre>
<hr>
<h4>Example 6: sizeof() with Arrays</h4>
<table>
<tr><th>Expression</th><th>Gives you</th><th>Example result</th></tr>
<tr><td><code>sizeof(numbers)</code></td><td>total bytes of whole array</td><td>5 elements &times; 4 bytes = 20</td></tr>
<tr><td><code>sizeof(numbers[0])</code></td><td>bytes of ONE element</td><td>4</td></tr>
<tr><td><code>sizeof(numbers) / sizeof(numbers[0])</code></td><td>total elements in array</td><td>20 / 4 = 5</td></tr>
</table>
<p><strong>Why use this?</strong> If you change the array size later, the loop automatically adjusts &mdash; no need to update manually.</p>
<pre><code>printf("Total bytes:     %zu\\n", sizeof(numbers));      // 20
printf("One element:     %zu\\n", sizeof(numbers[0]));   // 4
printf("Number of items: %zu\\n", sizeof(numbers) / sizeof(numbers[0])); // 5

// BEST PRACTICE: use sizeof to get size automatically
int size = sizeof(numbers) / sizeof(numbers[0]);
for(int i = 0; i &lt; size; i++) {
    printf("%d\\n", numbers[i]);
}

// OR write it directly inside the for loop
// for(int i = 0; i &lt; sizeof(numbers) / sizeof(numbers[0]); i++) {
//     printf("%d\\n", numbers[i]);
// }</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch17 = next((c for c in c_lang["chapters"] if c.get("id") == "ch17"), None)

    if ch17 is None:
        print('[ERROR] No chapter with id "ch17" found. Nothing changed.')
        return

    if "ARRAYS" not in ch17.get("title", ""):
        print(f'[WARN] ch17 title is "{ch17.get("title")}", expected it to contain "ARRAYS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch17["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 17 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
