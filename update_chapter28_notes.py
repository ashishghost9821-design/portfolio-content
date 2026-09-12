#!/usr/bin/env python3
"""
Replaces Chapter 28's ("FILE READING") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter28_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 28: File Reading</h3>
<p>In this chapter, we learn how to read from a file in C.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>fopen() modes</li>
<li>fgets() and fclose()</li>
<li>Path notes for Linux/Termux</li>
<li>Example: reading a file line by line</li>
</ul>
<hr>
<h4>Reading a File in C</h4>
<pre><code>FILE *pFile = fopen("filename", "mode");</code></pre>
<table>
<tr><th>Mode</th><th>Meaning</th></tr>
<tr><td><code>"r"</code></td><td>read only (file must exist)</td></tr>
<tr><td><code>"w"</code></td><td>write (creates file, overwrites if exists)</td></tr>
<tr><td><code>"a"</code></td><td>append (adds to end of file)</td></tr>
</table>
<p><code>FILE *pFile</code> is a pointer to a FILE structure. <code>fopen</code> returns <code>NULL</code> if the file isn't found &mdash; ALWAYS check for <code>NULL</code> before using it!</p>
<p><code>fgets(buffer, size, pFile)</code> reads one line at a time into a buffer, and returns <code>NULL</code> when the file ends &mdash; loop with <code>while != NULL</code> to read all lines.</p>
<p><code>fclose(pFile)</code> closes the file when done &mdash; ALWAYS close files you open.</p>
<hr>
<h4>Path Notes (Linux/Termux)</h4>
<p>Use forward slashes <code>/</code>, NOT backslashes <code>\\</code> &mdash; backslashes are for Windows only! Simplest option: just use the filename if the file is in the same folder.</p>
<hr>
<h4>Example: Reading a File Line by Line</h4>
<pre><code>// open file for reading -- use forward slash on Linux
FILE *pFile = fopen("/data/data/com.termux/files/home/c-programming/input.txt", "r");
char buffer[1024] = {0}; // stores one line at a time

// ALWAYS check if file opened successfully
if(pFile == NULL) {
    printf("Could not open file\\n");
    return 1; // exit program with error code
}

// read line by line until end of file (fgets returns NULL)
while(fgets(buffer, sizeof(buffer), pFile) != NULL) {
    printf("%s", buffer); // buffer already has '\\n' from file
}

fclose(pFile); // close file when done</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch28 = next((c for c in c_lang["chapters"] if c.get("id") == "ch28"), None)

    if ch28 is None:
        print('[ERROR] No chapter with id "ch28" found. Nothing changed.')
        return

    if "FILE READING" not in ch28.get("title", ""):
        print(f'[WARN] ch28 title is "{ch28.get("title")}", expected it to contain "FILE READING".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch28["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 28 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
