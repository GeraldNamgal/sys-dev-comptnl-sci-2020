#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


# Closure for numerical differentiation
def numerical_diff(f, h):
    def approx_derivative(x):
        return (f(x + h) - f(x)) / h            # Return f' at x
    return approx_derivative


# TODO: Need? -- Function of interest
def f(x):
    return np.log(x)


# True f prime of f(x) = ln(x)
def f_prime_true(x):
    return 1 / x


# h values of interest
h1 = 1e-1
h2 = 1e-7
h3 = 1e-15

# f primes (finite difference) for different h values
fd_h1 = numerical_diff(f, h1)
fd_h2 = numerical_diff(f, h2)
fd_h3 = numerical_diff(f, h3)

# TODO
# Arbitrary x values of interest where 0.2 <= x <= 0.4
#x_values = [0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4]
x_values = np.linspace(0.2, 0.4, 100)

# Initialize lists for f prime values
true_prime_vals = []
fd_h1_values = []
fd_h2_values = []
fd_h3_values = []

# Get f prime values using x values
for x in x_values:
    true_prime_vals.append(f_prime_true(x))
    fd_h1_values.append(fd_h1(x))
    fd_h2_values.append(fd_h2(x))
    fd_h3_values.append(fd_h3(x))

# TODO: Plot the lines
plt.plot(x_values, true_prime_vals, linestyle=':', label='true derivative')
plt.plot(x_values, fd_h1_values, label='h1')
plt.plot(x_values, fd_h2_values, linestyle='-', label='h2')
plt.plot(x_values, fd_h3_values, label='h3')
plt.title('TODO')
plt.xlabel('TODO')
plt.ylabel('f prime')
plt.legend()
plt.show()


# References:
# - https://youtu.be/Qm1TDobNrns
