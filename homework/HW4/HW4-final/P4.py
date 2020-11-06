#!/usr/bin/env python3

class AutoDiffToy:
    def __init__(self, eval_point, der_value=1.0):
        self.val = eval_point              # Set function value
        self.der = der_value               # Set derivative value

    def __mul__(self, other):              # Note: Applies product rule
        try:
            return AutoDiffToy(self.val * other.val,
                               self.der * other.val + self.val * other.der)
        except AttributeError:
            try:                           # other is scalar (has 0 derivative)?
                return AutoDiffToy(self.val * other, self.der * other)
            except Exception as err:
                print(f'Got an error: \'{err}\'')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):              # Note: Applies sum rule
        try:
            return AutoDiffToy(self.val + other.val, self.der + other.der)
        except AttributeError:
            try:                           # other is scalar (has 0 derivative)?
                return AutoDiffToy(self.val + other, self.der)
            except Exception as err:
                print(f'Got an error: \'{err}\'')

    def __radd__(self, other):
        return self.__add__(other)


# Demoing AutoDiffToy...
a = 2.0                                    # Value to evaluate at
x = AutoDiffToy(a)
alpha = 2.0                                # Slope
beta = 3.0                                 # Y-intercept

f = alpha * x + beta
print(f.val, f.der)
f = x * alpha + beta
print(f.val, f.der)
f = beta + alpha * x
print(f.val, f.der)
f = beta + x * alpha
print(f.val, f.der)
