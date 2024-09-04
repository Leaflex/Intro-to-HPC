# Module of basic python math functions
import numpy as np

def mysqrt(x):
    kmax = 100
    s = 1.0 * x
    if s < 0:
        print('Input must be > 0')
        return 0
    else:
        for k in range(kmax):
            s = 0.5 * (s + x / s)
    return s

def myfactorial(n):
    s = 1
    for k in range(n):
        s = (k + 1) * s
    return s

def myexp(x):
    e = 2.7182818284590451
    x0 = int(round(x))
    z = x - x0
    exp0 = e ** x0
    
    kmax = 10 
    s = 1
    for k in range(kmax):
        s = s + z ** (k + 1) / myfactorial(k + 1)
        
    return exp0 * s
    
def mylog(x):
    if x <= 0:
        raise ValueError("Input must be greater than 0")
    s = x  
    tolerance = 1e-10
    kmax = 100
    for _ in range(kmax):
        f_s = 2.7182818284590451 ** s - x
        fp_s = 2.7182818284590451 ** s
        
        s_new = s - f_s / fp_s
        
        if abs(s_new - s) < tolerance:
            return s_new
        
        s = s_new
    
    return s

def compareMy():
    test_values = [0.5, 1, 2, 5, 10]

    print("Comparing exp(x):")
    for val in test_values:
        my_exp = myexp(val)
        np_exp = np.exp(val)
        print(f"x = {val}: myexp = {my_exp}, np.exp = {np_exp}, difference = {abs(my_exp - np_exp)}")

    print("\nComparing log(x):")
    for val in test_values:
        my_log = mylog(val)
        np_log = np.log(val)
        print(f"x = {val}: mylog = {my_log}, np.log = {np_log}, difference = {abs(my_log - np_log)}")
        