def myGaussianElim(A, B):
    n = len(B)

    # Set diagonals to 1
    for i in range(n):
        factor = A[i][i]
        for j in range(i, n):
            A[i][j] = A[i][j] / factor
        B[i] = B[i] / factor

        # Eliminate lower triangle
        for k in range(i+1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]
         
    # Back substitution
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = B[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]

    return x
