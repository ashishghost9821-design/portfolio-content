#include <stdio.h>
#include <stdlib.h>

/*
 * ╔══════════════════════════════════════════════╗
 *        C PROGRAMMING - REALLOC
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS realloc()?
 * ═══════════════════════════════════════════════
 * Reallocation — resizes previously allocated memory.
 *
 * Syntax:
 *   float *temp = realloc(ptr, newSize);
 *
 *   ptr     -> pointer to existing malloc/calloc memory
 *   newSize -> new total size in BYTES
 *
 * What realloc() does:
 *   -> if newSize is BIGGER  : extends memory, keeps old data
 *   -> if newSize is SMALLER : shrinks memory, trims old data
 *   -> may move memory to a new location if needed
 *   -> returns NULL if reallocation fails
 *
 * WHY use a temp pointer?
 *   realloc can return NULL on failure.
 *   If you do: prices = realloc(prices, ...)
 *   and it fails -> prices becomes NULL
 *   -> original data is LOST forever (memory leak!)
 *
 *   Safe pattern:
 *     float *temp = realloc(prices, newSize);
 *     if(temp == NULL) { handle error, prices still safe }
 *     else             { prices = temp; temp = NULL; }
 *
 * malloc -> calloc -> realloc summary:
 *   malloc(size)         -> allocate, garbage values
 *   calloc(count, size)  -> allocate, zeroed values
 *   realloc(ptr, size)   -> resize existing allocation
 */

int main() {

    int number = 0;
    printf("Enter the number of prices: ");
    scanf("%d", &number);

    // initial allocation with malloc
    float *prices = malloc(number * sizeof(float));

    if(prices == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // fill initial prices
    for(int i = 0; i < number; i++) {
        printf("Enter price #%d: ", i + 1);
        scanf("%f", &prices[i]);
    }

    // ask for new size
    int newNumber = 0;
    printf("Enter a new number of prices: ");
    scanf("%d", &newNumber);

    // use temp pointer — NEVER do prices = realloc(prices, ...)
    // if realloc fails and returns NULL, original data is lost
    float *temp = realloc(prices, newNumber * sizeof(float));

    if(temp == NULL) {
        printf("Could not reallocate memory!\n");
        // prices still valid here — original data safe
    }
    else {
        prices = temp; // realloc succeeded, update prices
        temp   = NULL; // avoid dangling temp pointer

        // fill only the NEW slots (old ones already have data)
        for(int i = number; i < newNumber; i++) {
            printf("Enter price #%d: ", i + 1);
            scanf("%f", &prices[i]);
        }

        // print all prices
        printf("\nAll prices:\n");
        for(int i = 0; i < newNumber; i++) {
            printf("$%.2f\n", prices[i]); // fix: $%f.2 -> $%.2f
        }
    }

    free(prices);   // return memory to OS
    prices = NULL;  // avoid dangling pointer

    return 0;
}
