#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/*
 * ╔══════════════════════════════════════════════╗
 *       C PROGRAMMING - WHILE & DO/WHILE LOOPS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHILE LOOP
 * ═══════════════════════════════════════════════
 * Repeats code WHILE a condition is true.
 * Condition is checked BEFORE entering the loop.
 * If condition is false from the start, loop
 * never runs even once.
 *
 * Syntax:
 *   while(condition) {
 *       // code to repeat
 *   }
 */

/* ═══════════════════════════════════════════════
 * DO/WHILE LOOP
 * ═══════════════════════════════════════════════
 * Runs the code block FIRST, then checks condition.
 * Guarantees the loop body runs AT LEAST once.
 *
 * Syntax:
 *   do {
 *       // code to repeat
 *   } while(condition);
 *             ^
 *    semicolon required here!
 */

int main() {

    // --- DO/WHILE example ---
    // runs at least once, keeps asking until valid input
    int number = 0;

    do {
        printf("Enter a number greater than 0: ");
        scanf("%d", &number);
    } while(number <= 0); // repeats if number is 0 or negative

    (void)getchar(); // flush leftover '\n' from scanf before fgets

    // --- WHILE example ---
    // keeps asking for name until user enters something
    char name[50] = "";

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0'; // remove trailing newline

    while(strlen(name) == 0) { // if name is empty, ask again
        printf("Name cannot be empty! Please enter your name: ");
        fgets(name, sizeof(name), stdin);
        name[strlen(name) - 1] = '\0'; // remove trailing newline
    }

    printf("Hello %s\n", name);


    bool isRunning = true;
    char response = '\0';

    while(isRunning){
        printf("You are playing a game\n");
        printf("Would you like to continue ? (Y = yes, N = no): ");
        scanf("%c", &response);

        if(response != 'Y' && response != 'y'){
            isRunning = false;
        }
    }

    printf("You Exit The Game.\n");

    return 0;
}
