#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *            C PROGRAMMING - ARRAYS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS AN ARRAY?
 * ═══════════════════════════════════════════════
 * A fixed size collection of elements of the
 * SAME data type. Similar to a variable, but
 * holds more than one value.
 *
 * Syntax:
 *   type name[] = {val1, val2, val3};
 *
 * Indexing starts at 0, NOT 1:
 *   numbers[0] = first element
 *   numbers[1] = second element
 *   numbers[4] = fifth (last) element
 *
 * NEVER access index equal to or beyond the size:
 *   int numbers[5] -> valid: [0][1][2][3][4]
 *   numbers[5]     -> OUT OF BOUNDS = undefined behavior!
 */

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: int array
     * ─────────────────────────────────────────── */
    int numbers[] = {10, 20, 30, 40, 50}; // size = 5, index 0 to 4

    // accessing individual elements by index
    printf("%d\n", numbers[0]); // 10
    printf("%d\n", numbers[1]); // 20
    printf("%d\n", numbers[2]); // 30
    printf("%d\n", numbers[3]); // 40
    printf("%d\n", numbers[4]); // 50
    // numbers[5] -> WARNING: out of bounds! array ends at [4]

    /* ───────────────────────────────────────────
     * EXAMPLE 2: char array (individual characters)
     * ─────────────────────────────────────────── */
    char grade[] = {'A', 'B', 'C', 'D', 'F'}; // size = 5

    printf("%c\n", grade[0]); // A
    printf("%c\n", grade[1]); // B

    /* ───────────────────────────────────────────
     * EXAMPLE 3: char array as string
     * double quotes = string, stored as char array
     * ─────────────────────────────────────────── */
    char name[] = "Ashish Ghost"; // compiler auto sets size

    printf("%c\n", name[0]); // A (first character only)

    /* ───────────────────────────────────────────
     * EXAMPLE 4: modifying array elements
     * arrays are NOT read-only, values can change
     * ─────────────────────────────────────────── */
    numbers[0] = 100; // overwrite index 0
    numbers[1] = 90;
    numbers[2] = 80;

    printf("%d\n", numbers[0]); // now 100
    printf("%d\n", numbers[1]); // now 90
    printf("%d\n", numbers[2]); // now 80

    /* ───────────────────────────────────────────
     * EXAMPLE 5: loop through arrays
     * much better than printing one by one
     * ─────────────────────────────────────────── */

    // loop through grade[] char array
    for(int i = 0; i < 5; i++) {
        printf("%c\n", grade[i]); // grade NOT grades (typo fix)
    }

    // loop through numbers[] int array
    for(int i = 0; i < 5; i++) {
        printf("%d\n", numbers[i]);
    }

    // loop through name[] string char by char
    for(int i = 0; i < 12; i++) {
        printf("%c\n", name[i]);
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 6: sizeof() with arrays
     * ───────────────────────────────────────────
     * sizeof(numbers)    -> total bytes of whole array
     *                       5 elements * 4 bytes = 20
     *
     * sizeof(numbers[0]) -> bytes of ONE element = 4
     *
     * sizeof(numbers) / sizeof(numbers[0])
     *                    -> total elements in array
     *                       20 / 4 = 5
     *
     * WHY USE THIS?
     * If you change the array size later, the loop
     * automatically adjusts — no need to update manually.
     */

    printf("Total bytes:     %zu\n", sizeof(numbers));      // 20
    printf("One element:     %zu\n", sizeof(numbers[0]));   // 4
    printf("Number of items: %zu\n", sizeof(numbers) / sizeof(numbers[0])); // 5

    // BEST PRACTICE: use sizeof to get size automatically
    int size = sizeof(numbers) / sizeof(numbers[0]);
    for(int i = 0; i < size; i++) {
        printf("%d\n", numbers[i]);
    }

    // OR write it directly inside the for loop
    // for(int i = 0; i < sizeof(numbers) / sizeof(numbers[0]); i++) {
    //     printf("%d\n", numbers[i]);
    // }

    return 0;
}
