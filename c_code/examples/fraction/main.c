#include <stdio.h>
#include "fraction.h"

int main() {
    fraction a, b, sum;

    a.numer = -1; a.denom = 10;
    b.numer = -3; b.denom = 8;

    void fraction_add(
        const fraction* a,
        const fraction* b,
        fraction * sum
    );
    fraction_add(&a, &b, &sum);

    printf("\n %i/%i + %i/%i = %i/%i\n\n", a.numer, a.denom, b.numer, b.denom, sum.numer, sum.denom);
    
    return 0;
}