#include <stdlib.h>
#include "node.h"

int main () {
    node* top = NULL;

    int option =0;
    while( option !=6) {
        ExecuteOption(option ,& top);
        option = QueryOption ();
    }

    DeleteStack(& top);
    return 0;
}
