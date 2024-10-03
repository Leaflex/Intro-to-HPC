#include <stdio.h>
#include "node.h"

/**
 * @brief Displays the top card of the stack.
 *
 * Prints the card value and suit of the top node without removing it.
 *
 * @param top A pointer to the top node of the stack.
 */
void Peek(node* top) {
    printf(" Top card is %s, %s \n",top -> Card, top -> Suit);
}
