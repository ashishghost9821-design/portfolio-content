#!/usr/bin/env python3
"""
Fixes Chapter 18's broken placeholder title and replaces its notes
field with an explanation showing user input WITHOUT a loop vs WITH
a loop for arrays. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter18_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_TITLE = "Chapter 18: User Input with Arrays"

NEW_NOTES = """<h3>Chapter 18: User Input with Arrays</h3>
<p>In this chapter, we fill an array with values the user types in. We'll look at it two ways: WITHOUT a loop first (so you can see exactly what's repeating), then WITH a loop (the way you'd actually write it).</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>Filling an array without a loop</li>
<li>Filling an array with a loop</li>
<li>Why the loop version is better</li>
</ul>
<hr>
<h4>Without a Loop</h4>
<p>To fill 5 slots in an array by hand, you'd repeat the same two lines &mdash; a <code>printf</code> to ask, and a <code>scanf</code> to store the answer at that index &mdash; once per slot:</p>
<pre><code>int scores[5] = {0};

printf("Enter a score: ");
scanf("%d", &amp;scores[0]);

printf("Enter a score: ");
scanf("%d", &amp;scores[1]);

printf("Enter a score: ");
scanf("%d", &amp;scores[2]);

printf("Enter a score: ");
scanf("%d", &amp;scores[3]);

printf("Enter a score: ");
scanf("%d", &amp;scores[4]);</code></pre>
<p>It works, but notice the only thing that changes each time is the index number (<code>[0]</code>, <code>[1]</code>, <code>[2]</code>...). That repetition is exactly what a loop is for.</p>
<hr>
<h4>With a Loop</h4>
<p>A <code>for</code> loop replaces all five copy-pasted blocks with one, using <code>i</code> as the index instead of a hardcoded number:</p>
<pre><code>int scores[5] = {0};

for(int i = 0; i &lt; 5; i++){
    printf("Enter a Score: ");
    scanf("%d", &amp;scores[i]);
}

for(int i = 0; i &lt; 5; i++){
    printf("%d ", scores[i]);
}</code></pre>
<hr>
<h4>Why the Loop Version Is Better</h4>
<table>
<tr><th></th><th>Without loop</th><th>With loop</th></tr>
<tr><td>Lines of code</td><td>grows with array size</td><td>stays the same no matter the size</td></tr>
<tr><td>Changing the array size</td><td>must add/remove printf+scanf pairs by hand</td><td>just change the loop condition (e.g. <code>i &lt; 10</code>)</td></tr>
<tr><td>Risk of typos</td><td>higher &mdash; easy to miss updating an index</td><td>lower &mdash; index is handled by <code>i</code></td></tr>
</table>
<p>Both versions do the exact same thing &mdash; the loop just does it without repeating yourself.</p>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch18 = next((c for c in c_lang["chapters"] if c.get("id") == "ch18"), None)

    if ch18 is None:
        print('[ERROR] No chapter with id "ch18" found. Nothing changed.')
        return

    ch18["title"] = NEW_TITLE
    ch18["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 18 title and notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
