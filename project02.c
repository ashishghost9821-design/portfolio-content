#include <stdio.h>
#include <string.h>

/*
 * ╔══════════════════════════════════════════════╗
 *           C PROGRAMMING - MAD LIBS GAME
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 *
 * Concepts practiced:
 *   -> multiple fgets calls for string input
 *   -> strlen to strip trailing newline from each input
 *   -> storing multiple strings in separate char arrays
 *   -> combining strings in a printf story at the end
 */

int main() {

    char noun[50]       = "";
    char verb[50]       = "";
    char adjective1[50] = "";
    char adjective2[50] = "";
    char adjective3[50] = "";

    // collect all inputs first, then build the story
    printf("Enter an adjective (description): ");
    fgets(adjective1, sizeof(adjective1), stdin);
    adjective1[strlen(adjective1) - 1] = '\0';

    printf("Enter a noun (animal or person): ");
    fgets(noun, sizeof(noun), stdin);
    noun[strlen(noun) - 1] = '\0';

    printf("Enter an adjective (description): ");
    fgets(adjective2, sizeof(adjective2), stdin);
    adjective2[strlen(adjective2) - 1] = '\0';

    printf("Enter a verb (ending with -ing): ");
    fgets(verb, sizeof(verb), stdin);
    verb[strlen(verb) - 1] = '\0';

    printf("Enter an adjective (description): ");
    fgets(adjective3, sizeof(adjective3), stdin);
    adjective3[strlen(adjective3) - 1] = '\0';

    // build the mad libs story using all collected inputs
    printf("\nThe %s %s was %s %s in the %s forest.\n",
            adjective1, noun, adjective2, verb, adjective3);

    return 0;
}
