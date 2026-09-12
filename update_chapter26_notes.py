#!/usr/bin/env python3
"""
Replaces Chapter 26's ("POINTERS") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter26_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 26: Pointers</h3>
<p>In this chapter, we learn pointers &mdash; a variable that stores the MEMORY ADDRESS of another variable.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a pointer</li>
<li>Why use pointers (pass by reference)</li>
<li>Example: reading a pointer's address and value</li>
<li>Pass by reference in a function</li>
</ul>
<hr>
<h4>What is a Pointer?</h4>
<p>Every variable lives somewhere in RAM. That location has an address (like a house address). A pointer stores that address.</p>
<pre><code>int *pAge = &amp;age;
//   ^     ^     ^
//   |     |     &amp; = "address of" operator
//   |     |         gives the memory address of age
//   |     p = naming convention for pointers
//   int* = pointer to an int</code></pre>
<table>
<tr><th>Operator</th><th>Meaning</th></tr>
<tr><td><code>&amp;variable</code></td><td>gives ADDRESS of variable (referencing)</td></tr>
<tr><td><code>*pointer</code></td><td>gives VALUE at that address (dereferencing)</td></tr>
</table>
<hr>
<h4>Why Use Pointers?</h4>
<p>Normally when you pass a variable to a function, C makes a COPY &mdash; changes inside don't affect the original. With pointers, you pass the ADDRESS &mdash; the function changes the ORIGINAL variable directly. This is called "pass by reference".</p>
<p>Visual:</p>
<pre><code>int age = 25;
age  -&gt; value: 25,  address: 0x7fff5c (example)
pAge -&gt; value: 0x7fff5c (stores age's address)
*pAge -&gt; 25 (goes to that address and reads value)</code></pre>
<hr>
<h4>Example: Reading a Pointer's Address and Value</h4>
<pre><code>void birthday(int *age); // takes a pointer to int

int main() {

    int age = 25;

    // &amp; gives the memory address of age
    printf("Address of age: %p\\n", &amp;age);

    // pointer stores that address
    int *pAge = &amp;age;
    printf("pAge holds:     %p\\n", pAge);   // same address
    printf("Value at pAge:  %d\\n", *pAge);  // 25 (dereferencing)

    // pass the POINTER (address) to function
    // function will change the original age variable
    birthday(pAge);
    printf("After birthday: %d years old\\n", age); // age is now 26

    return 0;
}</code></pre>
<hr>
<h4>Pass by Reference</h4>
<p><code>(*age)++</code> means: go to the address stored in the <code>age</code> pointer, get the value there, then increment it by 1.</p>
<p>Parentheses around <code>*age</code> are important:</p>
<table>
<tr><th>Expression</th><th>Effect</th></tr>
<tr><td><code>(*age)++</code></td><td>increment the VALUE at the address &mdash; correct</td></tr>
<tr><td><code>*age++</code></td><td>increment the ADDRESS itself &mdash; wrong</td></tr>
</table>
<pre><code>void birthday(int *age) {
    (*age)++; // dereference then increment original value
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch26 = next((c for c in c_lang["chapters"] if c.get("id") == "ch26"), None)

    if ch26 is None:
        print('[ERROR] No chapter with id "ch26" found. Nothing changed.')
        return

    if "POINTERS" not in ch26.get("title", ""):
        print(f'[WARN] ch26 title is "{ch26.get("title")}", expected it to contain "POINTERS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch26["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 26 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
