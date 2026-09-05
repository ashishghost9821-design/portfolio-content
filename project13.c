#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <stdbool.h>

/*
 * ╔══════════════════════════════════════════════╗
 *          C PROGRAMMING - DIGITAL CLOCK
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 *
 * Concepts practiced:
 *   -> time_t and struct tm from <time.h>
 *   -> time() and localtime() functions
 *   -> \r carriage return trick for in-place update
 *   -> sleep() from <unistd.h>
 *   -> infinite while loop with bool flag
 */

/* ═══════════════════════════════════════════════
 * HOW TIME WORKS IN C
 * ═══════════════════════════════════════════════
 * time_t rawtime
 *   -> stores time as seconds since Jan 1 1970
 *   -> called "Unix Epoch" or "Unix Timestamp"
 *
 * time(&rawtime)
 *   -> fills rawtime with current time in seconds
 *
 * struct tm *pTime = localtime(&rawtime)
 *   -> converts raw seconds into readable struct
 *   -> struct tm has members:
 *        pTime->tm_hour  (0-23)
 *        pTime->tm_min   (0-59)
 *        pTime->tm_sec   (0-59)
 *
 * \r = carriage return
 *   -> moves cursor back to START of current line
 *   -> next printf overwrites same line
 *   -> creates the "ticking clock" effect
 *   -> without \r, each second prints on a new line
 *
 * fflush(stdout)
 *   -> forces output to print immediately
 *   -> without this, \r may not show on some systems
 */

int main() {

    time_t    rawtime  = 0;    // seconds since Jan 1 1970 (Unix Epoch)
    struct tm *pTime   = NULL; // pointer to broken-down time struct
    bool      isRunning = true;

    printf("DIGITAL CLOCK\n");

    while(isRunning) {

        time(&rawtime);               // get current time in seconds
        pTime = localtime(&rawtime);  // convert to hours/min/sec

        // \r overwrites same line instead of new line each second
        // %02d = always 2 digits, pad with 0 (e.g. 9 -> 09)
        printf("\r%02d:%02d:%02d",
               pTime->tm_hour,
               pTime->tm_min,
               pTime->tm_sec);

        fflush(stdout); // force print immediately

        sleep(1); // wait 1 second before next update
    }

    return 0;
}
