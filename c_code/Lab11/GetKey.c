#include <stdio.h>

char GetKey() {
    char key;
    printf("\nEnter key to search: ");
    scanf(" %c", &key); // Note the space before %c to ignore leading whitespace
    return key;
}
