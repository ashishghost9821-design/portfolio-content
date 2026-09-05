#include <stdio.h>
#include <stdlib.h>

/*
 * ╔══════════════════════════════════════════════╗
 *        C PROGRAMMING - CALLOC
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS calloc()?
 * ═══════════════════════════════════════════════
 * Contiguous allocation — like malloc() but with
 * one important difference:
 *
 *   malloc(size)        -> allocates memory, values are GARBAGE
 *   calloc(count, size) -> allocates memory, sets ALL bytes to 0
 *
 * Syntax:
 *   type *ptr = calloc(numberOfElements, sizeof(type));
 *
 * Example:
 *   int *scores = calloc(5, sizeof(int));
 *   -> allocates 5 ints = 20 bytes, all set to 0
 *
 * malloc vs calloc:
 *   malloc  -> faster (skips zeroing memory)
 *   calloc  -> safer  (no garbage values, less bugs)
 *
 * ALWAYS:
 *   1. check for NULL after calloc
 *   2. free() when done
 *   3. set pointer to NULL after free()
 */

int main() {

    int number = 0;
    printf("Enter the number of players: ");
    scanf("%d", &number);

    // calloc(count, size) — allocates and zeroes memory
    int *scores = calloc(number, sizeof(int)); // fix: score -> scores

    // check if allocation succeeded
    if(scores == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // fill scores array with user input
    for(int i = 0; i < number; i++) {
        printf("Enter score #%d: ", i + 1);
        scanf("%d", &scores[i]);
    }

    // print all scores
    printf("\nScores: ");
    for(int i = 0; i < number; i++) {
        printf("%d ", scores[i]);
    }
    printf("\n");

    free(scores);   // return memory to OS
    scores = NULL;  // avoid dangling pointer

    return 0;
}
