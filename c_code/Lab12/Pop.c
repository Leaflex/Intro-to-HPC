#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "node.h"

/**
 * @brief Removes the top node from the stack.
 *
 * Retrieves the suit and card values from the popped node,
 * updates the top pointer, and adjusts positions of remaining nodes.
 *
 * @param top A double pointer to the top node of the stack.
 * @param suit A pointer to a string for storing the suit of the popped node.
 * @param card A pointer to a string for storing the card value of the popped node.
 */
void Pop(node** top, char* suit, char* card) {
    if (*top == NULL) {
        return;
    }

    strcpy(suit, (*top)->Suit);
    strcpy(card, (*top)->Card);

    node* temp = *top;
    
    *top = (*top)->next;

    free(temp);

    // Update the positions of the remaining nodes
    node* ptr = *top;
    while (ptr != NULL) {
        ptr->position = ptr->position - 1;
        ptr = ptr->next;
    }
}
