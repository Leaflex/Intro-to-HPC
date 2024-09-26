#include <stdio.h>
int main() {
    int binomial(int n, int k);

    printf("\n Pascal's Triangle:\n\n");
    for (int n = 0; n <= 10; n++) {
        for (int k = 0; k <= n; k++) {
            int ans = binomial(n, k);
            printf("%5i", ans);
            if (k == n) {
                printf("\n"); 
            }
        }
    }
    printf("\n");
    return 0;
}

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