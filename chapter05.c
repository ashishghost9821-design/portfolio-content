#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *         C PROGRAMMING - SWITCH STATEMENT
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS A SWITCH STATEMENT?
 * ═══════════════════════════════════════════════
 * An alternative to using many if/else statements.
 * More efficient when checking a single variable
 * against fixed integer or char values.
 *
 * Syntax:
 *   switch(variable) {
 *       case value1:
 *           // code
 *           break;   <- stops fall-through to next case
 *       case value2:
 *           // code
 *           break;
 *       default:     <- runs if no case matches
 *           // code
 *   }
 *
 * IMPORTANT: always add break after each case
 * or it will fall-through and run the next case too.
 */

int main() {

    int dayOfWeek = 0;

    printf("Enter a day of the week (1-7): ");
    scanf("%d", &dayOfWeek);

    switch(dayOfWeek) {
        case 1:  printf("It is Monday\n");    break;
        case 2:  printf("It is Tuesday\n");   break;
        case 3:  printf("It is Wednesday\n"); break;
        case 4:  printf("It is Thursday\n");  break;
        case 5:  printf("It is Friday\n");    break;
        case 6:  printf("It is Saturday\n");  break;
        case 7:  printf("It is Sunday\n");    break;
        default: printf("Please enter a valid number (1-7)\n"); break;
    }

    return 0;
}
