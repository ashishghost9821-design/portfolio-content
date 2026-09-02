#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *          C PROGRAMMING - FILE READING
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * READING A FILE IN C
 * ═══════════════════════════════════════════════
 * FILE *pFile = fopen("filename", "mode");
 *
 * fopen() modes:
 *   "r"  -> read only (file must exist)
 *   "w"  -> write (creates file, overwrites if exists)
 *   "a"  -> append (adds to end of file)
 *
 * FILE *pFile
 *   -> pointer to a FILE structure
 *   -> fopen returns NULL if file not found
 *   -> ALWAYS check for NULL before using!
 *
 * fgets(buffer, size, pFile)
 *   -> reads one line at a time into buffer
 *   -> returns NULL when file ends
 *   -> loop with while != NULL to read all lines
 *
 * fclose(pFile)
 *   -> closes the file when done
 *   -> ALWAYS close files you open (good practice)
 *
 * PATH NOTE (Linux/Termux):
 *   Use forward slashes /  NOT backslashes \
 *   Backslashes \ are for Windows only!
 *   Simplest: just use filename if file is in same folder
 */

int main() {

    // open file for reading — use forward slash on Linux
    FILE *pFile = fopen("/data/data/com.termux/files/home/c-programming/input.txt", "r");
    char buffer[1024] = {0}; // stores one line at a time

    // ALWAYS check if file opened successfully
    if(pFile == NULL) {
        printf("Could not open file\n");
        return 1; // exit program with error code
    }

    // read line by line until end of file (fgets returns NULL)
    while(fgets(buffer, sizeof(buffer), pFile) != NULL) {
        printf("%s", buffer); // buffer already has '\n' from file
    }

    fclose(pFile); // close file when done

    return 0;
}
