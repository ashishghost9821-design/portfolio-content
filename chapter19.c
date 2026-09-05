#include <stdio.h>
#include <string.h>

/*
 * ╔══════════════════════════════════════════════╗
 *        C PROGRAMMING - ARRAY OF STRINGS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS AN ARRAY OF STRINGS?
 * ═══════════════════════════════════════════════
 * A 2D char array where each ROW is one string.
 *
 * Syntax:
 *   char name[rows][maxLength] = {"str1", "str2"};
 *
 *   rows      -> how many strings
 *   maxLength -> max characters per string (including '\0')
 *
 * Visual layout (fruits[4][10]):
 *   [0] -> "Apple\0   "   (5 chars + null + padding)
 *   [1] -> "Pineapple\0"  (9 chars + null)
 *   [2] -> "Banana\0   "  (6 chars + null + padding)
 *   [3] -> "Coconut\0  "  (7 chars + null + padding)
 *
 * Each row MUST fit within maxLength including '\0'
 * "Pineapple" = 9 chars + '\0' = 10 — exactly fits!
 */

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: hardcoded array of strings
     * modifying individual characters by index
     * ─────────────────────────────────────────── */
    char fruits[][10] = {"Apple",
                         "Pineapple",
                         "Banana",
                         "Coconut"};

    // modifying individual characters like a 2D array
    fruits[0][0] = 'e'; // Apple  -> epple
    fruits[0][4] = 'a'; // epple  -> eppla

    // sizeof(fruits) / sizeof(fruits[0]) = number of strings
    int size = sizeof(fruits) / sizeof(fruits[0]);

    // loop through and print each string with %s
    for(int i = 0; i < size; i++) {
        printf("%s\n", fruits[i]); // fruits[i] = one full string
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 2: user input — manual (one by one)
     * fgets reads each string into its own row
     * strlen strips the trailing '\n' fgets captures
     * ─────────────────────────────────────────── */
    char names[3][25] = {0}; // {0} initializes all to '\0'
    int rows = sizeof(names) / sizeof(names[0]); // = 3

    // WAY 1: manual input for each row
    printf("\n--- Enter 3 names (manual) ---\n");
    printf("Enter a name: ");
    fgets(names[0], sizeof(names[0]), stdin);
    names[0][strlen(names[0]) - 1] = '\0'; // strip '\n'

    printf("Enter a name: ");
    fgets(names[1], sizeof(names[1]), stdin);
    names[1][strlen(names[1]) - 1] = '\0';

    printf("Enter a name: ");
    fgets(names[2], sizeof(names[2]), stdin);
    names[2][strlen(names[2]) - 1] = '\0';

    // WAY 1: manual print for each row
    printf("\n--- Names entered (manual print) ---\n");
    printf("%s\n", names[0]);
    printf("%s\n", names[1]);
    printf("%s\n", names[2]);

    /* ───────────────────────────────────────────
     * EXAMPLE 3: same thing using for loops
     * cleaner — loop handles input and output
     * rows variable makes it easy to scale up
     * ─────────────────────────────────────────── */
    char names2[3][25] = {0};

    // WAY 2: loop input
    printf("\n--- Enter 3 names (loop input) ---\n");
    for(int i = 0; i < 3; i++) {
        printf("Enter a name: ");
        fgets(names2[i], sizeof(names2[i]), stdin);
        names2[i][strlen(names2[i]) - 1] = '\0'; // strip '\n'
    }

    // WAY 2: loop print
    printf("\n--- Names entered (loop print) ---\n");
    for(int i = 0; i < 3; i++) {
        printf("%s\n", names2[i]);
    }

    return 0;
}
