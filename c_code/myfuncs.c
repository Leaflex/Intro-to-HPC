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

double mylog(double x, int kmax, double tol, int printhow) {
    printf("%.3lf, %d, %.14lf, %d\n", x, kmax, tol, printhow);
    if (x <= 0) { 
        printf("x must be greater than 0: x = %lf\n", x);
        return -1;
    }
    if (kmax <= 0) {
        printf("kmax must be a positive integer: kmax = %d\n", kmax);
        return -1;
    }
    double s = x;
    for (int i = 0; i < kmax; i++) {
        double f_s = exp(s) - x;
        double fp_s = exp(s);
        double s_new = s - f_s / fp_s;
        if (printhow == 1) {
            printf("Iteration %3d: log(%.3lf) = %10.6lf, Change = %.14lf\n", i, x, s_new, fabs(s_new - s));
        }
        if (fabs(s_new - s) < tol) {
            return s_new;
        }
        s = s_new;
    }
    return s;
}