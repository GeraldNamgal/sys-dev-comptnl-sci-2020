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
    # TODO
    def set_params(self, **kwargs):
        raise NotImplementedError('Method not implemented yet')

    # TODO
    def fit(self, X, y):
        # TODO: Need to reshape if one feature matrix or not?
        if len(X.shape) == 1:
            X = X.reshape(-1, 1)

        ones_col = np.ones(shape=X.shape[0]).reshape(-1, 1)
        X = np.append(ones_col, X, axis=1)
        self.params['coeffs'] = X.transpose().dot(X) # TODO: Finish this equation

    # TODO
    def predict(self, X):
        raise NotImplementedError('Method not implemented yet')

    # TODO
    def score(self, X, y):
        raise NotImplementedError('Method not implemented yet')


# References:
# - https://towardsdatascience.com/multiple-linear-regression-from-scratch-in-numpy-36a3e8ac8014
