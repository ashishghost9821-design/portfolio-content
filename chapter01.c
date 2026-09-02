#include <stdio.h>
#include <stdbool.h>

int main() {

    /*
     * ╔══════════════════════════════════════════╗
     *          C PROGRAMMING - VARIABLES
     *       Bro Code Tutorial | My Notes
     * ╚══════════════════════════════════════════╝
     */

    /* ─────────────────────────────────────────
     * SECTION 1: WHAT IS A VARIABLE?
     * ─────────────────────────────────────────
     * A variable is a reusable container for a value.
     * Syntax: data_type variable_name = value;
     */

    int age      = 25;    // stores whole numbers
    int year     = 2026;
    int quantity = 10;

    printf("You are %d years old\n", age);
    printf("This is %d\n",           year);
    printf("You have ordered %d bananas\n", quantity);

    /* ─────────────────────────────────────────
     * SECTION 2: DATA TYPES
     * ─────────────────────────────────────────
     *
     *  TYPE      | SIZE     | DESCRIPTION
     * -----------+----------+-------------------------
     *  int       | 4 bytes  | Whole number
     *  float     | 4 bytes  | Single-precision decimal
     *  double    | 8 bytes  | Double-precision decimal
     *  char      | 1 byte   | Single character
     *  char[]    | varies   | Array of characters (string)
     *  bool      | 1 byte   | true or false (needs <stdbool.h>)
     */

    float  gpa      = 2.5;       // single-precision decimal
    float  price    = 19.99;
    double pi       = 3.141592;  // higher precision than float
    char   grade    = 'A';       // single quotes for char
    char   name[]   = "Bro Code";// double quotes for string
    bool   isOnline = true;      // true = 1, false = 0

    printf("Your GPA is %.1f\n",           gpa);      // 1 decimal place
    printf("The price is $%.2f\n",         price);    // 2 decimal places
    printf("The value of pi is %.15lf\n",  pi);       // 15 decimal places
    printf("Your grade is %c\n",           grade);
    printf("Hello, %s!\n",                 name);
    printf("Is online: %d\n",             isOnline);  // prints 1 (true) or 0 (false)

    /* ─────────────────────────────────────────
     * SECTION 3: FORMAT SPECIFIERS
     * ─────────────────────────────────────────
     * Special tokens starting with % that control
     * how data is displayed.
     *
     *  SPECIFIER | USED FOR
     * -----------+---------------------------
     *  %d        | int
     *  %f        | float
     *  %lf       | double
     *  %c        | char
     *  %s        | string (char[])
     *  %.Nf      | float/double with N decimal places
     */

    int    id       = 25;
    float  cost     = 19.99;
    double precise  = 3.1415926535;
    char   symbol   = '$';
    char   label[]  = "Bro Code";

    printf("%d\n",  id);       // integer
    printf("%f\n",  cost);     // float (default 6 decimal places)
    printf("%lf\n", precise);  // double
    printf("%c\n",  symbol);   // character
    printf("%s\n",  label);    // string

    /* ─────────────────────────────────────────
     * SECTION 4: WIDTH & FLAG MODIFIERS
     * ─────────────────────────────────────────
     * Go between % and the specifier to control alignment.
     *
     *  MODIFIER  | EFFECT
     * -----------+-------------------------------------
     *  %+d       | Always show sign (+ or -)
     *  %-3d      | Left-align in a field of width 3
     *  %3d       | Right-align in a field of width 3
     *  %03d      | Right-align, zero-pad instead of spaces
     */

    int num1 =     1;
    int num2 =    10;
    int num3 =   100;
    int num4 = -1000;

    printf("%+d\n",  num1);  // output: +1
    printf("%-3d|\n", num2); // output: 10|   (left-aligned, | shows spacing)
    printf("%3d\n",  num3);  // output: 100   (right-aligned)
    printf("%03d\n", num4);  // output: -1000 (negative overrides zero-pad)

    return 0; // 0 = program ran successfully
}
