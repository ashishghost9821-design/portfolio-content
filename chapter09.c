#include <stdio.h>
#include <stdbool.h>

/*
 * ╔══════════════════════════════════════════════╗
 *         C PROGRAMMING - FUNCTIONS
 *          Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS A FUNCTION?
 * ═══════════════════════════════════════════════
 * A reusable block of code that runs when called.
 * Helps avoid repeating the same code.
 *
 * Syntax:
 *   return_type functionName(parameters) {
 *       return value;
 *   }
 *
 * Must be defined ABOVE main() so compiler
 * knows it exists before it is called.
 */

/* ═══════════════════════════════════════════════
 * EXAMPLE 1: MATH FUNCTIONS (return double)
 * ═══════════════════════════════════════════════
 * return type = double
 * parameter   = double num (the input value)
 */

double cube(double num) {
    return num * num * num; // num^3
}

double square(double num) {
    return num * num; // num^2
    // same as:
    // double result = num * num;
    // return result;
}

// NOTE: replace double with int to work with integers

/* ═══════════════════════════════════════════════
 * EXAMPLE 2: BOOL FUNCTION (return bool)
 * ═══════════════════════════════════════════════
 * return type = bool  (needs <stdbool.h>)
 * returns true or false based on a condition
 */

bool ageCheck(int age) {
    if(age >= 18) {
        return true;  // eligible
    }
    else {
        return false; // not eligible
    }
}

/* ═══════════════════════════════════════════════
 * EXAMPLE 3: COMPARISON FUNCTION (return int)
 * ═══════════════════════════════════════════════
 * Takes two int parameters and returns the larger.
 * Shows functions can take multiple parameters.
 */

int getMax(int x, int y) {
    if(x >= y) {
        return x; // x is larger or equal
    }
    else {
        return y; // y is larger
    }
}

/* ═══════════════════════════════════════════════
 * MAIN — only ONE main() allowed in a C program
 * ═══════════════════════════════════════════════
 */

int main() {

    // --- calling cube() and square() ---
    double x = cube(2.3);
    double y = cube(3.3);
    double z = cube(4.5);
    double s = square(5.0);

    printf("cube(2.3)   = %.3lf\n", x);
    printf("cube(3.3)   = %.3lf\n", y);
    printf("cube(4.5)   = %.3lf\n", z);
    printf("square(5.0) = %.3lf\n", s);

    // --- calling ageCheck() ---
    int age = 0;

    printf("\nWhat is your age: ");
    scanf("%d", &age);

    if(ageCheck(age)) {
        printf("You may sign up\n");
    }
    else {
        printf("You must be 18+ to sign up!\n");
    }

    // --- calling getMax() ---
    int max = getMax(2, 3);
    printf("\nMax of 2 and 3: %d\n", max);

    return 0;
}
