#include <stdio.h>
#include <stdlib.h>
#include "node.h"

/**
 * @brief Deletes the entire stack.
 *
 * Iteratively frees all nodes in the stack, starting from the top,
 * and sets the top pointer to NULL. Displays a goodbye message.
 *
 * @param top A pointer to the pointer of the top node of the stack.
 */
void DeleteStack (node ** top) {
    node* temp;
    while (* top != NULL) {
        temp = *top;
        *top = (* top)->next;
        free(temp);
    }

    printf ("\n Goodbye !\n\n");
}
