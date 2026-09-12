#!/usr/bin/env python3
"""
Replaces Chapter 29's ("DYNAMIC MEMORY (malloc)") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter29_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 29: Dynamic Memory (malloc)</h3>
<p>In this chapter, we learn dynamic memory allocation with <code>malloc()</code>.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>Static vs dynamic memory</li>
<li>malloc() syntax</li>
<li>Dangling pointers</li>
<li>Example: allocating grades at runtime</li>
</ul>
<hr>
<h4>Static vs Dynamic Memory</h4>
<table>
<tr><th>Type</th><th>Details</th></tr>
<tr><td>Static (normal arrays)</td><td><code>char grades[5];</code> &mdash; size must be known at compile time, fixed size, cannot change while running</td></tr>
<tr><td>Dynamic (malloc)</td><td><code>char *grades = malloc(number * sizeof(char));</code> &mdash; size decided at RUNTIME, you choose how much memory to rent from the OS, must manually <code>free()</code> when done</td></tr>
</table>
<p>Think of it like renting a hotel room: <code>malloc()</code> = check in (rent memory), <code>free()</code> = check out (return memory to OS). If you forget <code>free()</code>, that's a memory leak (room never freed).</p>
<hr>
<h4>malloc() Syntax</h4>
<pre><code>void *malloc(size_t size);</code></pre>
<p><code>size_t</code> = number of BYTES to allocate.</p>
<pre><code>char *grades = malloc(number * sizeof(char));
//    ^               ^      ^          ^
//    |               |      |          sizeof(char) = 1 byte
//    |               |      number of elements
//    char pointer    malloc = allocate bytes</code></pre>
<p><code>malloc</code> returns <code>NULL</code> if allocation fails &mdash; ALWAYS check for <code>NULL</code> before using the pointer!</p>
<table>
<tr><th>Type</th><th>Bytes</th></tr>
<tr><td><code>sizeof(char)</code></td><td>1 byte</td></tr>
<tr><td><code>sizeof(int)</code></td><td>4 bytes</td></tr>
<tr><td><code>sizeof(float)</code></td><td>4 bytes</td></tr>
</table>
<hr>
<h4>Dangling Pointer</h4>
<p>After <code>free(grades)</code>, the pointer still holds the old address &mdash; but that memory is freed. Using it would be undefined behavior.</p>
<p>Fix: set the pointer to <code>NULL</code> after <code>free()</code>: <code>grades = NULL;</code>. Now any accidental use will crash clearly instead of silently corrupting memory.</p>
<hr>
<h4>Example: Allocating Grades at Runtime</h4>
<pre><code>int number = 0;
printf("Enter the number of grades: ");
scanf("%d", &amp;number);

// allocate memory for 'number' chars at runtime
char *grades = malloc(number * sizeof(char));

// ALWAYS check malloc result before using
if(grades == NULL) {
    printf("Memory allocation failed\\n");
    return 1;
}

// fill the dynamically allocated array
for(int i = 0; i &lt; number; i++) {
    printf("Enter grade #%d: ", i + 1);
    scanf(" %c", &amp;grades[i]); // space before %c clears '\\n'
}

// print all grades
printf("\\nGrades entered: ");
for(int i = 0; i &lt; number; i++) {
    printf("%c ", grades[i]);
}
printf("\\n");

free(grades);   // return rented memory back to OS
grades = NULL;  // avoid dangling pointer</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch29 = next((c for c in c_lang["chapters"] if c.get("id") == "ch29"), None)

    if ch29 is None:
        print('[ERROR] No chapter with id "ch29" found. Nothing changed.')
        return

    if "DYNAMIC MEMORY" not in ch29.get("title", ""):
        print(f'[WARN] ch29 title is "{ch29.get("title")}", expected it to contain "DYNAMIC MEMORY".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch29["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 29 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
