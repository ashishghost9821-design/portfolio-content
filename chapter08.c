#include <stdio.h>
#include <string.h>

/*
 * ╔══════════════════════════════════════════════╗
 *     C PROGRAMMING - FUNCTIONS WITH ARGUMENTS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS A FUNCTION?
 * ═══════════════════════════════════════════════
 * A reusable section of code that can be called
 * (invoked) from anywhere in the program.
 * Arguments (values) can be passed into a function
 * so it can use them.
 *
 * Syntax:
 *   return_type functionName(type param1, type param2) {
 *       // code using param1, param2
 *   }
 *
 * void = function returns nothing, just executes code
 */

/* ═══════════════════════════════════════════════
 * FUNCTION DEFINITION
 * ═══════════════════════════════════════════════
 * Parameters can be named anything — only their
 * TYPE matters. These two are identical:
 *
 *   void happyBirthday(char name[], int age)
 *   void happyBirthday(char birthdayboi[], int yearsold)
 *
 * The name inside the function is just a local label.
 */

void happyBirthday(char name[], int age) {
    printf("\nHappy Birthday to you");
    printf("\nHappy Birthday to you");
    printf("\nHappy Birthday dear %s!", name);
    printf("\nHappy Birthday to you");
    printf("\nYou are %d years old!\n", age);
}

int main() {

    char name[50] = "";
    int  age      = 0;

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0'; // remove trailing newline

    printf("Enter your age: ");
    scanf("%d", &age);

    happyBirthday(name, age); // call function with arguments

    return 0;
}
