#include <stdio.h>
#include <stdlib.h>
#include <math.h>

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

int main(void) {
    // Array of x values
    double x_values[5];
    double results[5];
    int kmax = 100;
    double tol = 1e-14;
    int printhow = 0;

    printf("Enter an integer value for kmax (100): ");
    scanf("%d", &kmax);
    printf("Enter a double value for tolerance (1e-14): ");
    scanf("%lf", &tol);
    printf("Enter a integer value for printhow (0): ");
    scanf("%d", &printhow);
    
    printf("Enter 5 values for x: ");
    for (int i = 0; i < 5; i++) {
        scanf("%lf", &x_values[i]);  // Input the values for x
    }
    
    for (int i = 0; i < 5; i++) {
        results[i] = myexp(x_values[i], kmax, tol, printhow);  // Calculate e^x
    }

    // Print results
    printf("Computed exp(x) values:\n");
    for (int i = 0; i < 5; i++) {
        printf("exp(%.2lf) = %.14lf\n", x_values[i], results[i]);
    }
    
    // Save results to file
    FILE *file = fopen("exp_results.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    for (int i = 0; i < 5; i++) {
        fprintf(file, "exp(%.2lf) = %.14lf\n", x_values[i], results[i]);
    }
    fclose(file);
    
    return 0;
}
