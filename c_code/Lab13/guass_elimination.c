#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include "matrix.h"

/**
 * @brief Generates a sub-triangular matrix L where diagonal elements are 1 and
 *        lower triangular elements are random values between 0 and 1.
 * 
 * @param N The size of the matrix (N x N).
 * 
 * @return A matrix L of size (N x N) where diagonal elements are 1 and 
 *         lower triangular elements are random values between 0 and 1.
 */
matrix generate_L(int N) {
    matrix L = new_matrix(N, N);
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= i; j++) {
            if (i == j) {
                mget(L, i, j) = 1.0;  // Diagonal elements are 1
            } else {
                mget(L, i, j) = ((double) rand() / RAND_MAX);  // Random numbers in the lower triangle
            }
        }
    }
    return L;
}

/**
 * @brief Computes matrix A as the product of matrix L and its transpose L^T.
 * 
 * @param L Pointer to the sub-triangular matrix L (N x N).
 * 
 * @return The matrix A (N x N) which is the result of L * L^T.
 */
matrix compute_A(matrix* L) {
    matrix Lt = new_matrix(L->rows, L->cols);
    // Transpose of L
    for (int i = 1; i <= L->rows; i++) {
        for (int j = 1; j <= L->cols; j++) {
            mget(Lt, j, i) = mgetp(L, i, j);
        }
    }
    // A = L * Lt
    matrix A = matrix_mult(L, &Lt);
    return A;
}

/**
 * @brief Generates a random vector b of size N with elements in the range [0, 1].
 * 
 * @param N The size of the vector.
 * 
 * @return A vector b of size N with random values between 0 and 1.
 */
vector generate_b(int N) {
    vector b = new_vector(N);
    for (int i = 1; i <= N; i++) {
        vget(b, i) = ((double) rand() / RAND_MAX);
    }
    return b;
}

/**
 * @brief Solves the system of linear equations Ax = b using Gaussian Elimination
 *        with partial pivoting and back substitution.
 * 
 * @param A Pointer to the matrix A (N x N) that will be modified during the process.
 * @param b Pointer to the vector b (N x 1) which will also be modified during the process.
 * 
 * @return The solution vector x (N x 1) that satisfies Ax = b.
 */
vector myGuassianElim(matrix* A, vector* b) {
    int N = A->rows;
    vector x = new_vector(N);
    
    // Gaussian elimination
    for (int i = 1; i <= N; i++) {
        // Partial pivoting
        int maxRow = i;
        for (int k = i + 1; k <= N; k++) {
            if (fabs(mgetp(A, k, i)) > fabs(mgetp(A, maxRow, i))) {
                maxRow = k;
            }
        }
        // Swap rows in A and b
        for (int k = i; k <= N; k++) {
            double tmp = mgetp(A, i, k);
            mgetp(A, i, k) = mgetp(A, maxRow, k);
            mgetp(A, maxRow, k) = tmp;
        }
        double tmp = vgetp(b, i);
        vgetp(b, i) = vgetp(b, maxRow);
        vgetp(b, maxRow) = tmp;

        // Elimination process
        for (int k = i + 1; k <= N; k++) {
            double factor = mgetp(A, k, i) / mgetp(A, i, i);
            for (int j = i; j <= N; j++) {
                mgetp(A, k, j) -= factor * mgetp(A, i, j);
            }
            vgetp(b, k) -= factor * vgetp(b, i);
        }
    }

    // Back substitution
    for (int i = N; i >= 1; i--) {
        vget(x, i) = vgetp(b, i);
        for (int j = i + 1; j <= N; j++) {
            vget(x, i) -= mgetp(A, i, j) * vget(x, j);
        }
        vget(x, i) /= mgetp(A, i, i);
    }

    return x;
}

int main() {
    int N = 5; // Matrix size
    srand(time(NULL)); // Seed for random number generation

    // Generate sub-triangular matrix L
    matrix L = generate_L(N);
    printf("L matrix:\n");
    print_matrix(&L);

    // Compute A = L * L^T
    matrix A = compute_A(&L);
    printf("A = L * L^T matrix:\n");
    print_matrix(&A);

    // Generate random vector b
    vector b = generate_b(N);
    printf("b vector:\n");
    print_vector(&b);

    // Solve the system Ax = b
    vector x = myGuassianElim(&A, &b);
    printf("Solution x vector:\n");
    print_vector(&x);

    return 0;
}
