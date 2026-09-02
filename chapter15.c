#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *          C PROGRAMMING - NESTED LOOPS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS A NESTED LOOP?
 * ═══════════════════════════════════════════════
 * A loop inside another loop.
 * The inner loop completes ALL its iterations
 * for EACH single iteration of the outer loop.
 *
 * IMPORTANT: use different variable names
 * for each loop (i, j, x, y) to avoid conflicts.
 */

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: single loop
     * prints 1 2 3 4 5 6 7 8 9 on one line
     * ─────────────────────────────────────────── */
    for(int i = 1; i < 10; i++) {
        printf("%d ", i);
    }
    printf("\n"); // move to next line after loop

    /* ───────────────────────────────────────────
     * EXAMPLE 2: nested loop
     * outer loop (j) runs 3 times
     * inner loop (i) runs 9 times per outer cycle
     * prints the same row of numbers 3 times
     * ─────────────────────────────────────────── */
    for(int j = 1; j < 4; j++) {       // outer: 3 rows
        for(int i = 1; i < 10; i++) {  // inner: 9 columns
            printf("%d ", i);
        }
        printf("\n"); // new line after each row
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 3: multiplication table
     * outer loop (y) = row    (1 to 10)
     * inner loop (x) = column (1 to 10)
     * x * y = value at each cell
     *
     * %3d = print int with 3 spaces width
     *       keeps columns aligned neatly
     * ─────────────────────────────────────────── */
    for(int y = 1; y <= 10; y++) {      // outer: each row
        for(int x = 1; x <= 10; x++) { // inner: each column
            printf("%3d ", x * y);      // %3d aligns columns
        }
        printf("\n"); // new line after each row
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 4: user input grid
     * user chooses rows, columns, and symbol
     * outer loop controls rows (r)
     * inner loop controls columns (c)
     * NEVER use same variable name in nested loops!
     * ─────────────────────────────────────────── */
    int  rows    = 0;
    int  columns = 0;
    char symbol  = '\0';

    printf("Enter the # of rows: ");
    scanf("%d", &rows);

    printf("Enter the # of columns: ");
    scanf("%d", &columns);

    printf("Enter a symbol to use: ");
    scanf(" %c", &symbol);

    for(int r = 0; r < rows; r++) {        // outer: controls rows
        for(int c = 0; c < columns; c++) { // inner: controls columns
            printf("%c", symbol);
        }
        printf("\n"); // new line after each row
    }

    return 0;
}
