#!/usr/bin/env python3

import myfuncs as my, numpy as np
test_values = [0.5, 1, 2, 5, 10]

print("Comparing exp(x):")
for val in test_values:
    my_exp = my.myexp(val)
    np_exp = np.exp(val)
    print(f"x = {val}: myexp = {my_exp}, np.exp = {np_exp}, difference = {abs(my_exp - np_exp)}")

print("\nComparing log(x):")
for val in test_values:
    my_log = my.mylog(val)
    np_log = np.log(val)
    print(f"x = {val}: mylog = {my_log}, np.log = {np_log}, difference = {abs(my_log - np_log)}")
    