#include <stdlib.h>
#include "node.h"

/**
 * @brief Main function for the card stack program.
 *
 * This function serves as the entry point of the program, initializing
 * the stack and allowing the user to interact with it through a menu
 * of options. The user can add cards to the stack, view the stack,
 * and manage the stack until they choose to exit the program.
 *
 * @return int Returns 0 upon successful execution.
 */
int main () {
    node* top = NULL;

    int option = 0;
    while(option != 6) {
        ExecuteOption(option, &top);
        option = QueryOption();
    }

    DeleteStack(&top);
    return 0;
}
