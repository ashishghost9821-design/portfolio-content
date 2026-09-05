#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
 * ╔══════════════════════════════════════════════╗
 *        C PROGRAMMING - NUMBER GUESSING GAME
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHY fgets + sscanf INSTEAD OF JUST scanf?
 * ═══════════════════════════════════════════════
 * scanf("%d") skips whitespace including '\n'
 * so pressing Enter with nothing typed makes
 * it wait forever — program gets stuck.
 *
 * Fix: fgets reads the WHOLE line including '\n'
 *      sscanf then tries to parse an integer from it
 *      if line is empty or invalid, sscanf returns 0
 *      and we handle the error cleanly.
 *
 * sscanf(buffer, "%d", &guess)
 *   -> same as scanf but reads from a string
 *      instead of keyboard directly
 */

int main() {

    srand(time(NULL)); // seed random number generator

    int  guess  = 0;
    int  tries  = 0;
    int  min    = 1;
    int  max    = 100;
    int  answer = (rand() % (max - min + 1)) + min;
    char buffer[50]; // stores raw input line from fgets

    printf("*** NUMBER GUESSING GAME ***\n");

    do {
        printf("Guess a number between %d - %d: ", min, max);

        // fgets reads full line — never gets stuck on empty Enter
        if(fgets(buffer, sizeof(buffer), stdin) == NULL) {
            continue; // skip if input fails
        }

        // sscanf parses integer from the line fgets read
        // returns 1 if successful, 0 if invalid/empty
        if(sscanf(buffer, "%d", &guess) != 1) {
            printf("Invalid input! Please enter a number.\n");
            continue; // go back to top of loop
        }

        // range check: keep guess within min-max
        if(guess < min || guess > max) {
            printf("Please stay in range (%d - %d)\n", min, max);
            continue;
        }

        tries++;

        if(guess < answer) {
            printf("Too low!\n");
        }
        else if(guess > answer) {
            printf("Too high!\n");
        }
        else {
            printf("!! CORRECT !!\n");
        }

    } while(guess != answer);

    printf("The answer was: %d\n", answer);
    printf("It took you %d tries\n", tries);

    return 0;
}
