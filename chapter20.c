#include <stdio.h>
#include <stdbool.h>

/*
 * ╔══════════════════════════════════════════════╗
 *        C PROGRAMMING - TERNARY OPERATOR
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS THE TERNARY OPERATOR?
 * ═══════════════════════════════════════════════
 * A shorthand for a simple if/else statement.
 * Returns one of two values based on a condition.
 *
 * Syntax:
 *   (condition) ? value_if_true : value_if_false;
 *
 * Equivalent to:
 *   if(condition) { value_if_true }
 *   else          { value_if_false }
 *
 * Best used for SHORT, SIMPLE conditions.
 * For complex logic, use regular if/else.
 */

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: find max of two numbers
     * if x > y is true  -> max = x
     * if x > y is false -> max = y
     * ─────────────────────────────────────────── */
    int x   = 5;
    int y   = 6;
    int max = (x > y) ? x : y;
    printf("Max: %d\n", max); // 6

    /* ───────────────────────────────────────────
     * EXAMPLE 2: bool condition inside printf
     * ternary used directly inside printf
     * ─────────────────────────────────────────── */
    bool isOnline = true;
    printf("%s", (isOnline) ? "Online\n" : "Offline\n");

    /* ───────────────────────────────────────────
     * EXAMPLE 3: even or odd check
     * number % 2 == 0 means no remainder = even
     * ─────────────────────────────────────────── */
    int number = 8;
    printf("%d is %s", number, (number % 2 == 0) ? "Even\n" : "Odd\n");

    /* ───────────────────────────────────────────
     * EXAMPLE 4: age check
     * ─────────────────────────────────────────── */
    int age = 21;
    printf("%s", (age >= 18) ? "Adult\n" : "Child\n");

    /* ───────────────────────────────────────────
     * EXAMPLE 5: AM or PM clock
     * %02d = print int with 2 digits, pad with 0
     * e.g. 9 -> "09", 11 -> "11"
     * ─────────────────────────────────────────── */
    int hours   = 11;
    int minutes = 30;
    printf("%02d:%02d %s", hours, minutes, (hours < 12) ? "AM\n" : "PM\n");
    // alternative way using a variable:
    // char *meridiem = (hours < 12) ? "AM" : "PM";
    // printf("%02d:%02d %s\n", hours, minutes, meridiem);

    return 0;
}
