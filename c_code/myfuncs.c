#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int binomial (int n, int k) {
    int factorial (int n);

    return factorial(n) / (factorial(k) * factorial(n - k));
}

int factorial(int n) {
    if (n <= 1) {
        return 1; // base case
    } else {
        return n * factorial(n-1);
    }
}

double myexp( double x, int kmax, double tol, int printhow) {
    printf("%.3lf, %d, %.14lf, %d\n", x, kmax, tol, printhow);
    if (kmax <= 0) {
        printf("kmax must be a positive integer: kmax = %d\n", kmax);
        return -1;
    }
    double e = 2.718281828459;
    double x0 = round(x);
    double z = x - x0;
    double exp0 = x0;
    double s = 1;
    double term = 1.0;
    for (int k = 1; k <= kmax + 1; k++) {
        term *= z / k;
        s += term;
        if (printhow == 1) {
            printf("Iteration %lf, Term: %lf, Partial Sum: %lf\n", k, term, s);
        }
        if (fabs(term) < tol) {
            break;
        }
    }
    return exp0 * s;
}

double myexp( double x, int kmax, double tol, int printhow) {
    printf("%.3lf, %d, %.14lf, %d\n", x, kmax, tol, printhow);
    if (kmax <= 0) {
        printf("kmax must be a positive integer: kmax = %d\n", kmax);
        return -1;
    }
    const double e = 2.718281828459;
    int x0 = (int)round(x); // Non-fractional part of x
    double exp0 = pow(e, x0);// Non-fractional part of exp(x)
    double z = x - x0;
    double sum = 0.0;
    // Compute fractional part of exp(x) with z
    for (int k = 0; k <= kmax; k++) {
        double term = pow(z, k) / factorial(k);
        sum += term;
        if (printhow == 1) {
            printf("Iteration %d, Term: %.14lf, Partial Sum: %.14lf\n", k, term, sum);
        }
        if (fabs(term) < tol) {  // Stop if the term is smaller than the tolerance
            break;
        }
    }
    return exp0 * sum;  // Final result: e^x0 * sum of series for exp(z)z
}