#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *         C PROGRAMMING - ARRAY OF STRUCTS
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS AN ARRAY OF STRUCTS?
 * ═══════════════════════════════════════════════
 * An array where each element is a struct.
 * Helps organize and group together related data.
 *
 * Syntax:
 *   TypeName arrayName[] = {{...}, {...}, {...}};
 *
 * Accessing members:
 *   arrayName[index].member
 *   cars[0].model -> first car's model
 *   cars[1].year  -> second car's year
 *
 * sizeof trick to get count automatically:
 *   sizeof(cars) / sizeof(cars[0]) = number of structs
 */

typedef struct {
    char model[25];
    int  year;
    int  price;
} Car;

int main() {

    // each {} is one Car struct — must match member order
    // {model, year, price}
    Car cars[] = {{"Mustang",    2025, 32000},
                  {"Corvette",   2026, 68000},
                  {"Challenger", 2024, 29000}};

    // get total number of cars automatically
    int number = sizeof(cars) / sizeof(cars[0]);

    // loop through each Car struct and print its members
    for(int i = 0; i < number; i++) {
        printf("%s %d $%d\n", cars[i].model,
                               cars[i].year,
                               cars[i].price);
    }

    return 0;
}
