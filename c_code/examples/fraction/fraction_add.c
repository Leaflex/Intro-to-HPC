#include <stdio.h>
#include "fraction.h"

void fraction_add(const fraction* a, const fraction* b, fraction * sum) {
    sum->denom = a->denom * b->denom;
    sum->numer = a->numer * b->denom + b->numer * a->denom;

    void fractin_reduce(fraction* sum);
    fraction_reduce(sum);
};