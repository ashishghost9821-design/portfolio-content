#include <stdio.h>
#include <math.h>

int main() {

    /*
     * ╔══════════════════════════════════════════╗
     *        C PROGRAMMING - MATH FUNCTIONS
     *       Bro Code Tutorial | My Notes
     * ╚══════════════════════════════════════════╝
     */

    /* ─────────────────────────────────────────
     * SECTION 1: MATH.H LIBRARY
     * ─────────────────────────────────────────
     * <math.h> provides built-in functions for
     * common mathematical operations like square
     * roots, powers, rounding, and trigonometry.
     */

    float x = 9;

    // sqrt(x) -> square root of x
    // returns the square root of a number
    printf("sqrt:  %f\n", sqrt(x));

    // pow(x, 4) -> x to the power of 4
    // raises x to the given exponent
    printf("pow:   %f\n", pow(x, 4));

    /* ─────────────────────────────────────────
     * SECTION 2: ROUNDING FUNCTIONS
     * ─────────────────────────────────────────
     * round() -> nearest whole number
     * ceil()  -> always rounds UP
     * floor() -> always rounds DOWN
     */

    // round(x) -> round to nearest whole number
    // 9.5 and above rounds up, below rounds down
    printf("round: %f\n", round(x));

    // ceil(x) -> ceiling, always rounds UP
    // even 9.1 becomes 10.0
    printf("ceil:  %f\n", ceil(x));

    // floor(x) -> floor, always rounds DOWN
    // even 9.9 becomes 9.0
    printf("floor: %f\n", floor(x));

    /* ─────────────────────────────────────────
     * SECTION 3: ABSOLUTE VALUE & LOGARITHM
     * ─────────────────────────────────────────
     * fabs() -> absolute value for floats/doubles
     * log()  -> natural logarithm (base e)
     */

    // fabs(x) -> absolute value for float
    // use fabs() NOT abs() — abs() is for int only
    printf("fabs:  %f\n", fabs(x));

    // log(x) -> natural logarithm (base e)
    // opposite of e^x
    printf("log:   %f\n", log(x));

    /* ─────────────────────────────────────────
     * SECTION 4: TRIGONOMETRIC FUNCTIONS
     * ─────────────────────────────────────────
     * sin(), cos(), tan() all expect the angle
     * in RADIANS, not degrees.
     */

    // sin(x) -> sine of x
    // x must be in radians, not degrees
    printf("sin:   %f\n", sin(x));

    // cos(x) -> cosine of x
    // x must be in radians, not degrees
    printf("cos:   %f\n", cos(x));

    // tan(x) -> tangent of x
    // x must be in radians, not degrees
    printf("tan:   %f\n", tan(x));

    return 0;
}
