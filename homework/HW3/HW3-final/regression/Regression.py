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
        ones_col = np.ones(shape=X.shape[0]).reshape(-1, 1)
        X = np.append(ones_col, X, axis=1)
        beta_hat = np.linalg.pinv(X.transpose().dot(X)).dot(X.transpose()).dot(y)
        # TODO: Debugging
        print(beta_hat, '\n')
        # Intercept can be thought of as beta_0
        self.params['intercept'] = beta_hat[0]
        # TODO: Debugging
        print(self.params['intercept'], '\n')
        self.params['coeffs'] = beta_hat[1:]
        # TODO: Debugging
        print(self.params['coeffs'])

    # TODO
    def predict(self, X):
        raise NotImplementedError('Method not implemented yet')

    # TODO
    def score(self, X, y):
        raise NotImplementedError('Method not implemented yet')


# TODO: Debugging
X = np.array([[0, 1, 2, 3], [1, 5, 3, 7], [1, 7, 3, 8], [9, 2, 4, 8], [5, 9, 1, 3]])
y = np.array([[3],[7],[1],[6],[9]])
regr = LinearRegression()
regr.fit(X, y)

# References:
# - https://towardsdatascience.com/multiple-linear-regression-from-scratch-in-numpy-36a3e8ac8014
