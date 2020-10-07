#!/usr/bin/env python3

class Regression:
    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        # TODO: Manually set parameters of the linear model
        raise NotImplementedError

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def score(self, X, y):
        raise NotImplementedError


a_test = Regression()
try:
    a_test.fit(5, 3)
