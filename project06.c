#include <stdio.h>

/*
 * ╔══════════════════════════════════════════════╗
 *    C PROGRAMMING - TEMPERATURE CONVERTER PROGRAM
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 *
 * Concepts practiced:
 *   -> char input with scanf("%c")
 *   -> if/else if/else with char comparison
 *   -> float arithmetic with conversion formula
 *
 * FORMULAS:
 *   C to F -> fahrenheit = (celsius * 9/5) + 32
 *   F to C -> celsius    = (fahrenheit - 32) * 5/9
 *
 * NOTE: use 9/5 carefully — in C, integer division
 *   9/5 = 1 (truncated), BUT since celsius is float
 *   the compiler promotes it to float automatically.
 *   To be safe you can write 9.0/5.0 explicitly.
 */

int main() {

    char  choice     = '\0';
    float fahrenheit = 0.0f;
    float celsius    = 0.0f;

    printf("--- Temperature Conversion Program ---\n");
    printf("C. Celsius to Fahrenheit\n");
    printf("F. Fahrenheit to Celsius\n");
    printf("Is the temp in Celsius (C) or Fahrenheit (F)?: ");
    scanf(" %c", &choice); // space before %c clears leftover '\n'

    if(choice == 'C') {
        // Celsius -> Fahrenheit
        printf("Enter the temperature in Celsius: ");
        scanf("%f", &celsius);
        fahrenheit = (celsius * 9/5) + 32;
        printf("%.1f C is equal to %.1f F\n", celsius, fahrenheit);
    }
    else if(choice == 'F') {
        // Fahrenheit -> Celsius
        printf("Enter the temperature in Fahrenheit: ");
        scanf("%f", &fahrenheit);
        celsius = (fahrenheit - 32) * 5/9;
        printf("%.1f F is equal to %.1f C\n", fahrenheit, celsius);
    }
    else {
        printf("Invalid choice! Please enter C or F\n");
    }

    return 0;
}
