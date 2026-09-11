#!/usr/bin/env python3
"""
Replaces Chapter 8's ("LOGICAL OPERATORS") notes field with the
interlaced explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter8_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 8: Logical Operators</h3>
<p>In this chapter, we learn how logical operators combine or modify boolean expressions.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What are logical operators</li>
<li>Example: &amp;&amp; (AND)</li>
<li>Example: || (OR)</li>
<li>Example: bool with if/else</li>
<li>Example: ! (NOT)</li>
</ul>
<hr>
<h4>What are Logical Operators?</h4>
<table>
<tr><th>Operator</th><th>Meaning</th><th>True when</th></tr>
<tr><td><code>&amp;&amp;</code></td><td>AND</td><td>BOTH conditions are true</td></tr>
<tr><td><code>||</code></td><td>OR</td><td>AT LEAST one is true</td></tr>
<tr><td><code>!</code></td><td>NOT</td><td>condition is flipped</td></tr>
</table>
<pre><code>true  &amp;&amp; true  = true
true  &amp;&amp; false = false
false || true  = true
false || false = false
!true          = false
!false         = true</code></pre>
<hr>
<h4>Example 1: &amp;&amp; (AND)</h4>
<p>Both conditions must be true to enter the if block &mdash; here, <code>temp</code> must be &gt; 0 AND &lt; 30 to be GOOD.</p>
<pre><code>int temp = 0;

printf("What is the current temperature: ");
scanf("%d", &amp;temp);

if(temp &gt; 0 &amp;&amp; temp &lt; 30) {
    printf("The temperature is GOOD\\n");
}
else {
    printf("The temperature is BAD\\n");
}</code></pre>
<hr>
<h4>Example 2: || (OR)</h4>
<p>True if <code>temp &lt;= 0</code> OR <code>temp &gt;= 30</code> (either bad extreme):</p>
<pre><code>if(temp &lt;= 0 || temp &gt;= 30) {
    printf("The temperature is BAD\\n");
}
else {
    printf("The temperature is GOOD\\n");
}</code></pre>
<hr>
<h4>Example 3: bool with if/else</h4>
<pre><code>bool isSunny = true;

if(isSunny) {
    printf("It is sunny outside\\n");
}
else {
    printf("It is cloudy outside\\n");
}</code></pre>
<hr>
<h4>Example 4: ! (NOT)</h4>
<p>Flips the bool value:</p>
<pre><code>if(!isSunny) {           // if NOT sunny
    printf("It is cloudy outside\\n");
}
else {
    printf("It is sunny outside\\n");
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch8 = next((c for c in c_lang["chapters"] if c.get("id") == "ch8"), None)

    if ch8 is None:
        print('[ERROR] No chapter with id "ch8" found. Nothing changed.')
        return

    if "LOGICAL" not in ch8.get("title", ""):
        print(f'[WARN] ch8 title is "{ch8.get("title")}", expected it to contain "LOGICAL".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch8["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 8 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
