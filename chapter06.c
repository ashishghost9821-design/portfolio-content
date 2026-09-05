#include <stdio.h>
#include <stdbool.h>

int main() {

    /*
     * ╔══════════════════════════════════════════════╗
     *        C PROGRAMMING - NESTED IF/ELSE
     *         Bro Code Tutorial | My Notes
     * ╚══════════════════════════════════════════════╝
     */

    /* ═══════════════════════════════════════════════
     * WHAT IS A NESTED IF/ELSE?
     * ═══════════════════════════════════════════════
     * An if/else statement inside another if/else.
     * Used when a condition depends on another condition.
     *
     * Syntax:
     *   if(condition1) {
     *       if(condition2) {
     *           // both true
     *       }
     *       else {
     *           // only condition1 true
     *       }
     *   }
     *   else {
     *       // condition1 false
     *   }
     */

    /* ═══════════════════════════════════════════════
     * COMPOUND ASSIGNMENT OPERATOR
     * ═══════════════════════════════════════════════
     * Shorthand for updating a variable's own value.
     *
     *   price *= 0.9  means  price = price * 0.9
     *   price *= 0.8  means  price = price * 0.8
     *   price *= 0.7  means  price = price * 0.7
     */

    /* ═══════════════════════════════════════════════
     * EXAMPLE: TICKET DISCOUNT CALCULATOR
     * ═══════════════════════════════════════════════
     * Base price = $10.00
     *
     * Discount rules:
     *   student only          -> 10% off -> $9.00  (* 0.9)
     *   senior only           -> 20% off -> $8.00  (* 0.8)
     *   student + senior both -> 30% off -> $7.00  (* 0.7)
     *   neither               -> no discount
     */

    float price     = 10.00f; // base ticket price
    bool isStudent  = true;   // toggle to test different cases
    bool isSenior   = true;   // toggle to test different cases

    if(isStudent) {
        if(isSenior) {
            // both student AND senior -> 30% off total
            printf("You get a student discount of 10%%.\n");
            printf("You get a senior discount of 20%%.\n");
            price *= 0.7; // price = price * 0.7
        }
        else {
            // student only -> 10% off
            printf("You get a student discount of 10%%.\n");
            price *= 0.9; // price = price * 0.9
        }
    }
    else {
        if(isSenior) {
            // senior only -> 20% off
            printf("You get a senior discount of 20%%.\n");
            price *= 0.8; // price = price * 0.8
        }
        // else: no discount, price stays the same
    }

    printf("The price of a ticket is: $%.2f\n", price);

    return 0;
}
