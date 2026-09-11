#!/usr/bin/env python3
"""
Replaces Chapter 6's ("SWITCH STATEMENT") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter6_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 6: Switch Statement</h3>
<p>In this chapter, we learn <code>switch</code> as an alternative to many <code>if</code>/<code>else</code> statements &mdash; more efficient when checking a single variable against fixed integer or char values.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a switch statement</li>
</ul>
<hr>
<h4>What is a Switch Statement?</h4>
<pre><code>switch(variable) {
    case value1:
        // code
        break;   // stops fall-through to next case
    case value2:
        // code
        break;
    default:     // runs if no case matches
        // code
}</code></pre>
<p><strong>Important:</strong> always add <code>break</code> after each case, or it will fall through and run the next case too.</p>
<pre><code>int dayOfWeek = 0;

printf("Enter a day of the week (1-7): ");
scanf("%d", &amp;dayOfWeek);

switch(dayOfWeek) {
    case 1:  printf("It is Monday\\n");    break;
    case 2:  printf("It is Tuesday\\n");   break;
    case 3:  printf("It is Wednesday\\n"); break;
    case 4:  printf("It is Thursday\\n");  break;
    case 5:  printf("It is Friday\\n");    break;
    case 6:  printf("It is Saturday\\n");  break;
    case 7:  printf("It is Sunday\\n");    break;
    default: printf("Please enter a valid number (1-7)\\n"); break;
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch6 = next((c for c in c_lang["chapters"] if c.get("id") == "ch6"), None)

    if ch6 is None:
        print('[ERROR] No chapter with id "ch6" found. Nothing changed.')
        return

    if "SWITCH" not in ch6.get("title", ""):
        print(f'[WARN] ch6 title is "{ch6.get("title")}", expected it to contain "SWITCH".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch6["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 6 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
