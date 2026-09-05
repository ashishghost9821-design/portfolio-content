#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *      C PROGRAMMING - WEIGHT CONVERTER PROGRAM
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 *
 * Concepts practiced:
 *   -> if/else if/else for menu selection
 *   -> float arithmetic with conversion factor
 *   -> scanf for int (menu) and float (weight)
 *
 * FORMULAS:
 *   kg to lbs -> pounds     = kilograms * 2.20462
 *   lbs to kg -> kilograms  = pounds    / 2.20462
 */

int main() {

    int   choice     = 0;
    float pounds     = 0.0f;
    float kilograms  = 0.0f;

    printf("--- Weight Conversion Calculator ---\n");
    printf("1. Kilograms to Pounds\n");
    printf("2. Pounds to Kilograms\n");
    printf("Enter your choice (1 or 2): ");
    scanf("%d", &choice);

    if(choice == 1) {
        // kilograms -> pounds
        printf("Enter the weight in Kilograms: ");
        scanf("%f", &kilograms);
        pounds = kilograms * 2.20462; // conversion factor
        printf("%.2f kg is equal to %.2f lbs\n", kilograms, pounds);
    }
    else if(choice == 2) {
        // pounds -> kilograms
        printf("Enter the weight in Pounds: ");
        scanf("%f", &pounds);
        kilograms = pounds / 2.20462; // reverse conversion
        printf("%.2f lbs is equal to %.2f kg\n", pounds, kilograms);
    }
    else {
        printf("Invalid choice! Please enter 1 or 2\n");
    }

    return 0;
}
