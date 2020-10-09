#!/usr/bin/env python3

from sklearn import datasets  # TODO: Goes in other file
from sklearn.model_selection import train_test_split  # TODO: Goes in other file
import numpy as np
import pandas as pd  # TODO: Delete later
import warnings  # TODO: Delete later
warnings.filterwarnings('ignore')  # TODO: Delete later


class Regression:
    def __init__(self, alpha):
        self.params = {}
        self.alpha = alpha

    def get_params(self):
        return self.params

    # TODO: Done, just need to check that it works
    def set_params(self, **kwargs):
        for key, value in kwargs:
            if key in self.params:
                self.params[key] = value

    def fit(self, X, y):
        raise NotImplementedError('Method not implemented')

    def predict(self, X):  # TODO: Change X to 'X_row' or 'row' or something?
        prediction = self.params['intercept']
        for x, coeff in zip(X, self.params['coeffs']):
            prediction += (x * coeff)
        return prediction

    # TODO
    def score(self, X, y):
        ss_e = 0
        ss_t = 0
        r_squared = 1 - (ss_e / ss_t)
        return r_squared

# TODO: Factor out common code back into base class when finished derived classes


class LinearRegression(Regression):
    # TODO
    def fit(self, X, y):
        ones_col = np.ones(shape=X.shape[0]).reshape(-1, 1)
        X = np.append(ones_col, X, axis=1)       # Append column of ones to X
        # Ordinary Least Squares best fit coefficients equation aka 'beta_hat':
        beta_hat = np.linalg.pinv(X.transpose().dot(X)).dot(X.transpose()).dot(y)
        self.params['coeffs'] = beta_hat[1:]     # Non-first rows of matrix
        self.params['intercept'] = beta_hat[0]   # Intercept is also 'beta_0'


class RidgeRegression(Regression):
    # TODO
    def fit(self, X, y):
        ones_col = np.ones(shape=X.shape[0]).reshape(-1, 1)
        X = np.append(ones_col, X, axis=1)       # Append column of ones to X
        gamma = np.identity(X.shape[1]).dot(self.alpha)
        tmp_matrix = np.add(X.transpose().dot(X), gamma.transpose().dot(gamma))
        # Ridge Regression best fit coefficients equation aka 'beta_hat':
        beta_hat = np.linalg.pinv(tmp_matrix).dot(X.transpose()).dot(y)
        self.params['coeffs'] = beta_hat[1:]     # Non-first rows of matrix
        self.params['intercept'] = beta_hat[0]   # Intercept is also 'beta_0'


# TODO: Debugging
# Get Boston data using pandas
boston = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')
print(boston.head(), '\n')
X = boston.drop('medv', axis=1).values
y = boston['medv'].values
print(X, '\n')
print(y, '\n')

# Get Boston data using hw instructions
dataset = datasets.load_boston()
print(dataset['data'], '\n')
print(dataset['target'], '\n')

X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

# Demo (from tutorial)
model = LinearRegression(0.5)  # 0.5 is from hw
model.fit(X, y)
print(model.get_params()['intercept'])
print(model.get_params()['coeffs'])
print(model.predict(X[0]))  # First row's predicted value (actual is first row's y value)

# Demo (from hw)
alpha = 0.5
models = [LinearRegression(alpha)]
for model in models:
    model.fit(X_train, y_train)


# References:
# - https://towardsdatascience.com/multiple-linear-regression-from-scratch-in-numpy-36a3e8ac8014
