#!/usr/bin/env python3
"""
Replaces Chapter 27's ("FILE WRITING") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter27_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 27: File Writing</h3>
<p>In this chapter, we learn how to write to a file from C.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>fopen() modes</li>
<li>fprintf() and fclose()</li>
<li>Example: writing text to a file</li>
</ul>
<hr>
<h4>Writing a File in C</h4>
<pre><code>FILE *pFile = fopen("path", "mode");</code></pre>
<table>
<tr><th>Mode</th><th>Meaning</th></tr>
<tr><td><code>"r"</code></td><td>read only (file must already exist)</td></tr>
<tr><td><code>"w"</code></td><td>write (creates file if not exists, OVERWRITES if it does exist)</td></tr>
<tr><td><code>"a"</code></td><td>append (adds to end, keeps old content)</td></tr>
</table>
<p><code>fprintf(pFile, "format", value)</code> works the same as <code>printf</code>, but writes to a FILE instead of printing to the screen.</p>
<p><code>fclose(pFile)</code> saves and closes the file &mdash; ALWAYS close after writing, or data may be lost.</p>
<p><strong>Always</strong> check <code>pFile != NULL</code> before writing. <code>fopen</code> returns <code>NULL</code> if the path is wrong or permissions don't allow creating the file.</p>
<hr>
<h4>Example: Writing Text to a File</h4>
<pre><code>// open file for writing -- creates Output.txt if not exists
// OVERWRITES content if file already exists
FILE *pFile = fopen("/data/data/com.termux/files/home/Output.txt", "w");

char text[] = "BOOTY BOOTY BOOTY\\nROCKIN' EVERYWHERE!";

// check if file opened successfully before writing
if(pFile == NULL) {
    printf("Error opening file\\n");
    return 1; // exit with error code
}

// fprintf writes to file instead of screen
// same format as printf: fprintf(file, "format", value)
fprintf(pFile, "%s", text);

printf("File was written successfully\\n");

fclose(pFile); // save and close -- never skip this!</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch27 = next((c for c in c_lang["chapters"] if c.get("id") == "ch27"), None)

    if ch27 is None:
        print('[ERROR] No chapter with id "ch27" found. Nothing changed.')
        return

    if "FILE WRITING" not in ch27.get("title", ""):
        print(f'[WARN] ch27 title is "{ch27.get("title")}", expected it to contain "FILE WRITING".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch27["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 27 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
