#!/usr/bin/env python3
"""
Replaces Chapter 10's ("FUNCTIONS") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter10_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 10: Functions</h3>
<p>In this chapter, we learn functions that return a value &mdash; a reusable block of code that runs when called, helping avoid repeating the same code.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a function</li>
<li>Example 1: math functions (return double)</li>
<li>Example 2: bool function (return bool)</li>
<li>Example 3: comparison function (return int)</li>
</ul>
<hr>
<h4>What is a Function?</h4>
<pre><code>return_type functionName(parameters) {
    return value;
}</code></pre>
<p>Must be defined ABOVE <code>main()</code> so the compiler knows it exists before it is called.</p>
<hr>
<h4>Example 1: Math Functions (return double)</h4>
<p>Return type = <code>double</code>, parameter = <code>double num</code> (the input value).</p>
<pre><code>double cube(double num) {
    return num * num * num; // num^3
}

double square(double num) {
    return num * num; // num^2
    // same as:
    // double result = num * num;
    // return result;
}</code></pre>
<p><em>Note:</em> replace <code>double</code> with <code>int</code> to work with integers.</p>
<hr>
<h4>Example 2: Bool Function (return bool)</h4>
<p>Return type = <code>bool</code> (needs <code>&lt;stdbool.h&gt;</code>), returns true or false based on a condition.</p>
<pre><code>bool ageCheck(int age) {
    if(age &gt;= 18) {
        return true;  // eligible
    }
    else {
        return false; // not eligible
    }
}</code></pre>
<hr>
<h4>Example 3: Comparison Function (return int)</h4>
<p>Takes two int parameters and returns the larger &mdash; shows functions can take multiple parameters.</p>
<pre><code>int getMax(int x, int y) {
    if(x &gt;= y) {
        return x; // x is larger or equal
    }
    else {
        return y; // y is larger
    }
}</code></pre>
<hr>
<h4>Calling the Functions</h4>
<p>Only ONE <code>main()</code> is allowed in a C program.</p>
<pre><code>int main() {

    // --- calling cube() and square() ---
    double x = cube(2.3);
    double y = cube(3.3);
    double z = cube(4.5);
    double s = square(5.0);

    printf("cube(2.3)   = %.3lf\\n", x);
    printf("cube(3.3)   = %.3lf\\n", y);
    printf("cube(4.5)   = %.3lf\\n", z);
    printf("square(5.0) = %.3lf\\n", s);

    // --- calling ageCheck() ---
    int age = 0;

    printf("\\nWhat is your age: ");
    scanf("%d", &amp;age);

    if(ageCheck(age)) {
        printf("You may sign up\\n");
    }
    else {
        printf("You must be 18+ to sign up!\\n");
    }

    // --- calling getMax() ---
    int max = getMax(2, 3);
    printf("\\nMax of 2 and 3: %d\\n", max);

    return 0;
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch10 = next((c for c in c_lang["chapters"] if c.get("id") == "ch10"), None)

    if ch10 is None:
        print('[ERROR] No chapter with id "ch10" found. Nothing changed.')
        return

    if "FUNCTIONS" not in ch10.get("title", ""):
        print(f'[WARN] ch10 title is "{ch10.get("title")}", expected it to contain "FUNCTIONS".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch10["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 10 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
