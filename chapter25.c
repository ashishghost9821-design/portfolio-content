#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *           C PROGRAMMING - POINTERS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS A POINTER?
 * ═══════════════════════════════════════════════
 * A variable that stores the MEMORY ADDRESS
 * of another variable.
 *
 * Every variable lives somewhere in RAM.
 * That location has an address (like a house address).
 * A pointer stores that address.
 *
 * Syntax:
 *   int *pAge = &age;
 *    ^    ^      ^
 *    |    |      & = "address of" operator
 *    |    |          gives the memory address of age
 *    |    p = naming convention for pointers
 *    int* = pointer to an int
 *
 * TWO OPERATORS:
 *   &variable  -> gives ADDRESS of variable   (referencing)
 *   *pointer   -> gives VALUE at that address (dereferencing)
 *
 * WHY USE POINTERS?
 * Normally when you pass a variable to a function,
 * C makes a COPY — changes inside don't affect original.
 * With pointers you pass the ADDRESS — function changes
 * the ORIGINAL variable directly. Called "pass by reference".
 *
 * Visual:
 *   int age = 25;
 *   age  -> value: 25,  address: 0x7fff5c (example)
 *   pAge -> value: 0x7fff5c (stores age's address)
 *   *pAge -> 25 (goes to that address and reads value)
 */

void birthday(int *age); // takes a pointer to int

int main() {

    int age = 25;

    // & gives the memory address of age
    printf("Address of age: %p\n", &age);

    // pointer stores that address
    int *pAge = &age;
    printf("pAge holds:     %p\n", pAge);   // same address
    printf("Value at pAge:  %d\n", *pAge);  // 25 (dereferencing)

    // pass the POINTER (address) to function
    // function will change the original age variable
    birthday(pAge);
    printf("After birthday: %d years old\n", age); // age is now 26

    return 0;
}

/* ═══════════════════════════════════════════════
 * PASS BY REFERENCE
 * ═══════════════════════════════════════════════
 * (*age)++ means:
 *   1. go to the address stored in age pointer
 *   2. get the value there
 *   3. increment it by 1
 *
 * Parentheses around *age are important:
 *   (*age)++ -> increment the VALUE at address ✅
 *   *age++   -> increment the ADDRESS itself   ❌ (wrong)
 */
void birthday(int *age) {
    (*age)++; // dereference then increment original value
}
