#!/usr/bin/env python3

import myfuncs as my
import numpy as np
import math

test_values = [0.5, 1, 2, 5, 10]

# Comparing exp(x)
print("Comparing exp(x):")
for val in test_values:
    my_exp = my.myexp(val, printhow=1)
    np_exp = np.exp(val)
    print(f"x = {val}: myexp = {my_exp}, np.exp = {np_exp}, difference = {abs(my_exp - np_exp)}")

# Comparing log(x)
print("\nComparing log(x):")
for val in test_values:
    my_log = my.mylog(val, printhow=1)
    np_log = np.log(val)
    print(f"x = {val}: mylog = {my_log}, np.log = {np_log}, difference = {abs(my_log - np_log)}")

# Comparing factorial(n)
print("\nComparing factorial(n):")
factorial_values = [0, 1, 5, 10]
for val in factorial_values:
    my_fact = my.myfactorial(val, printhow=1)
    np_fact = math.factorial(val)
    print(f"n = {val}: myfactorial = {my_fact}, math.factorial = {np_fact}, difference = {abs(my_fact - np_fact)}")
