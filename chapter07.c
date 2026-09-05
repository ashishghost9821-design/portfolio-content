#include <stdio.h>
#include <stdbool.h>

/*
 * ╔══════════════════════════════════════════════╗
 *        C PROGRAMMING - LOGICAL OPERATORS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT ARE LOGICAL OPERATORS?
 * ═══════════════════════════════════════════════
 * Used to combine or modify boolean expressions.
 *
 *  OPERATOR | MEANING | TRUE WHEN
 * ----------+---------+---------------------------
 *  &&       | AND     | BOTH conditions are true
 *  ||       | OR      | AT LEAST one is true
 *  !        | NOT     | condition is flipped
 *
 * Examples:
 *   true  && true  = true
 *   true  && false = false
 *   false || true  = true
 *   false || false = false
 *   !true          = false
 *   !false         = true
 */

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: && (AND)
     * BOTH conditions must be true to enter if block
     * temp must be > 0 AND < 30 to be GOOD
     * ─────────────────────────────────────────── */
    int temp = 0;

    printf("What is the current temperature: ");
    scanf("%d", &temp);

    if(temp > 0 && temp < 30) {
        printf("The temperature is GOOD\n");
    }
    else {
        printf("The temperature is BAD\n");
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 2: || (OR) — commented out version
     * true if temp <= 0 OR temp >= 30 (either bad extreme)
     *
     *   if(temp <= 0 || temp >= 30) {
     *       printf("The temperature is BAD\n");
     *   }
     *   else {
     *       printf("The temperature is GOOD\n");
     *   }
     * ─────────────────────────────────────────── */

    /* ───────────────────────────────────────────
     * EXAMPLE 3: bool with if/else
     * ─────────────────────────────────────────── */
    bool isSunny = true;

    if(isSunny) {
        printf("It is sunny outside\n");
    }
    else {
        printf("It is cloudy outside\n");
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 4: ! (NOT) — commented out version
     * flips the bool value
     *
     *   if(!isSunny) {           // if NOT sunny
     *       printf("It is cloudy outside\n");
     *   }
     *   else {
     *       printf("It is sunny outside\n");
     *   }
     * ─────────────────────────────────────────── */

    return 0;
}
