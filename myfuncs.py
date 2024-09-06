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

def sqrt(x, printhow=0, initial_guess=1, kmax=100, tol=1e-14):
    # computing s = sqrt(x) using newton method
    # x is a real number
    # initial_guess is the initial guess for newton method, default is 1
    # kmax is the max number of iterations, default is 100
    # tol is the tolerance to terminate newton method, default is 1e-14

    # input validation
    if x < 0:
        print('Input is negative')
        return -1
    
    if x == 0:
        return 0

    # transfers x from int to float
    x = x*1.0

    # main loop for newton method
    s = initial_guess*1.0
    for k in range(kmax):
        sold = s
        s = 0.5*(s+x/s)

        # choose to print information to screen
        if printhow == 1:
            print(k+1, abs(s-sold))

        # check change in two successive steps for termination
        if abs(s-sold)<tol:
            break


    return s

def myfactorial(n, printhow=0):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    s = 1
    for k in range(1, n + 1):
        s *= k
        if printhow == 1:
            print(f"{k}! = {s}")
    return s

def myexp(x, kmax=100, tol=1e-14, printhow=0):
    if kmax <= 0:
        raise ValueError("kmax must be a positive integer")
    
    e = np.e
    x0 = int(np.floor(x))
    z = x - x0
    exp0 = e ** x0
    
    s = 1.0
    term = 1.0
    for k in range(1, kmax + 1):
        term *= z / k
        s += term
        if printhow == 1:
            print(f"Iteration {k}, Term: {term}, Partial Sum: {s}")
        if abs(term) < tol:
            break
    return exp0 * s
    
def mylog(x, kmax=100, tol=1e-14, printhow=0):
    # Doesn't really need initial_guess because x serves as a good starting point
    if x <= 0:
        raise ValueError("Input must be greater than 0")
    if kmax <= 0:
        raise ValueError("kmax must be a positive integer")

    s = x
    for k in range(kmax):
        f_s = np.exp(s) - x
        fp_s = np.exp(s)
        s_new = s - f_s / fp_s
        if printhow == 1:
            print(f"Iteration {k+1}: log({x}) = {s_new}, Change = {abs(s_new - s)}")
        if abs(s_new - s) < tol:
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
        