#!/usr/bin/env python3
"""
Replaces Chapter 24's ("STRUCT") notes field with the interlaced
explanation + code-block format. Makes a .bak backup first.
Run from portfolio-content/:
    python3 update_chapter24_notes.py
"""
import json
import shutil

PATH = "content.json"

NEW_NOTES = """<h3>Chapter 24: Struct</h3>
<p>In this chapter, we learn <code>struct</code> &mdash; a user-defined data type that groups multiple variables of DIFFERENT types under one name.</p>
<p><strong>Topics Covered:</strong></p>
<ul>
<li>What is a struct</li>
<li>Example: initializing with values</li>
<li>Example: {0} initialization</li>
<li>Example: strcpy() to set a string member</li>
<li>Printing structs with a function</li>
</ul>
<hr>
<h4>What is a Struct?</h4>
<p>Think of it like a custom blueprint/template. Each variable inside is called a "member" or "field".</p>
<pre><code>typedef struct {
    type member1;
    type member2;
} TypeName;</code></pre>
<p>Accessing members: <code>variable.member</code>, e.g. <code>student1.name</code>, <code>student1.age</code>, <code>student1.gpa</code>.</p>
<p><strong>Important:</strong> every member line MUST end with <code>;</code> &mdash; missing it is a very common bug with structs!</p>
<pre><code>typedef struct {
    char  name[50];
    int   age;
    float gpa;
    bool  isFullTime; // DON'T forget the semicolon here!
} Student;</code></pre>
<hr>
<h4>Function Prototype</h4>
<p>Passing a struct to a function works like passing any other variable &mdash; the function gets its own COPY of the struct (not the original).</p>
<pre><code>void printStudent(Student student);</code></pre>
<hr>
<h4>Example 1: Initialize Struct with Values</h4>
<p>Values must match member ORDER exactly: <code>{name, age, gpa, isFullTime}</code>.</p>
<pre><code>Student student1 = {"Spongebob", 38, 2.5, true};
Student student2 = {"Patrick",   36, 1.0, false};</code></pre>
<hr>
<h4>Example 2: {0} Initialization</h4>
<p><code>{0}</code> sets ALL members to their zero equivalent:</p>
<table>
<tr><th>Type</th><th>Zero value</th></tr>
<tr><td><code>int</code></td><td>0</td></tr>
<tr><td><code>float</code></td><td>0.0</td></tr>
<tr><td><code>char</code></td><td><code>\\0</code> (empty string)</td></tr>
<tr><td><code>bool</code></td><td>false</td></tr>
</table>
<p>Useful when you want to fill values later.</p>
<pre><code>Student student3 = {0};</code></pre>
<hr>
<h4>Example 3: strcpy() to Set a String Member</h4>
<p>You CANNOT assign a string with <code>=</code> after init &mdash; <code>student3.name = "Sandy";</code> is an ERROR. <code>strcpy()</code> copies a string INTO the char array instead: <code>strcpy(destination, source);</code> (needs <code>&lt;string.h&gt;</code>).</p>
<pre><code>strcpy(student3.name, "Sandy"); // copy "Sandy" into student3.name
student3.age        = 27;
student3.gpa        = 4.0f;
student3.isFullTime = true;</code></pre>
<hr>
<h4>Example 4: {0} Then Filled Member by Member</h4>
<pre><code>Student student4 = {0};
strcpy(student4.name, "Squidward");
student4.age        = 40;
student4.gpa        = 2.0f;
student4.isFullTime = false;

// print all students using the function
printStudent(student1);
printStudent(student2);
printStudent(student3);
printStudent(student4);</code></pre>
<hr>
<h4>Function Definition</h4>
<p>Access each member using dot notation: <code>student.member</code>. Ternary is used for the bool member to print "Yes" or "No".</p>
<pre><code>void printStudent(Student student) {
    printf("Name:      %s\\n",  student.name);
    printf("Age:       %d\\n",  student.age);
    printf("GPA:       %.2f\\n", student.gpa);
    printf("Full-time: %s\\n",  (student.isFullTime) ? "Yes" : "No");
    printf("\\n");
}</code></pre>"""

def main():
    shutil.copy(PATH, PATH + ".bak")
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    c_lang = next(l for l in data["languages"] if l.get("name") == "C")
    ch24 = next((c for c in c_lang["chapters"] if c.get("id") == "ch24"), None)

    if ch24 is None:
        print('[ERROR] No chapter with id "ch24" found. Nothing changed.')
        return

    if "STRUCT" not in ch24.get("title", ""):
        print(f'[WARN] ch24 title is "{ch24.get("title")}", expected it to contain "STRUCT".')
        print("       Stopping without changes so we don't overwrite the wrong chapter.")
        return

    ch24["notes"] = NEW_NOTES

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Chapter 24 notes updated.")
    print(f"Backup saved as {PATH}.bak")

if __name__ == "__main__":
    main()
