#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


# Closure for numerical differentiation
def numerical_diff(f, h):
    def approx_derivative(x):                   # Define inner fxn
        return (f(x + h) - f(x)) / h            # Inner fxn returns f' at x
    return approx_derivative                    # Return inner fxn


# Given function is f(x) = ln(x)
def f(x):
    return np.log(x)


# True f prime of given function
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

# Arbitrary x values for defined domain: 0.2 <= x <= 0.4
x_values = np.linspace(0.2, 0.4, 50)

# Initialize lists for f prime values
true_prime_vals = []
fd_h1_values = []
fd_h2_values = []
fd_h3_values = []

# Get f prime values with x values as input
for x in x_values:
    true_prime_vals.append(f_prime_true(x))
    fd_h1_values.append(fd_h1(x))
    fd_h2_values.append(fd_h2(x))
    fd_h3_values.append(fd_h3(x))

plt.plot(x_values, true_prime_vals, linestyle=':', label='f\'(x) exactly')
plt.plot(x_values, fd_h1_values, label='f\'(x) for h = 1e-1')
plt.plot(x_values, fd_h2_values, linestyle='-', label='f\'(x) for h = 1e-7')
plt.plot(x_values, fd_h3_values, label='f\'(x) for h = 1e-15')
plt.title('Derivative of \'f(x) = ln(x)\' Vs. \'x\' for Various \'h\' (Delta x)')
plt.xlabel('x')
plt.ylabel('f \'(x)')
plt.legend()

# Problem 1 Part C
print('Answer to Q-a: The true derivative is best approximated when the value '
      'of h is 1e−7. For values of h that are too large, the finite difference '
      'function approximates the derivative imprecisely which is expected '
      '(since h is further from 0). On the other hand, values of h that are '
      'too small suffer from floating point error. Floating point errors are '
      'ultimately caused by limits with machine precision, i.e., there are '
      'finite resources within a system\'s architecture. When a value such '
      'as h is too close to the precision limit of a machine, the value gets '
      'amplified and made bigger than it should be, e.g., when it\'s used in a '
      'calculation. Results from numerical analysis indicate that a practical '
      'value to use for h is the square root of machine precision (for first-'
      'order methods).')
print('\nAnswer to Q-b: Automatic differentiation addresses these problems by '
      'the fact that it doesn\'t use finite difference allowing it to be both '
      'accurate to machine precision and stable. It further achieves these '
      'qualities through the use of embedded symbolic derivatives and '
      'elementary functions when differentiating in either forward or reverse '
      'mode.')

# Show the plot
plt.show()


# References:
# - https://youtu.be/Qm1TDobNrns
# - https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html
