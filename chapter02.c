#include <stdio.h>
#include <string.h>

int main() {

    /*
     * ╔══════════════════════════════════════════════╗
     *           C PROGRAMMING - USER INPUT
     *         Bro Code Tutorial | My Notes
     * ╚══════════════════════════════════════════════╝
     */

    /* ═══════════════════════════════════════════════
     * WHAT IS USER INPUT?
     * ═══════════════════════════════════════════════
     * User input allows the program to receive data
     * from the keyboard at runtime instead of
     * hardcoding values.
     *
     * Key functions:
     *   scanf()   -> reads formatted input (int, float, char)
     *   getchar() -> consumes leftover '\n' in input buffer
     *   fgets()   -> safely reads a full line of text (string)
     */

    /* ═══════════════════════════════════════════════
     * VARIABLE INITIALIZATION FOR INPUT
     * ═══════════════════════════════════════════════
     * Always initialize variables to a default/empty
     * value before taking input from the user.
     */

    int   age     = 0;      // default 0 for int
    float gpa     = 0.0f;   // 0.0f means float (f suffix)
    char  grade   = '\0';   // '\0' = null character (empty char)
    char  name[30]= "";     // char array with max 30 characters

    /* ═══════════════════════════════════════════════
     * scanf() — Reading int, float, char
     * ═══════════════════════════════════════════════
     * Syntax: scanf("specifier", &variable);
     *
     * IMPORTANT: use & (address-of operator) before
     * variable name so scanf knows WHERE to store value.
     * Exception: char[] arrays (already a pointer, no &)
     */

    printf("Enter your age: ");
    scanf("%d", &age);        // & required for int

    printf("Enter your gpa: ");
    scanf("%f", &gpa);        // & required for float

    printf("Enter your grade: ");
    scanf(" %c", &grade);     // & required for char
                              // space before %c clears leftover '\n'

    /* ═══════════════════════════════════════════════
     * getchar() — Clearing the Input Buffer
     * ═══════════════════════════════════════════════
     * After scanf(), a '\n' (newline) is left in the
     * input buffer. If fgets() runs next, it will
     * immediately read that '\n' and skip your input.
     * getchar() consumes that leftover '\n'.
     */

    (void)getchar(); // flush '\n' left by last scanf

    /* ═══════════════════════════════════════════════
     * fgets() — Reading a Full String (with spaces)
     * ═══════════════════════════════════════════════
     * Syntax: fgets(variable, size, stdin);
     *
     *   variable -> where to store the string
     *   size     -> max characters to read (use sizeof)
     *   stdin    -> means keyboard input
     *
     * WHY fgets instead of scanf("%s")?
     *   scanf("%s") stops at a space, so "Bro Code"
     *   would only store "Bro". fgets reads the full line.
     *
     * NOTE: fgets stores the '\n' at the end of input.
     * Fix: name[strlen(name) - 1] = '\0'
     *      replaces that '\n' with null terminator '\0'
     */

    printf("Enter your full name: ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0'; // remove trailing newline

    /* ═══════════════════════════════════════════════
     * PRINTING THE INPUT BACK
     * ═══════════════════════════════════════════════
     */

    printf("\n--- You Entered ---\n");
    printf("Age   : %d\n",   age);
    printf("GPA   : %.2f\n", gpa);
    printf("Grade : %c\n",   grade);
    printf("Name  : %s\n",   name);

    return 0;
}
