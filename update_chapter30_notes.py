#!/usr/bin/env python3
"""
Replaces Chapter 30's ("CALLOC") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter30_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 30: Calloc</h3>
<p>In this chapter, we learn <code>calloc()</code> &mdash; contiguous allocation, like <code>malloc()</code> but with one important difference.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is calloc()</li>
<li>malloc vs calloc</li>
<li>Example: allocating scores at runtime</li>
</ul>
<hr>
<h4>What is calloc()?</h4>
<table>
<tr><th>Function</th><th>Behavior</th></tr>
<tr><td><code>malloc(size)</code></td><td>allocates memory, values are GARBAGE</td></tr>
<tr><td><code>calloc(count, size)</code></td><td>allocates memory, sets ALL bytes to 0</td></tr>
</table>
<pre><code>type *ptr = calloc(numberOfElements, sizeof(type));</code></pre>
<pre><code>int *scores = calloc(5, sizeof(int));
// allocates 5 ints = 20 bytes, all set to 0</code></pre>
<hr>
<h4>malloc vs calloc</h4>
<table>
<tr><th>Function</th><th>Trade-off</th></tr>
<tr><td><code>malloc</code></td><td>faster (skips zeroing memory)</td></tr>
<tr><td><code>calloc</code></td><td>safer (no garbage values, fewer bugs)</td></tr>
</table>
<p><strong>Always:</strong></p>
<ol>
<li>check for <code>NULL</code> after calloc</li>
<li><code>free()</code> when done</li>
<li>set the pointer to <code>NULL</code> after free()</li>
</ol>
<hr>
<h4>Example: Allocating Scores at Runtime</h4>
<pre><code>int number = 0;
printf("Enter the number of players: ");
scanf("%d", &amp;number);

// calloc(count, size) -- allocates and zeroes memory
int *scores = calloc(number, sizeof(int));

// check if allocation succeeded
if(scores == NULL) {
    printf("Memory allocation failed!\\n");
    return 1;
}

// fill scores array with user input
for(int i = 0; i &lt; number; i++) {
    printf("Enter score #%d: ", i + 1);
    scanf("%d", &amp;scores[i]);
}

// print all scores
printf("\\nScores: ");
for(int i = 0; i &lt; number; i++) {
    printf("%d ", scores[i]);
}
printf("\\n");

free(scores);   // return memory to OS
scores = NULL;  // avoid dangling pointer</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch30 = next((c for c in c_lang["chapters"] if c.get("id") == "ch30"), None)

    if ch30 is None:
        print('[ERROR] No chapter with id "ch30" found. Nothing changed.')
        return

    if "CALLOC" not in ch30.get("title", ""):
        print(f'[WARN] ch30 title is "{ch30.get("title")}", expected it to contain "CALLOC".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch30["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 30 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
