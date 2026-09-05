#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
 * ╔══════════════════════════════════════════════╗
 *       C PROGRAMMING - ROCK PAPER SCISSORS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * FUNCTION PROTOTYPES
 * ═══════════════════════════════════════════════
 * Declared above main() so compiler knows
 * they exist before they are called.
 */

int  getComputerChoice();                        // returns 1, 2, or 3 randomly
int  getUserChoice();                            // returns user's menu choice
void checkWinner(int userChoice, int computerChoice); // prints result, returns nothing

/* ═══════════════════════════════════════════════
 * MAIN
 * ═══════════════════════════════════════════════ */

int main() {

    srand(time(NULL)); // seed random number generator once

    printf("*** ROCK PAPER SCISSORS ***\n");

    int userChoice     = getUserChoice();
    int computerChoice = getComputerChoice();

    // print what user chose
    switch(userChoice) {
        case 1: printf("You chose Rock!\n");     break;
        case 2: printf("You chose Paper!\n");    break;
        case 3: printf("You chose Scissors!\n"); break;
    }

    // print what computer chose
    switch(computerChoice) {
        case 1: printf("Computer chose Rock!\n");     break;
        case 2: printf("Computer chose Paper!\n");    break;
        case 3: printf("Computer chose Scissors!\n"); break;
    }

    checkWinner(userChoice, computerChoice);

    return 0;
}

/* ═══════════════════════════════════════════════
 * FUNCTION DEFINITIONS
 * ═══════════════════════════════════════════════ */

// returns random int 1-3 (1=Rock, 2=Paper, 3=Scissors)
int getComputerChoice() {
    return (rand() % 3) + 1;
}

// shows menu, reads and returns user's choice
int getUserChoice() {
    int choice = 0;

    printf("1. Rock\n");
    printf("2. Paper\n");
    printf("3. Scissors\n");
    printf("Choose: ");
    scanf("%d", &choice);

    return choice;
}

/* ═══════════════════════════════════════════════
 * checkWinner() — TWO WAYS TO WRITE WIN CONDITION
 * ═══════════════════════════════════════════════
 *
 * WAY 1 (used below): separate if/else for each win
 *   -> easier to read, more explicit
 *
 * WAY 2 (commented out): combine all wins with || (OR)
 *   -> shorter, but harder to read at a glance
 *   -> || means "or" — true if ANY condition is true
 *
 *   else if((userChoice == 1 && computerChoice == 3) ||
 *           (userChoice == 2 && computerChoice == 1) ||
 *           (userChoice == 3 && computerChoice == 2)) {
 *       printf("You WIN!\n");
 *   }
 */

void checkWinner(int userChoice, int computerChoice) {

    if(userChoice == computerChoice) {
        printf("It's a TIE!\n");
    }
    else if(userChoice == 1 && computerChoice == 3) {
        printf("You WIN! Rock beats Scissors\n");
    }
    else if(userChoice == 2 && computerChoice == 1) {
        printf("You WIN! Paper beats Rock\n");
    }
    else if(userChoice == 3 && computerChoice == 2) {
        printf("You WIN! Scissors beats Paper\n");
    }
    else {
        printf("You LOSE!\n");
    }
}
