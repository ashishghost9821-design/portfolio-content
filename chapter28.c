#include <stdio.h>
#include <stdlib.h> // malloc() and free() live here

/*
 * ╔══════════════════════════════════════════════╗
 *       C PROGRAMMING - DYNAMIC MEMORY (malloc)
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * STATIC vs DYNAMIC MEMORY
 * ═══════════════════════════════════════════════
 * STATIC (normal arrays):
 *   char grades[5];
 *   -> size must be known at compile time
 *   -> fixed size, cannot change while running
 *
 * DYNAMIC (malloc):
 *   char *grades = malloc(number * sizeof(char));
 *   -> size decided at RUNTIME (while program runs)
 *   -> you choose how much memory to rent from OS
 *   -> must manually free() when done
 *
 * Think of it like renting a hotel room:
 *   malloc() = check in  (rent memory)
 *   free()   = check out (return memory to OS)
 *   If you forget free() = memory leak (room never freed)
 */

/* ═══════════════════════════════════════════════
 * malloc() SYNTAX
 * ═══════════════════════════════════════════════
 * void *malloc(size_t size);
 *
 *   size_t = number of BYTES to allocate
 *
 * Example:
 *   char *grades = malloc(number * sizeof(char));
 *    ^               ^      ^          ^
 *    |               |      |          sizeof(char) = 1 byte
 *    |               |      number of elements
 *    char pointer    malloc = allocate bytes
 *
 * malloc returns NULL if allocation fails
 * ALWAYS check for NULL before using the pointer!
 *
 * sizeof(type) gives bytes needed per element:
 *   sizeof(char)  = 1 byte
 *   sizeof(int)   = 4 bytes
 *   sizeof(float) = 4 bytes
 */

/* ═══════════════════════════════════════════════
 * DANGLING POINTER
 * ═══════════════════════════════════════════════
 * After free(grades), the pointer still holds
 * the old address — but that memory is freed.
 * Using it would be undefined behavior.
 *
 * Fix: set pointer to NULL after free()
 *   grades = NULL;
 * Now any accidental use will crash clearly
 * instead of silently corrupting memory.
 */

int main() {

    int number = 0;
    printf("Enter the number of grades: ");
    scanf("%d", &number);

    // allocate memory for 'number' chars at runtime
    char *grades = malloc(number * sizeof(char));

    // ALWAYS check malloc result before using
    if(grades == NULL) {          // typo fix: gardes -> grades
        printf("Memory allocation failed\n");
        return 1;
    }

    // fill the dynamically allocated array
    for(int i = 0; i < number; i++) {
        printf("Enter grade #%d: ", i + 1);
        scanf(" %c", &grades[i]); // space before %c clears '\n'
    }

    // print all grades
    printf("\nGrades entered: ");
    for(int i = 0; i < number; i++) {
        printf("%c ", grades[i]);
    }
    printf("\n");

    free(grades);   // return rented memory back to OS
    grades = NULL;  // avoid dangling pointer

    return 0;
}
