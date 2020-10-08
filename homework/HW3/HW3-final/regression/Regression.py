#!/usr/bin/env python3

import numpy as np

class Regression:
    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        raise NotImplementedError('Method not implemented yet')

    def fit(self, X, y):
        raise NotImplementedError('Method not implemented yet')

    def predict(self, X):
        raise NotImplementedError('Method not implemented yet')

    def score(self, X, y):
        raise NotImplementedError('Method not implemented yet')

# TODO: Factor out common code back into base class when finished derived classes


class LinearRegression(Regression):
    def set_params(self, **kwargs):
        # TODO
        raise NotImplementedError('Method not implemented yet')

    def fit(self, X, y):
        # TODO
        raise NotImplementedError('Method not implemented yet')

    def predict(self, X):
        # TODO
        raise NotImplementedError('Method not implemented yet')

    def score(self, X, y):
        # TODO
        raise NotImplementedError('Method not implemented yet')


arr = np.array([[0, 1, 2, 3], [1, 5, 3, 7], [1, 7, 3, 8], [9, 2, 4, 8], [5, 9, 1, 3]])
print(arr)
print()
ones_col = np.ones(shape=arr.shape[0]).reshape(-1, 1)
print(ones_col)
print()
catted = np.concatenate((ones_col, arr), 1)
print(catted)
print()
appended = np.append(ones_col, arr, axis=1)
print(appended)

# References:
# - https://towardsdatascience.com/multiple-linear-regression-from-scratch-in-numpy-36a3e8ac8014
