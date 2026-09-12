#!/usr/bin/env python3
"""
Replaces Chapter 31's ("REALLOC") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter31_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 31: Realloc</h3>
<p>In this chapter, we learn <code>realloc()</code> &mdash; reallocation, which resizes previously allocated memory.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is realloc()</li>
<li>Why use a temp pointer</li>
<li>malloc &rarr; calloc &rarr; realloc summary</li>
<li>Example: resizing a prices array</li>
</ul>
<hr>
<h4>What is realloc()?</h4>
<pre><code>float *temp = realloc(ptr, newSize);</code></pre>
<p><code>ptr</code> = pointer to existing malloc/calloc memory. <code>newSize</code> = new total size in BYTES.</p>
<p>What <code>realloc()</code> does:</p>
<ul>
<li>if <code>newSize</code> is BIGGER: extends memory, keeps old data</li>
<li>if <code>newSize</code> is SMALLER: shrinks memory, trims old data</li>
<li>may move memory to a new location if needed</li>
<li>returns <code>NULL</code> if reallocation fails</li>
</ul>
<hr>
<h4>Why Use a Temp Pointer?</h4>
<p><code>realloc</code> can return <code>NULL</code> on failure. If you do <code>prices = realloc(prices, ...)</code> and it fails, <code>prices</code> becomes <code>NULL</code> &mdash; the original data is LOST forever (memory leak!).</p>
<p>Safe pattern:</p>
<pre><code>float *temp = realloc(prices, newSize);
if(temp == NULL) { /* handle error, prices still safe */ }
else             { prices = temp; temp = NULL; }</code></pre>
<hr>
<h4>malloc &rarr; calloc &rarr; realloc Summary</h4>
<table>
<tr><th>Function</th><th>Behavior</th></tr>
<tr><td><code>malloc(size)</code></td><td>allocate, garbage values</td></tr>
<tr><td><code>calloc(count, size)</code></td><td>allocate, zeroed values</td></tr>
<tr><td><code>realloc(ptr, size)</code></td><td>resize existing allocation</td></tr>
</table>
<hr>
<h4>Example: Resizing a Prices Array</h4>
<pre><code>int number = 0;
printf("Enter the number of prices: ");
scanf("%d", &amp;number);

// initial allocation with malloc
float *prices = malloc(number * sizeof(float));

if(prices == NULL) {
    printf("Memory allocation failed\\n");
    return 1;
}

// fill initial prices
for(int i = 0; i &lt; number; i++) {
    printf("Enter price #%d: ", i + 1);
    scanf("%f", &amp;prices[i]);
}

// ask for new size
int newNumber = 0;
printf("Enter a new number of prices: ");
scanf("%d", &amp;newNumber);

// use temp pointer -- NEVER do prices = realloc(prices, ...)
// if realloc fails and returns NULL, original data is lost
float *temp = realloc(prices, newNumber * sizeof(float));

if(temp == NULL) {
    printf("Could not reallocate memory!\\n");
    // prices still valid here -- original data safe
}
else {
    prices = temp; // realloc succeeded, update prices
    temp   = NULL; // avoid dangling temp pointer

    // fill only the NEW slots (old ones already have data)
    for(int i = number; i &lt; newNumber; i++) {
        printf("Enter price #%d: ", i + 1);
        scanf("%f", &amp;prices[i]);
    }

    // print all prices
    printf("\\nAll prices:\\n");
    for(int i = 0; i &lt; newNumber; i++) {
        printf("$%.2f\\n", prices[i]);
    }
}

free(prices);   // return memory to OS
prices = NULL;  // avoid dangling pointer</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch31 = next((c for c in c_lang["chapters"] if c.get("id") == "ch31"), None)

    if ch31 is None:
        print('[ERROR] No chapter with id "ch31" found. Nothing changed.')
        return

    if "REALLOC" not in ch31.get("title", ""):
        print(f'[WARN] ch31 title is "{ch31.get("title")}", expected it to contain "REALLOC".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch31["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 31 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
