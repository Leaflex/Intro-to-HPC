#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "node.h"

/**
 * @brief Pushes a new node onto the top of the stack.
 *
 * This function creates a new node containing the specified suit and card value,
 * and adds it to the top of the stack. If the stack is empty, it initializes
 * the top node. The position of each node in the stack is updated accordingly.
 *
 * @param suit A pointer to a string representing the suit of the card.
 * @param card A pointer to a string representing the card value.
 * @param top A double pointer to the top node of the stack.
 */
void Push(const char* suit, const char* card, node** top) {
    if (* top == NULL) {
        *top =( node *) malloc(sizeof(struct node));
        (* top)->next = NULL;
        strcpy((* top)->Suit, suit);
        strcpy((* top)->Card, card);
        (* top)->position = 1;
    } else {
        node* temp;
        temp =( node *) malloc(sizeof(struct node));
        temp ->next = *top;
        strcpy(temp -> Suit, suit);
        strcpy(temp -> Card, card);
        temp -> position = 1;
        *top = temp;
        node* ptr = (* top)->next;
        while (ptr != NULL) {
            ptr -> position = ptr -> position +1;
            ptr = ptr ->next;
        }
    }
}

