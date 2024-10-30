#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "matrix.h"
#include <omp.h>


void usage(const char* program_name) {
    fprintf(stderr, "Usage: %s <num_threads> <vector_size>\n", program_name);
    exit(1);
}


// Fine-grain parallel normalization
void normalize_vector_fine_grain(vector x, int N, int thread_count) {
    double norm = 0.0;

    // Calculate 2-norm
    #pragma omp parallel for reduction(+:norm) num_threads(thread_count)
    for (int i = 1; i <= N; i++) {
        norm += fabs(vget(x, i));
    }

    // Normalize the vector
    #pragma omp parallel for num_threads(thread_count)
    for (int i = 1; i <= N; i++) {
        vget(x, i) = vget(x, i) / norm;
    }
}

// Coarse-grain parallel normalization
void normalize_vector_coarse_grain(vector x, int N, int thread_count) {
    double norm = 0.0; // Make norm a shared variable

    #pragma omp parallel num_threads(thread_count)
    {
        const int my_rank = omp_get_thread_num();
        const int N_per_thread = N / thread_count;
        const int istart = my_rank * N_per_thread + 1;
        const int iend = (my_rank + 1) * N_per_thread;

        double norm_thread = 0.0;
        for (int i = istart; i <= iend; i++) {
            norm_thread += fabs(vget(x, i));
        }

        #pragma omp critical
        norm += norm_thread; // Combine the results safely
    }

    // Normalize the vector outside the parallel region
    #pragma omp parallel for num_threads(thread_count)
    for (int i = 1; i <= N; i++) {
        vget(x, i) = vget(x, i) / norm;
    }
}


int main(int argc, char* argv[]) {
    void usage(const char* prog_name);
    srand(time(NULL));

    if (argc != 3) { usage(argv[0]); }
    const int thread_count = strtol(argv[1], NULL, 10);
    const int N = strtol(argv[2], NULL, 10);
    if (thread_count < 1 || N < 1) {
        usage(argv[0]);
    }

    vector x = new_vector(N);
    // Initialize the vector x with random values or a specific pattern
    #pragma omp parallel for num_threads(thread_count)
    for (int i = 1; i <= N; i++) {
        vget(x, i) = ((double)(rand() % 10000)) / 10000.0; // example initialization
    }

    // Measure WallTime for fine-grain parallel normalization
    double start_time = omp_get_wtime();
    normalize_vector_fine_grain(x, N, thread_count);
    double end_time = omp_get_wtime();
    printf("Fine-grain normalization time: %f seconds with %d threads and a N = %d\n", end_time - start_time, thread_count, N);

    // Reset vector x for coarse-grain normalization
    #pragma omp parallel for num_threads(thread_count)
    for (int i = 1; i <= N; i++) {
        vget(x, i) = ((double)(rand() % 10000)) / 10000.0; // reinitialize
    }

    // Measure WallTime for coarse-grain parallel normalization
    start_time = omp_get_wtime();
    normalize_vector_coarse_grain(x, N, thread_count);
    end_time = omp_get_wtime();
    printf("Coarse-grain normalization time: %f seconds with %d threads and a N = %d\n", end_time - start_time, thread_count, N);

    // Clean up vector resources
    delete_vector(&x);
    
    return 0;
}
