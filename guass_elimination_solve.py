#!/usr/bin/env python3
import mylinalg as my
import numpy as np

# Coefficient matrix A
A = np.array([
    [-2, 0, 1],
    [-1, 7, 1],
    [5, -1, 1]
], dtype=float)
a = A.copy()

# Constant matrix B
B = np.array([-4, -50, -26], dtype=float)
b = B.copy()

print(f"A: {A}\n")
print(f"B: {B}\n")

numpyOutput = np.linalg.solve(A, B)
print(f"np.linalg.solve(A, B): {numpyOutput}\n")

myOutput = [float(x) for x in my.myGaussianElim(A, B)]
print(f"myGaussianElim(A, B): {myOutput}\n")
