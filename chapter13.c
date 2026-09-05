#include <stdio.h>
#include <unistd.h> // Linux/Mac — for sleep()
                    // #include <windows.h> for Windows

/*
 * ╔══════════════════════════════════════════════╗
 *          C PROGRAMMING - FOR LOOPS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS A FOR LOOP?
 * ═══════════════════════════════════════════════
 * Repeats code a limited number of times.
 * Best used when you know exactly how many
 * times you want to repeat something.
 *
 * Syntax:
 *   for(initialize; condition; update) {
 *       // code to repeat
 *   }
 *
 * How it works step by step:
 *   1. initialize -> runs ONCE at the start  (int i = 0)
 *   2. condition  -> checked BEFORE each run (i <= 10)
 *   3. body       -> runs if condition true
 *   4. update     -> runs AFTER each body    (i++)
 *   5. repeat from step 2 until condition is false
 *
 * UPDATE OPERATORS:
 *   i++   -> i = i + 1  (increment by 1)
 *   i--   -> i = i - 1  (decrement by 1)
 *   i+=2  -> i = i + 2  (increment by 2, skips odd numbers)
 *   i+=3  -> i = i + 3  (increment by 3, every 3rd number)
 */

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: count 0 to 10 by 1
     * i starts at 0, runs while i <= 10, adds 1 each time
     * ─────────────────────────────────────────── */
    for(int i = 0; i <= 10; i++) {
        printf("%d\n", i); // prints 0 1 2 3 4 5 6 7 8 9 10
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 2: count 0 to 10 by 2 (even numbers only)
     * i+=2 means skip every odd number
     * ─────────────────────────────────────────── */
    for(int i = 0; i <= 10; i+=2) {
        printf("%d\n", i); // prints 0 2 4 6 8 10
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 3: count 0 to 100 by 3
     * i+=3 means jump 3 steps each iteration
     * ─────────────────────────────────────────── */
    for(int i = 0; i <= 100; i+=3) {
        printf("%d\n", i); // prints 0 3 6 9 12 ... 99
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 4: count DOWN from 10 to 0
     * i starts at 10, condition i >= 0, update i--
     * ─────────────────────────────────────────── */
    for(int i = 10; i >= 0; i--) {
        printf("%d\n", i); // prints 10 9 8 7 6 5 4 3 2 1 0
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 5: COUNTDOWN TIMER with sleep()
     * sleep(1) pauses program for 1 second each loop
     *
     * Linux/Mac : sleep(1)   -> 1 second
     * Windows   : Sleep(1000)-> 1000 milliseconds = 1 second
     *             capital S, needs <windows.h>
     * ─────────────────────────────────────────── */
    for(int i = 10; i >= 0; i--) {
        sleep(1);          // pause 1 second before printing
        printf("%d\n", i); // prints 10 9 8 ... 0 with 1 sec delay
    }

    printf("Happy New Year!\n"); // prints after countdown finishes

    return 0;
}
