#include <stdio.h>
#include <math.h>

/*
 * ╔══════════════════════════════════════════════╗
 *     C PROGRAMMING - COMPOUND INTEREST CALCULATOR
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 *
 * Concepts practiced:
 *   -> pow() from <math.h> (compile with -lm)
 *   -> %% to print a literal % in printf
 *   -> converting percentage to decimal (/ 100)
 *   -> mixed int and double variables
 *
 * FORMULA: A = P * (1 + r/n)^(n*t)
 *   P = principal  (starting amount)
 *   r = rate       (annual interest as decimal)
 *   n = compounded (times per year)
 *   t = time       (years)
 *   A = total      (final amount)
 */

int main() {

    double principal       = 0.0; // starting amount
    double rate            = 0.0; // interest rate (converted to decimal)
    int    years           = 0;   // time in years
    int    timesCompounded = 0;   // how many times per year
    double total           = 0.0; // final result

    printf("--- Compound Interest Calculator ---\n");

    printf("Enter the principal (P): ");
    scanf("%lf", &principal);

    printf("Enter the interest rate %% (r): "); // %% prints literal %
    scanf("%lf", &rate);
    rate = rate / 100; // convert % to decimal e.g. 5 -> 0.05

    printf("Enter the # of years (t): ");
    scanf("%d", &years);

    printf("Enter # of times compounded per year (n): ");
    scanf("%d", &timesCompounded);

    // apply compound interest formula using pow() from <math.h>
    total = principal * pow(1 + rate / timesCompounded, timesCompounded * years);

    printf("After %d years, the total will be: $%.2f\n", years, total);

    return 0;
}
