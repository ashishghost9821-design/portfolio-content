#!/usr/bin/env python3
"""
Replaces Chapter 3's ("USER INPUT") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter3_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 3: User Input</h3>
<p>In this chapter, we learn how a program can receive data from the keyboard at runtime instead of hardcoding values.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is user input</li>
<li>Initializing variables for input</li>
<li><code>scanf()</code> for int, float, char</li>
<li><code>getchar()</code> to clear the input buffer</li>
<li><code>fgets()</code> for reading full strings</li>
</ul>
<hr>
<h4>What is User Input?</h4>
<p>Key functions used to read input:</p>
<table>
<tr><th>Function</th><th>Purpose</th></tr>
<tr><td><code>scanf()</code></td><td>reads formatted input (int, float, char)</td></tr>
<tr><td><code>getchar()</code></td><td>consumes leftover <code>\\n</code> in the input buffer</td></tr>
<tr><td><code>fgets()</code></td><td>safely reads a full line of text (string)</td></tr>
</table>
<hr>
<h4>Initializing Variables for Input</h4>
<p>Always initialize variables to a default/empty value before taking input from the user.</p>
<pre><code>int   age     = 0;      // default 0 for int
float gpa     = 0.0f;   // 0.0f means float (f suffix)
char  grade   = '\\0';   // '\\0' = null character (empty char)
char  name[30]= "";     // char array with max 30 characters</code></pre>
<hr>
<h4>scanf() &mdash; Reading int, float, char</h4>
<pre><code>scanf("specifier", &amp;variable);</code></pre>
<p><strong>Important:</strong> use <code>&amp;</code> (address-of operator) before the variable name so <code>scanf</code> knows WHERE to store the value. Exception: <code>char[]</code> arrays are already a pointer, so no <code>&amp;</code>.</p>
<pre><code>printf("Enter your age: ");
scanf("%d", &amp;age);        // &amp; required for int

printf("Enter your gpa: ");
scanf("%f", &amp;gpa);        // &amp; required for float

printf("Enter your grade: ");
scanf(" %c", &amp;grade);     // &amp; required for char
                          // space before %c clears leftover '\\n'</code></pre>
<hr>
<h4>getchar() &mdash; Clearing the Input Buffer</h4>
<p>After <code>scanf()</code>, a <code>\\n</code> (newline) is left in the input buffer. If <code>fgets()</code> runs next, it will immediately read that <code>\\n</code> and skip your input. <code>getchar()</code> consumes that leftover <code>\\n</code>.</p>
<pre><code>(void)getchar(); // flush '\\n' left by last scanf</code></pre>
<hr>
<h4>fgets() &mdash; Reading a Full String (with spaces)</h4>
<pre><code>fgets(variable, size, stdin);</code></pre>
<table>
<tr><th>Argument</th><th>Meaning</th></tr>
<tr><td><code>variable</code></td><td>where to store the string</td></tr>
<tr><td><code>size</code></td><td>max characters to read (use <code>sizeof</code>)</td></tr>
<tr><td><code>stdin</code></td><td>means keyboard input</td></tr>
</table>
<p><strong>Why fgets instead of scanf("%s")?</strong> <code>scanf("%s")</code> stops at a space, so <code>"Bro Code"</code> would only store <code>"Bro"</code>. <code>fgets</code> reads the full line.</p>
<p><em>Note:</em> <code>fgets</code> stores the <code>\\n</code> at the end of input. Fix: <code>name[strlen(name) - 1] = '\\0'</code> replaces that <code>\\n</code> with a null terminator <code>\\0</code>.</p>
<pre><code>printf("Enter your full name: ");
fgets(name, sizeof(name), stdin);
name[strlen(name) - 1] = '\\0'; // remove trailing newline</code></pre>
<hr>
<h4>Printing the Input Back</h4>
<pre><code>printf("\\n--- You Entered ---\\n");
printf("Age   : %d\\n",   age);
printf("GPA   : %.2f\\n", gpa);
printf("Grade : %c\\n",   grade);
printf("Name  : %s\\n",   name);</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch3 = next((c for c in c_lang["chapters"] if c.get("id") == "ch3"), None)

    if ch3 is None:
        print('[ERROR] No chapter with id "ch3" found. Nothing changed.')
        return

    if "USER INPUT" not in ch3.get("title", ""):
        print(f'[WARN] ch3 title is "{ch3.get("title")}", expected it to contain "USER INPUT".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch3["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 3 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
