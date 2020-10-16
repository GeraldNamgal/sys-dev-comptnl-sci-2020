#!/usr/bin/env python3

def numerical_diff(f, h):
    def approx_derivative(x):
        return (f(x + h) - f(x)) / h         # Return f' at x
    return approx_derivative
