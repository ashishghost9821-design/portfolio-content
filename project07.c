#include <stdio.h>

int main() {

    // CALCULATOR PROGRAM

    char   operator = '\0';
    double num1     = 0.0;
    double num2     = 0.0;
    double result   = 0.0;

    printf("Enter the First number: ");
    scanf("%lf", &num1);

    printf("Enter the operator (+ - * /): ");
    scanf(" %c", &operator); // space before %c clears leftover '\n'

    printf("Enter the Second number: ");
    scanf("%lf", &num2);

    /* ═══════════════════════════════════════════════
     * SWITCH STATEMENT
     * ═══════════════════════════════════════════════
     * Checks operator character against each case.
     * break -> stops fall-through to next case.
     * default -> runs if no case matches.
     *
     * WARNING: forgetting break causes fall-through
     * meaning it runs the next case automatically!
     */

    switch(operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if(num2 == 0) {
                printf("You can't divide by zero!\n");
            }
            else {
                result = num1 / num2;
            }
            break; // THIS was missing — caused fall-through to default
        default:
            printf("Invalid Operator!\n");
    }

    printf("Result: %.4lf\n", result);

    return 0;
}
