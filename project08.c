#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
 * ╔══════════════════════════════════════════════╗
 *         C PROGRAMMING - RANDOM NUMBERS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * RANDOM NUMBER FUNCTIONS
 * ═══════════════════════════════════════════════
 * #include <stdlib.h> -> for rand() and srand()
 * #include <time.h>   -> for time()
 *
 * srand(time(NULL)) -> seeds the random number
 *                      generator with current time
 *                      so you get different numbers
 *                      each run. Call ONCE at start.
 *
 * rand()    -> generates a random int from 0 to RAND_MAX
 * RAND_MAX  -> maximum value rand() can return (32767+)
 *
 * FORMULA to get random number in a range:
 *   (rand() % max) + min
 *   -> % max  gives 0 to max-1
 *   -> + min  shifts range up
 *
 * FORMULA for exact min to max inclusive:
 *   (rand() % (max - min + 1)) + min
 */

int main() {

    srand(time(NULL)); // seed once at start

    printf("%d\n", rand());     // random number 0 to RAND_MAX
    printf("%d\n", RAND_MAX);   // max possible value of rand()

    // --- range 1 to 6 (like a dice) ---
    int min = 1;
    int max = 6;
    int randomNUM = (rand() % max) + min;
    printf("Dice roll: %d\n", randomNUM);

    // --- range 50 to 100 ---
    int Min = 50;
    int Max = 100;

    // formula: (rand() % (Max - Min + 1)) + Min
    // Max - Min + 1 = 51 possible values (50,51,...,100)
    int randomNum1 = (rand() % (Max - Min + 1)) + Min;
    int randomNum2 = (rand() % (Max - Min + 1)) + Min;
    int randomNum3 = (rand() % (Max - Min + 1)) + Min;

    printf("%d\n%d\n%d\n", randomNum1, randomNum2, randomNum3);

    return 0;
}
