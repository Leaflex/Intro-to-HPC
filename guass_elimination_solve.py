#!/usr/bin/env python3
import myfuncs as my
import numpy as np

# Coefficient matrix A
A = np.array([
    [-2, 0, 1],
    [-1, 7, 1],
    [5, -1, 1]
], dtype=float)

# Constant matrix B
B = np.array([-4, -50, -26], dtype=float)

print(f"A: {A}\n")
print(f"B: {B}\n")

myOutput = my.myGaussianElim(A, B)
numpyOutput = np.linalg.solve(A, B)
print(f"myGaussianElim(A, B): {myOutput}\n\n")
print(f"np.linalg.solve(A, B): {numpyOutput}")
