#include <stdio.h>

/**
 * @brief Displays the menu of stack operation options.
 *
 * This function prints the available options for interacting with the
 * stack, including pushing, popping, peeking, displaying the stack,
 * getting the stack size, and exiting the program.
 */
void DisplayOptions () {
    printf ("\n 0 - List Options ");
    printf ("\n 1 - Push (a single node)");
    printf ("\n 2 - Pop (the top node)");
    printf ("\n 3 - Peek (at the top node)");
    printf ("\n 4 - Dipslay (the entire stack )");
    printf ("\n 5 - Get stack size");
    printf ("\n 6 - Exit");
    printf ("\n");
}