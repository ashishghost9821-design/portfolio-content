#include <stdio.h>
#include <string.h>

/*
 * ╔══════════════════════════════════════════════╗
 *        C PROGRAMMING - SHOPPING CART PROGRAM
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 *
 * Concepts practiced:
 *   -> fgets for string input
 *   -> scanf for int and float input
 *   -> arithmetic (price * quantity)
 *   -> mixed format specifiers in printf
 */

int main() {

    char  item[50] = "";
    float price    = 0.0f;
    int   quantity = 0;
    char  currency = '$';
    float total    = 0.0f;

    printf("What item would you like to buy?: ");
    fgets(item, sizeof(item), stdin);
    item[strlen(item) - 1] = '\0'; // remove trailing newline

    printf("What is the price for each?: ");
    scanf("%f", &price);

    printf("How many would you like?: ");
    scanf("%d", &quantity);

    total = price * quantity; // calculate total cost

    printf("\nYou have bought %d %s\n", quantity, item);
    printf("Total: %c%.2f\n", currency, total);

    return 0;
}
