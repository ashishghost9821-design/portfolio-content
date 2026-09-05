#include <stdio.h>
#include <stdbool.h>
#include <string.h>

/*
 * ╔══════════════════════════════════════════════╗
 *            C PROGRAMMING - STRUCT
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 */

/* ═══════════════════════════════════════════════
 * WHAT IS A STRUCT?
 * ═══════════════════════════════════════════════
 * A user-defined data type that groups multiple
 * variables of DIFFERENT types under one name.
 *
 * Think of it like a custom blueprint/template.
 * Each variable inside is called a "member" or "field".
 *
 * Syntax:
 *   typedef struct {
 *       type member1;
 *       type member2;
 *   } TypeName;
 *
 * Accessing members:
 *   variable.member
 *   student1.name, student1.age, student1.gpa
 *
 * IMPORTANT: every member line MUST end with ;
 * Missing ; is a very common bug with structs!
 */

typedef struct {
    char  name[50];
    int   age;
    float gpa;
    bool  isFullTime; // DON'T forget the semicolon here!
} Student;

/* ═══════════════════════════════════════════════
 * FUNCTION PROTOTYPE
 * ═══════════════════════════════════════════════
 * Passing a struct to a function — works like
 * passing any other variable. The function gets
 * its own COPY of the struct (not the original).
 */
void printStudent(Student student);

int main() {

    /* ───────────────────────────────────────────
     * EXAMPLE 1: initialize struct with values
     * values must match member ORDER exactly:
     * {name, age, gpa, isFullTime}
     * ─────────────────────────────────────────── */
    Student student1 = {"Spongebob", 38, 2.5, true};
    Student student2 = {"Patrick",   36, 1.0, false};

    /* ───────────────────────────────────────────
     * EXAMPLE 2: {0} initialization
     * {0} sets ALL members to their zero equivalent:
     *   int   -> 0
     *   float -> 0.0
     *   char  -> '\0' (empty string)
     *   bool  -> false
     * useful when you want to fill values later
     * ─────────────────────────────────────────── */
    Student student3 = {0};

    /* ───────────────────────────────────────────
     * EXAMPLE 3: strcpy() to set string member
     * you CANNOT assign a string with = after init:
     *   student3.name = "Sandy";  -> ERROR
     * strcpy() copies a string INTO the char array:
     *   strcpy(destination, source);
     * needs #include <string.h>
     * ─────────────────────────────────────────── */
    strcpy(student3.name, "Sandy"); // copy "Sandy" into student3.name
    student3.age        = 27;
    student3.gpa        = 4.0f;
    student3.isFullTime = true;

    /* ───────────────────────────────────────────
     * EXAMPLE 4: struct initialized with {0}
     * then filled member by member
     * ─────────────────────────────────────────── */
    Student student4 = {0};
    strcpy(student4.name, "Squidward");
    student4.age        = 40;
    student4.gpa        = 2.0f;
    student4.isFullTime = false;

    // print all students using the function
    printStudent(student1);
    printStudent(student2);
    printStudent(student3);
    printStudent(student4);

    return 0;
}

/* ═══════════════════════════════════════════════
 * FUNCTION DEFINITION
 * ═══════════════════════════════════════════════
 * Access each member using dot notation: student.member
 * Ternary used for bool -> prints "Yes" or "No"
 */
void printStudent(Student student) {
    printf("Name:      %s\n",  student.name);
    printf("Age:       %d\n",  student.age);
    printf("GPA:       %.2f\n", student.gpa);
    printf("Full-time: %s\n",  (student.isFullTime) ? "Yes" : "No");
    printf("\n");
}
