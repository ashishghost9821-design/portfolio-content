#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *             C PROGRAMMING - ENUM
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS AN ENUM?
 * ═══════════════════════════════════════════════
 * A user-defined data type that consists of a set
 * of named integer constants.
 *
 * Benefit: replaces plain numbers with readable names
 * so code is easier to understand.
 *
 * Syntax:
 *   enum Name { VALUE1, VALUE2, VALUE3 };
 *
 * By default values start at 0 and increment by 1:
 *   VALUE1 = 0, VALUE2 = 1, VALUE3 = 2 ...
 *
 * You can assign custom values manually:
 *   enum Day { SUNDAY = 1, MONDAY = 2, ... }
 *
 * TWO WAYS to define enum:
 *
 * WAY 1: regular enum (must write "enum Day" each time)
 *   enum Day { SUNDAY, MONDAY };
 *   enum Day today = SUNDAY;
 *
 * WAY 2: typedef enum (cleaner, no need to repeat "enum")
 *   typedef enum { SUNDAY, MONDAY } Day;
 *   Day today = SUNDAY;
 */

/* ═══════════════════════════════════════════════
 * EXAMPLE 1: enum with custom start value
 * ═══════════════════════════════════════════════
 * Adding "Day" after closing } makes "Day" a variable
 * name, NOT a type — use typedef instead for types.
 */
typedef enum {
    SUNDAY    = 1,
    MONDAY    = 2,
    TUESDAY   = 3,
    WEDNESDAY = 4,
    THURSDAY  = 5,
    FRIDAY    = 6,
    SATURDAY  = 7
} Day;

/* ═══════════════════════════════════════════════
 * EXAMPLE 2: typedef enum for status codes
 * ═══════════════════════════════════════════════
 * Default values: SUCCESS = 0, FAILURE = 1, PENDING = 2
 * Much more readable than using raw numbers 0, 1, 2
 */
typedef enum {
    SUCCESS,  // = 0
    FAILURE,  // = 1
    PENDING   // = 2
} Status;

/* ═══════════════════════════════════════════════
 * FUNCTION PROTOTYPE
 * ═══════════════════════════════════════════════
 * Parameter must have a NAME (status), not just type.
 * WRONG: void connectStatus(Status);
 * RIGHT: void connectStatus(Status status);
 */
void connectStatus(Status status);

/* ═══════════════════════════════════════════════
 * MAIN — only ONE main() in a C program
 * ═══════════════════════════════════════════════ */
int main() {

    // --- EXAMPLE 1: Day enum ---
    Day today = SUNDAY;

    if(today == SUNDAY || today == SATURDAY) {
        printf("It's the weekend!\n");
    }
    else {
        printf("It's a weekday.\n");
    }

    // --- EXAMPLE 2: Status enum ---
    Status status = SUCCESS;
    connectStatus(status);

    status = PENDING;
    connectStatus(status);

    status = FAILURE;
    connectStatus(status);

    return 0;
}

/* ═══════════════════════════════════════════════
 * FUNCTION DEFINITION
 * ═══════════════════════════════════════════════
 * switch(status) — must pass the variable in
 * WRONG: switch() -> compiler error, nothing to check
 * RIGHT: switch(status) -> checks the enum value
 */
void connectStatus(Status status) {
    switch(status) {
        case SUCCESS:
            printf("Connection was successful\n");
            break;
        case FAILURE:
            printf("Could not connect\n");
            break;
        case PENDING:
            printf("Connecting....\n");
            break;
    }
}
