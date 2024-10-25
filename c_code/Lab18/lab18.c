#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {
    int N = 100000;  // Number of rows in matrix A
    int K = 200;     // Number of columns in matrix A
    double *w = (double*)malloc(N * sizeof(double));
    int i, j;

    // Start timing
    double start_time = omp_get_wtime();

    // Parallel computation of w using OpenMP
    #pragma omp parallel for private(j)
    for (i = 0; i < N; i++) {
        w[i] = 0.0;
        for (j = 0; j < K; j++) {
            double A_ij = 1.0 / (i + 1 + j);
            double v_j = 1.0 / (j + 1);
            w[i] += A_ij * v_j;
        }
    }

    // End timing
    double end_time = omp_get_wtime();

    // Print out the time taken for computation
    printf("Time taken: %f seconds\n", end_time - start_time);

    // Free allocated memory
    free(w);

    return 0;
}
