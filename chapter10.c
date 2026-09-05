#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *      C PROGRAMMING - RETURN VALUES & SCOPE
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * RETURN VALUES
 * ═══════════════════════════════════════════════
 * Functions can send a value BACK to where
 * they were called using return.
 *
 * Syntax:
 *   int add(int x, int y) {
 *       return x + y; // sends result back to caller
 *   }
 */

/* ═══════════════════════════════════════════════
 * VARIABLE SCOPE
 * ═══════════════════════════════════════════════
 * Scope = where a variable can be accessed.
 *
 * LOCAL scope  -> declared inside a function
 *                 only accessible within that function
 *                 destroyed when function ends
 *
 * GLOBAL scope -> declared outside all functions
 *                 accessible everywhere
 *                 hard to debug — avoid when possible
 *
 * Example of global (avoid this):
 *   int result = 0; // global — bad practice
 */

// returns sum of x and y
int add(int x, int y) {
    int result = x + y; // result is LOCAL to add()
    return result;
}

// returns difference of x and y
int subtract(int x, int y) {
    int result = x - y; // result is LOCAL to subtract()
    return result;
}

int main() {

    int x = 5;
    int y = 6;

    int result = subtract(x, y); // result is LOCAL to main()
    printf("subtract(%d, %d) = %d\n", x, y, result);

    result = add(x, y);
    printf("add(%d, %d) = %d\n", x, y, result);

    return 0;
}
