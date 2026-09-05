#include <stdio.h>

int main() {

    /*
     * ╔══════════════════════════════════════════╗
     *      C PROGRAMMING - IF / ELSE IF / ELSE
     *       Bro Code Tutorial | My Notes
     * ╚══════════════════════════════════════════╝
     */

    /* ─────────────────────────────────────────
     * SECTION 1: CONDITIONAL LOGIC
     * ─────────────────────────────────────────
     * if/else if/else lets the program choose
     * different paths depending on a condition.
     * Conditions are checked top to bottom —
     * the first true condition runs, the rest
     * are skipped.
     */

    int age = 0;

    printf("What is your age: ");
    scanf("%d", &age);

    if(age >= 65){
        printf("You are a senior\n");
    }

    else if(age >= 18){
        printf("You are an adult\n");
    }

    else if(age < 0){
        printf("You haven't been born yet\n");
    }

    else if(age == 0){
        printf("You are a new born.\n");
    }

    else{
        printf("You are a child\n");
    }

    return 0;
}
