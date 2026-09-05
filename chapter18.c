#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *          C PROGRAMMING - 2D ARRAYS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS A 2D ARRAY?
 * ═══════════════════════════════════════════════
 * An array where each element is itself an array.
 * Think of it as a TABLE with rows and columns.
 *
 * Syntax:
 *   type name[rows][columns] = {{...}, {...}, {...}};
 *
 * You can leave rows empty [] — compiler counts them.
 * You MUST always specify columns.
 *
 * Accessing elements:
 *   name[row][column]
 *   name[0][0] = first row, first column
 *   name[1][2] = second row, third column
 *
 * Visual layout:
 *             col0  col1  col2
 *   row0  ->  [1]   [2]   [3]
 *   row1  ->  [4]   [5]   [6]
 *   row2  ->  [7]   [8]   [9]
 */

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: 3x3 int 2D array
     * accessing elements manually by index
     * ─────────────────────────────────────────── */
    int numbers[][3] = {{1, 2, 3},
                        {4, 5, 6},
                        {7, 8, 9}};

    // row 0
    printf("%d", numbers[0][0]); // 1
    printf("%d", numbers[0][1]); // 2
    printf("%d\n", numbers[0][2]); // 3

    // row 1
    printf("%d", numbers[1][0]); // 4
    printf("%d", numbers[1][1]); // 5
    printf("%d\n", numbers[1][2]); // 6

    // row 2
    printf("%d", numbers[2][0]); // 7
    printf("%d", numbers[2][1]); // 8
    printf("%d\n", numbers[2][2]); // 9

    /* ───────────────────────────────────────────
     * EXAMPLE 2: 4x3 int 2D array with nested loop
     * outer loop = rows, inner loop = columns
     * much cleaner than accessing manually
     * ─────────────────────────────────────────── */
    int number[][3] = {{1,  2,  3},
                       {4,  5,  6},
                       {7,  8,  9},
                       {10, 11, 12}};

    for(int i = 0; i < 4; i++) {        // i = row    (0 to 3)
        for(int j = 0; j < 3; j++) {    // j = column (0 to 2)
            printf("%3d", number[i][j]); // %3d keeps columns aligned
        }
        printf("\n"); // new line after each row
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 3: 2D char array — numpad
     * same concept but with characters
     * shows 2D arrays work with any data type
     * ─────────────────────────────────────────── */
    char numpad[][3] = {{'1', '2', '3'},
                        {'4', '5', '6'},
                        {'7', '8', '9'},
                        {'*', '0', '#'}};

    printf("\n--- Numpad ---\n");
    for(int i = 0; i < 4; i++) {     // 4 rows
        for(int j = 0; j < 3; j++) { // 3 columns
            printf("%c ", numpad[i][j]);
        }
        printf("\n"); // new line after each row
    }

    return 0;
}
