#include <stdio.h>
#include <math.h>

/*
 * ╔══════════════════════════════════════════════╗
 *        C PROGRAMMING - SPHERE CALCULATOR
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 *
 * Concepts practiced:
 *   -> const keyword (value that cannot change)
 *   -> pow() from <math.h> (compile with -lm)
 *   -> double for high precision decimals
 *   -> multiple formulas using same variable
 *
 * FORMULAS:
 *   Area         = PI * r^2
 *   Surface Area = 4 * PI * r^2
 *   Volume       = (4/3) * PI * r^3
 *
 * NOTE: use 4.0/3.0 NOT 4/3
 *       4/3 in C = 1 (integer division truncates decimal)
 *       4.0/3.0  = 1.333... (correct float division)
 */

int main() {

    // const = value that cannot be changed after declaration
    const double PI = 3.14159;

    double radius      = 0.0;
    double area        = 0.0;
    double surfaceArea = 0.0;
    double volume      = 0.0;

    printf("Enter the radius: ");
    scanf("%lf", &radius);

    area        = PI * pow(radius, 2);           // PI * r^2
    surfaceArea = 4 * PI * pow(radius, 2);       // 4 * PI * r^2
    volume      = (4.0/3.0) * PI * pow(radius, 3); // (4/3) * PI * r^3
    // pow(radius, 2) same as radius * radius
    // pow(radius, 3) same as radius * radius * radius

    printf("Area:         %.2lf\n", area);
    printf("Surface Area: %.2lf\n", surfaceArea);
    printf("Volume:       %.2lf\n", volume);

    return 0;
}
