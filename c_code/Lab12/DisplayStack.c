#include <stdio.h>
#include <stdlib.h>
#include "node.h"

/**
 * @brief Displays the entire stack of cards.
 *
 * Prints the position, card value, suit, address, and next node address for each node.
 *
 * @param top A pointer to the top node of the stack.
 */
void DisplayStack (node* top) {
    if (top == NULL) { 
        printf(" Stack is emtpy\n");
        return;
    }

    printf (" ---------------------------------------------\n");
    printf (" |Pos :| Card :| Suit :| Address : | Next: |\n");
    printf (" ---------------------------------------------\n");
    PrintNode(top);
    printf (" ---------------------------------------------\n");
}

void PrintNode (node* top) {
    printf (" |%3i |%6s |%9s |%15p |%15p |\n",
    top-> position ,top-> Card, top-> Suit ,top ,top-> next);
    if (top-> next == NULL) {
        return;
    }
    PrintNode (top-> next);
}