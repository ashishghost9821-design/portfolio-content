#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *            C PROGRAMMING - TYPEDEF
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS TYPEDEF?
 * ═══════════════════════════════════════════════
 * A reserved keyword that gives an existing
 * data type a custom "nickname".
 *
 * Syntax:
 *   typedef existing_type new_name;
 *
 * Benefits:
 *   -> simplifies complex or long type names
 *   -> improves code readability
 *   -> makes types more meaningful/descriptive
 */

/* ═══════════════════════════════════════════════
 * TYPEDEF DECLARATIONS (outside main)
 * ═══════════════════════════════════════════════
 *
 *   typedef int Number;
 *   -> "Number" is now an alias for int
 *
 *   typedef char String[50];
 *   -> "String" is now a char array of size 50
 *   -> alternative: char* (pointer, no size needed)
 *
 *   typedef char Initials[3];
 *   -> "Initials" is a char array of size 3
 *   -> holds 2 chars + '\0' null terminator
 */

typedef int    Number;
typedef char   String[50];  // char array of 50, no need to write char[50] again
typedef char   Initials[3]; // char array of 3 (2 letters + '\0')

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: typedef int -> Number
     * ─────────────────────────────────────────── */
    Number x = 3;
    Number y = 4;
    Number z = x + y;
    printf("%d\n", z); // 7

    /* ───────────────────────────────────────────
     * EXAMPLE 2: typedef char[50] -> String
     * ─────────────────────────────────────────── */
    String name = "Bro Code";
    printf("%s\n", name);

    /* ───────────────────────────────────────────
     * EXAMPLE 3: typedef char[3] -> Initials
     * cleaner than writing char user1[3] every time
     * holds 2 characters + '\0' null terminator
     *
     * WITHOUT typedef:  char user1[3] = "BC";
     * WITH typedef:     Initials user1 = "BC";
     * ─────────────────────────────────────────── */
    Initials user1 = "BC";
    Initials user2 = "SS";
    Initials user3 = "PS";
    Initials user4 = "ST";

    printf("%s\n", user1);
    printf("%s\n", user2);
    printf("%s\n", user3);
    printf("%s\n", user4);

    return 0;
}
