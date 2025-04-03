"""
The bisection method is a technique for finding solutions (roots) to equations with a single
unknown variable. Given a polynomial function f, try to find an initial interval off by
random probe. Store all the updates in an Numpy array. Plot the root finding process using
the matplotlib/pyplot library.
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x - 9  # Example polynomial function

def find_initial_interval():
    x_values = np.linspace(-10, 10, 1000)
    for i in range(len(x_values) - 1):
        if f(x_values[i]) * f(x_values[i+1]) < 0:
            return x_values[i], x_values[i+1]
    return None, None

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    midpoints = []
    
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have opposite signs at the interval endpoints.")
    
    for _ in range(max_iter):
        c = (a + b) / 2.0
        midpoints.append(c)
        
        if abs(f(c)) < tol:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    return np.array(midpoints)

def plot_convergence(midpoints):
    plt.plot(midpoints, 'bo-', label='Midpoint Estimates')
    plt.axhline(midpoints[-1], color='r', linestyle='--', label=f'Root at {midpoints[-1]:.6f}')
    plt.xlabel('Iteration')
    plt.ylabel('Midpoint Value')
    plt.title('Bisection Method Convergence')
    plt.legend()
    plt.grid()
    plt.show()

# Find an initial interval
a, b = find_initial_interval()
if a is not None and b is not None:
    print(f"Initial interval: [{a}, {b}]")
    midpoints = bisection_method(f, a, b)
    plot_convergence(midpoints)
else:
    print("No valid interval found in the given range.")