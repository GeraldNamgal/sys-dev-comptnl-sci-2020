#!/usr/bin/env python3

import numpy as np
import pandas as pd  # TODO: Delete later
import warnings  # TODO: Delete later
warnings.filterwarnings('ignore')  # TODO: Delete later
from sklearn import datasets  # TODO: Goes in other file
from sklearn.model_selection import train_test_split  # TODO: Goes in other file


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
    # TODO: Belongs in OLS or just Ridge?
    def set_params(self, **kwargs):
        raise NotImplementedError('Method not implemented yet')

    # TODO
    def fit(self, X, y):
        ones_col = np.ones(shape=X.shape[0]).reshape(-1, 1)
        X = np.append(ones_col, X, axis=1)       # Append column of ones to X
        # Ordinary Least Squares best fit coefficients equation aka 'beta_hat':
        beta_hat = np.linalg.pinv(X.transpose().dot(X)).dot(X.transpose()).dot(y)
        self.params['coeffs'] = beta_hat[1:]     # Non-first rows of matrix
        self.params['intercept'] = beta_hat[0]   # Intercept is also 'beta_0'

    # TODO
    def predict(self, X):
        prediction = self.params['intercept']
        for xi, bi in zip(X, self.params['coeffs']):
            prediction += (bi * xi)
        return prediction

    # TODO
    def score(self, X, y):
        raise NotImplementedError('Method not implemented yet')


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


# References:
# - https://towardsdatascience.com/multiple-linear-regression-from-scratch-in-numpy-36a3e8ac8014
