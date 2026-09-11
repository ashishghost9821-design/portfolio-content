#!/usr/bin/env python3
"""
Replaces Chapter 20's ("ARRAY OF STRINGS") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter20_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 20: Array of Strings</h3>
<p>In this chapter, we learn arrays of strings &mdash; a 2D char array where each ROW is one string.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is an array of strings</li>
<li>Example: hardcoded array of strings</li>
<li>Example: user input (manual)</li>
<li>Example: user input (loop)</li>
</ul>
<hr>
<h4>What is an Array of Strings?</h4>
<pre><code>char name[rows][maxLength] = {"str1", "str2"};</code></pre>
<p><code>rows</code> = how many strings, <code>maxLength</code> = max characters per string (including <code>\\0</code>).</p>
<p>Visual layout (<code>fruits[4][10]</code>):</p>
<pre><code>[0] -&gt; "Apple\\0   "   (5 chars + null + padding)
[1] -&gt; "Pineapple\\0"  (9 chars + null)
[2] -&gt; "Banana\\0   "  (6 chars + null + padding)
[3] -&gt; "Coconut\\0  "  (7 chars + null + padding)</code></pre>
<p>Each row MUST fit within <code>maxLength</code> including <code>\\0</code> &mdash; "Pineapple" = 9 chars + <code>\\0</code> = 10, exactly fits!</p>
<hr>
<h4>Example 1: Hardcoded Array of Strings</h4>
<p>Modifying individual characters by index:</p>
<pre><code>char fruits[][10] = {"Apple",
                     "Pineapple",
                     "Banana",
                     "Coconut"};

// modifying individual characters like a 2D array
fruits[0][0] = 'e'; // Apple  -&gt; epple
fruits[0][4] = 'a'; // epple  -&gt; eppla

// sizeof(fruits) / sizeof(fruits[0]) = number of strings
int size = sizeof(fruits) / sizeof(fruits[0]);

// loop through and print each string with %s
for(int i = 0; i &lt; size; i++) {
    printf("%s\\n", fruits[i]); // fruits[i] = one full string
}</code></pre>
<hr>
<h4>Example 2: User Input &mdash; Manual (One by One)</h4>
<p><code>fgets</code> reads each string into its own row. <code>strlen</code> strips the trailing <code>\\n</code> that <code>fgets</code> captures.</p>
<pre><code>char names[3][25] = {0}; // {0} initializes all to '\\0'
int rows = sizeof(names) / sizeof(names[0]); // = 3

// WAY 1: manual input for each row
printf("\\n--- Enter 3 names (manual) ---\\n");
printf("Enter a name: ");
fgets(names[0], sizeof(names[0]), stdin);
names[0][strlen(names[0]) - 1] = '\\0'; // strip '\\n'

printf("Enter a name: ");
fgets(names[1], sizeof(names[1]), stdin);
names[1][strlen(names[1]) - 1] = '\\0';

printf("Enter a name: ");
fgets(names[2], sizeof(names[2]), stdin);
names[2][strlen(names[2]) - 1] = '\\0';

// WAY 1: manual print for each row
printf("\\n--- Names entered (manual print) ---\\n");
printf("%s\\n", names[0]);
printf("%s\\n", names[1]);
printf("%s\\n", names[2]);</code></pre>
<hr>
<h4>Example 3: User Input &mdash; Loop</h4>
<p>Cleaner &mdash; a loop handles input and output, and the <code>rows</code> variable makes it easy to scale up.</p>
<pre><code>char names2[3][25] = {0};

// WAY 2: loop input
printf("\\n--- Enter 3 names (loop input) ---\\n");
for(int i = 0; i &lt; 3; i++) {
    printf("Enter a name: ");
    fgets(names2[i], sizeof(names2[i]), stdin);
    names2[i][strlen(names2[i]) - 1] = '\\0'; // strip '\\n'
}

// WAY 2: loop print
printf("\\n--- Names entered (loop print) ---\\n");
for(int i = 0; i &lt; 3; i++) {
    printf("%s\\n", names2[i]);
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch20 = next((c for c in c_lang["chapters"] if c.get("id") == "ch20"), None)

    if ch20 is None:
        print('[ERROR] No chapter with id "ch20" found. Nothing changed.')
        return

    if "ARRAY OF STRINGS" not in ch20.get("title", ""):
        print(f'[WARN] ch20 title is "{ch20.get("title")}", expected it to contain "ARRAY OF STRINGS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch20["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 20 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
