#include <stdio.h>
#include <stdbool.h>

/*
 * ╔══════════════════════════════════════════════╗
 *      C PROGRAMMING - FUNCTION PROTOTYPES
 *          Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS A FUNCTION PROTOTYPE?
 * ═══════════════════════════════════════════════
 * A declaration that tells the compiler about a
 * function BEFORE it is actually defined.
 *
 * Provides:
 *   -> function name
 *   -> return type
 *   -> parameters (type and order)
 *
 * Benefits:
 *   -> allows functions to be defined BELOW main()
 *   -> enables type checking by compiler
 *   -> improves code readability and organization
 *   -> helps prevent errors
 *
 * Syntax:
 *   return_type functionName(type param1, type param2);
 *                                                    ^
 *                                           semicolon here!
 */

/* ═══════════════════════════════════════════════
 * FUNCTION PROTOTYPES
 * ═══════════════════════════════════════════════
 * Declared here, defined below main().
 */

void hello(char name[], int age); // takes string + int, returns nothing
bool ageCheck(int age);           // takes int, returns bool

/* ═══════════════════════════════════════════════
 * MAIN
 * ═══════════════════════════════════════════════
 * Functions can now be called here even though
 * they are defined below — because prototypes
 * already told the compiler they exist.
 */

int main() {

    // calling hello() with name and age
    hello("Spongebob", 30);

    // calling ageCheck() inside if condition directly
    if(ageCheck(30)) {
        printf("You are old enough to work at the Krusty Krab\n");
    }
    else {
        printf("You must be 16+ to work at the Krusty Krab\n");
    }

    return 0;
}

/* ═══════════════════════════════════════════════
 * FUNCTION DEFINITIONS
 * ═══════════════════════════════════════════════
 * Defined below main() — only possible because
 * prototypes were declared above.
 */

// void = returns nothing, just prints
void hello(char name[], int age) {
    printf("Hello %s\n", name);
    printf("You are %d years old\n", age);
}

// shorthand return — no need for full if/else
// return age >= 16 directly returns true or false
bool ageCheck(int age) {
    return age >= 16;
    // same as writing:
    // if(age >= 16) { return true; }
    // else          { return false; }
}
