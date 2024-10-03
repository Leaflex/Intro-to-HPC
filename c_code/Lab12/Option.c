#include <stdio.h>
#include <stdlib.h>
#include "node.h"

/**
 * @brief Prompts the user for an option and reads their choice.
 *
 * This function displays a prompt to the user, asking for their menu
 * choice, and reads the input value. The input is expected to be a
 * single digit integer corresponding to the user's choice in the menu.
 *
 * @return int The user's choice as an integer.
 */
int QueryOption() {
    int option;
    printf (" ENTER CHOICE : ");
    scanf ("%i", & option );
    return option ;
}

/**
 * @brief Executes the selected option from the menu.
 *
 * This function processes the user's selected option and performs the
 * corresponding action. It allows the user to manage a stack of cards
 * by adding new cards, removing the top card, peeking at the top card,
 * displaying the stack, or showing the stack size.
 *
 * @param const int option The user's selected option from the menu.
 * @param node** top A pointer to the pointer of the top node in the stack.
 */
void ExecuteOption (const int option , node** top) {
    char suit[9]; 
    char card[6];
    int size;
    switch (option) {
        case 0: // Display available options
            DisplayOptions ();
            break;
        case 1: // Enter a new value then push new node to stack
            printf (" Enter card value (1 - 10, J, Q, K, A): ");
            scanf (" %5s", card);
            printf (" Enter suit for the card: ");
            scanf ("%8s", suit);
            Push(suit, card, top);
            break;
        case 2: // Pop top value off of stack
            if (*top != NULL) {
                Pop(top, suit, card);
                printf(" Pop value = %s, %s\n", suit, card);
            } else { 
                printf(" Stack is empty\n");
            }
            break ;
        case 3: // Peek at top value on stack
            if ((* top)!= NULL) {
                Peek(*top);
            }
            else {
                printf (" Stack is empty\n");
            }
            break;
        case 4: // Display the entire stack
            DisplayStack(*top);
            break;
        case 5: // Print stack size
            GetStackSize (*top ,&size );
            printf (" Stack size is %i\n", size);
            break;
        case 6: // Do nothing here , but this causes code to end
            break;
        default:
            printf(" Error : incorrect option . Try again .\n");
            break;
    }
}