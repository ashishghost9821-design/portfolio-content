#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *          C PROGRAMMING - FILE WRITING
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WRITING A FILE IN C
 * ═══════════════════════════════════════════════
 * FILE *pFile = fopen("path", "mode");
 *
 * fopen() modes:
 *   "r"  -> read only  (file must already exist)
 *   "w"  -> write      (creates file if not exists,
 *                        OVERWRITES if it does exist)
 *   "a"  -> append     (adds to end, keeps old content)
 *
 * fprintf(pFile, "format", value)
 *   -> same as printf BUT writes to a FILE
 *   -> instead of printing to screen, saves to file
 *
 * fclose(pFile)
 *   -> saves and closes the file
 *   -> ALWAYS close after writing or data may be lost
 *
 * ALWAYS check pFile != NULL before writing
 * fopen returns NULL if path is wrong or
 * permissions don't allow creating the file
 */

int main() {

    // open file for writing — creates Output.txt if not exists
    // OVERWRITES content if file already exists
    FILE *pFile = fopen("/data/data/com.termux/files/home/Output.txt", "w");

    char text[] = "BOOTY BOOTY BOOTY\nROCKIN' EVERYWHERE!";

    // check if file opened successfully before writing
    if(pFile == NULL) {
        printf("Error opening file\n");
        return 1; // exit with error code
    }

    // fprintf writes to file instead of screen
    // same format as printf: fprintf(file, "format", value)
    fprintf(pFile, "%s", text);

    printf("File was written successfully\n");

    fclose(pFile); // save and close — never skip this!

    return 0;
}
