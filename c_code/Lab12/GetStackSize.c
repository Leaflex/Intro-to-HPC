#include <stdlib.h>
#include "node.h"

/**
 * @brief Calculates the size of the stack.
 *
 * Iterates through the stack and counts the number of nodes,
 * storing the result in the provided stack_size pointer.
 *
 * @param top A pointer to the top node of the stack.
 * @param stack_size Pointer to an integer to store the size of the stack.
 */
void GetStackSize(node* top, int* stack_size) {
    *stack_size = 0; // Initialize the stack size to 0

    while (top != NULL) {
        (*stack_size)++; // Increment the count for each node
        top = top->next; // Move to the next node
    }
}
