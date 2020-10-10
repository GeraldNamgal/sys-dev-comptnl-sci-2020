#!/usr/bin/env python3

from sklearn import datasets  # TODO: Goes in other file
from sklearn.model_selection import train_test_split  # TODO: Goes in other file
import numpy as np


class Regression:
    def __init__(self, alpha):
        self.params = {'alpha': alpha}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.params:
                self.params[key] = value

    def fit(self, X, y):
        raise NotImplementedError('Method not implemented')

    def predict(self, X):
        predictions = []
        for row in X:
            prediction = self.params['intercept']
            for element, coeff in zip(row, self.params['coeffs']):
                prediction += (element * coeff)
            predictions.append(prediction)
        return predictions                    # Return array of predictions

    # TODO
    def score(self, X, y):
        # TODO: Get predictions
        y_bar = np.mean(y)                    # Get mean of original data values
        ss_t = 0                              # Get SS_t...
        for y_value in y:
            ss_t += (y_value - y_bar) ** 2
        ss_e = 0                              # Get SS_e...
        for y_value, row in zip(y, X):
            ss_e += (y_value - self.predict(row)) ** 2
        return 1 - (ss_e / ss_t)              # Return R-squared


class LinearRegression(Regression):
    def fit(self, X, y):
        ones_col = np.ones(shape=X.shape[0]).reshape(-1, 1)
        X = np.append(ones_col, X, axis=1)       # Append column of ones to X
        # Ordinary Least Squares best fit coefficients equation aka 'beta_hat':
        beta_hat = np.linalg.pinv(X.transpose().dot(X)).dot(X.transpose()).dot(y)
        self.params['coeffs'] = beta_hat[1:]     # Non-first rows of matrix
        self.params['intercept'] = beta_hat[0]   # Intercept is also 'beta_0'


class RidgeRegression(Regression):
    def fit(self, X, y):
        ones_col = np.ones(shape=X.shape[0]).reshape(-1, 1)
        X = np.append(ones_col, X, axis=1)       # Append column of ones to X
        gamma = np.identity(X.shape[1]).dot(self.params['alpha'])
        tmp_matrix = np.add(X.transpose().dot(X), gamma.transpose().dot(gamma))
        # Ridge Regression best fit coefficients equation aka 'beta_hat':
        beta_hat = np.linalg.pinv(tmp_matrix).dot(X.transpose()).dot(y)
        self.params['coeffs'] = beta_hat[1:]     # Non-first rows of matrix
        self.params['intercept'] = beta_hat[0]   # Intercept is also 'beta_0'


# TODO: Goes in other file when finished
# Get Boston data
dataset = datasets.load_boston()

# Train-test split the data
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

# Score the models
alpha = 0.1
models = [LinearRegression(alpha)]
for model in models:
    model.fit(X_train, y_train)


# References:
# - https://towardsdatascience.com/multiple-linear-regression-from-scratch-in-numpy-36a3e8ac8014
