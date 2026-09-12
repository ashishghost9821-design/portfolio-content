import json, re, shutil

FILE = "content.json"
shutil.copy(FILE, FILE + ".bak")   # safety backup

with open(FILE) as f:
    data = json.load(f)

lang = data["languages"][0]
chapters = lang["chapters"]

# shift every existing chapter number up by 1 (ch1->ch2 ... ch30->ch31)
for ch in chapters:
    m = re.match(r"ch(\d+)$", ch["id"])
    num = int(m.group(1))
    ch["id"] = f"ch{num+1}"
    ch["title"] = re.sub(r"Chapter \d+:", f"Chapter {num+1}:", ch["title"])

new_chapter = {
    "id": "ch1",
    "title": "Chapter 1: BASICS",
    "desc": "Notes and examples on the structure of a C program, variables, and I/O.",
    "notes": "<p>See code example below for details on C basics.</p>",
    "codeExample": r"""#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════════════════╗
 *              C PROGRAMMING - BASICS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════════════════╝
 */

/* ──────────────────────────────────────────────────────────
 * SECTION 1: STRUCTURE OF A C PROGRAM
 * ──────────────────────────────────────────────────────────
 * #include <stdio.h> -> loads the Standard Input Output library
 * int main()         -> every program starts executing here
 * { }                -> curly braces mark the start/end of a block
 * ;                  -> every statement ends with a semicolon
 */

int main() {

    // This is a single-line comment, ignored by the compiler
    printf("Hello, World!\n"); // \n moves the cursor to a new line

    /* ──────────────────────────────────────────────────────
     * SECTION 2: VARIABLES & DATA TYPES
     * ──────────────────────────────────────────────────────
     * A variable is a labeled box that stores a value.
     * Syntax: data_type variable_name = value;
     */

    int   age   = 20;      // whole numbers
    float price = 19.99f;  // decimals
    char  grade = 'A';     // a single character

    printf("Age: %d\n",     age);
    printf("Price: %.2f\n", price);
    printf("Grade: %c\n",   grade);

    /* ──────────────────────────────────────────────────────
     * SECTION 3: OUTPUT - printf()
     * ──────────────────────────────────────────────────────
     * %d -> int      %f -> float/double
     * %c -> char     %s -> string
     */

    /* ──────────────────────────────────────────────────────
     * SECTION 4: INPUT - scanf()
     * ──────────────────────────────────────────────────────
     * scanf waits for the user to type a value.
     * & means "store the answer inside this variable".
     */

    printf("Enter your age: ");
    scanf("%d", &age);
    printf("You entered: %d\n", age);

    return 0;
}
"""
}

chapters.insert(0, new_chapter)

with open(FILE, "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done. {len(chapters)} chapters total. Backup saved as {FILE}.bak")
