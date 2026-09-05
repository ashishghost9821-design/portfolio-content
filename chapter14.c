#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *        C PROGRAMMING - BREAK & CONTINUE
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * BREAK vs CONTINUE
 * ═══════════════════════════════════════════════
 *
 *  break    -> STOP the loop completely
 *              exits the loop immediately
 *
 *  continue -> SKIP current iteration only
 *              jumps to next cycle of the loop
 */

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: continue — skip number 4
     * prints 1 2 3 5 6 7 8 9 10 (4 is skipped)
     * ─────────────────────────────────────────── */
    for(int i = 1; i <= 10; i++) {
        if(i == 4) {
            continue; // skip this iteration, go to i=5
        }
        printf("%d\n", i);
    }

    /* ───────────────────────────────────────────
     * EXAMPLE 2: break — stop at number 4
     * prints 1 2 3 (stops when i hits 4)
     * ─────────────────────────────────────────── */
    for(int i = 1; i <= 10; i++) {
        if(i == 4) {
            break; // exit the loop entirely
        }
        printf("%d\n", i);
    }

    return 0;
}
