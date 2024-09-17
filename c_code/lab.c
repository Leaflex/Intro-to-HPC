#include <stdio.h>
#include <stdlib.h>
#include <math.h>

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

int main(int argc, char **argv) {
    if (argc < 5) {
        printf("Usage: ./lab <double x> <int kmax> <double tol> <int printhow>\n");
        printf("Example: ./lab7.o 25.0 100 1.0E-14 1\n");
        return 0;
    }
    double result = mylog(atof(argv[1]), atoi(argv[2]), atof(argv[3]), atoi(argv[4]));
    if (result > 0) {
        printf("\nResult of log(%.3lf) = %.5lf\n", atof(argv[1]), result);
    } else {
        printf("Something went wrong\n");
    }
    return 1;
}
