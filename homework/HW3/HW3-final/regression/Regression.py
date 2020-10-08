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
        # TODO: Need to reshape if one feature matrix or not? -- Peniel said don't need to
        # Peniel also said you could print out y and X to see if need to but said after
        # that no reshaping is necessary

        if len(X.shape) == 1:
            X = X.reshape(-1, 1)

        [[1, 2, 3]]
        -->
        [[1],  # *** Do we have to reshape / What does this mean?
         [2],
         [3]]

        ones_col = np.ones(shape=X.shape[0]).reshape(-1, 1)
        X = np.append(ones_col, X, axis=1)

        [[1 4],
         [2 5],
         [3 6]]
        -->
        [[1 1 4],  # *** Ones in first column ok?
         [1 2 5],
         [1 3 6]]

        self.params['beta_0'] =\ # <-- Peniel said this is the intercept
            np.linalg.pinv(X.transpose().dot(X)).dot()[0] # TODO: Finish this equation

    self.params['coeffs'] = beta[1:]
        # *** What is intercept? The ones column? <-- Peniel said first row is (use index)

    # TODO
    def predict(self, X):
        raise NotImplementedError('Method not implemented yet')

    # TODO
    def score(self, X, y):
        raise NotImplementedError('Method not implemented yet')


# References:
# - https://towardsdatascience.com/multiple-linear-regression-from-scratch-in-numpy-36a3e8ac8014
