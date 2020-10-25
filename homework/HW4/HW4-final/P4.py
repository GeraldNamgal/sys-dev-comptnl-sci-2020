#!/usr/bin/env python3

class AutoDiffToy:
    def __init__(self, eval_point):
        self.val = eval_point               # Set function value
        self.der = None                     # Initialize derivative value

    def __mul__(self, other):
        try:
            return AutoDiffToy(self.val * other.val)
        except AttributeError:
            try:
                new_obj = AutoDiffToy(self.val * other)
                new_obj.der = other
                return new_obj
            except Exception as err:
                print(f'Got an error: \'{err}\'')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        try:
            return AutoDiffToy(self.val + other.val)
        except AttributeError:
            try:
                new_obj = AutoDiffToy(self.val + other)
                new_obj.der = self.der      # Pass derivative to new object
                return new_obj
            except Exception as err:
                print(f'Got an error: \'{err}\'')

    def __radd__(self, other):
        return self.__add__(other)


# Demoing AutoDiffToy...
a = 2.0                                     # Value to evaluate at
x = AutoDiffToy(a)
alpha = 2.0
beta = 3.0

f = alpha * x + beta
print(f.val, f.der)
f = x * alpha + beta
print(f.val, f.der)
f = beta + alpha * x
print(f.val, f.der)
f = beta + x * alpha
print(f.val, f.der)
