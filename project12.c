#include <stdio.h>
#include <ctype.h>

/*
 * ╔══════════════════════════════════════════════╗
 *           C PROGRAMMING - QUIZ GAME
 *           Bro Code Tutorial | My Notes
 * ╚══════════════════════════════════════════════╝
 *
 * Concepts practiced:
 *   -> 2D array of strings for questions and options
 *   -> char array for answer key
 *   -> toupper() from <ctype.h> to accept a or A
 *   -> sizeof to get question count automatically
 *   -> for loop to cycle through all questions
 *
 * WARNING: string literals placed next to each other
 * WITHOUT a comma get merged into ONE string by compiler
 *   WRONG: {"Hello" "World"}  -> "HelloWorld" (one string)
 *   RIGHT: {"Hello", "World"} -> two separate strings
 */

int main() {

    // each string is one question — MUST have commas between them
    char questions[][100] = {
        "What is the largest planet in the solar system?",
        "What is the hottest planet?",
        "What planet has the most moons?",
        "Is the Earth flat?"
    };

    // each string holds all options for one question
    char options[][100] = {
        "A. Jupiter\nB. Saturn\nC. Uranus\nD. Neptune",
        "A. Mercury\nB. Venus\nC. Earth\nD. Mars",
        "A. Earth\nB. Mars\nC. Jupiter\nD. Saturn",
        "A. Yes\nB. No\nC. Maybe\nD. Sometimes"
    };

    // correct answer for each question (index matched)
    char answerKey[] = {'A', 'B', 'D', 'B'};

    // sizeof trick to get count automatically
    // if you add more questions later, no need to update this
    int questionCount = sizeof(questions) / sizeof(questions[0]);

    char guess = '\0';
    int  score = 0;

    printf("*** QUIZ GAME ***\n");

    for(int i = 0; i < questionCount; i++) {
        printf("\n%s\n",   questions[i]); // print question
        printf("\n%s\n",   options[i]);   // print options
        printf("\nEnter your choice: ");
        scanf(" %c", &guess);             // space before %c clears '\n'

        guess = toupper(guess); // convert a->A, b->B so both work

        if(guess == answerKey[i]) {
            printf("CORRECT!\n");
            score++;
        }
        else {
            printf("Wrong! The answer was %c\n", answerKey[i]);
        }
    }

    printf("\nYour score: %d out of %d\n", score, questionCount);

    return 0;
}
