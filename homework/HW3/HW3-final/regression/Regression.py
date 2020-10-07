#!/usr/bin/env python3

class Regression:
    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        raise NotImplementedError("Method not implemented yet")

    def fit(self, X, y):
        raise NotImplementedError("Method not implemented yet")

    def predict(self, X):
        raise NotImplementedError("Method not implemented yet")

    def score(self, X, y):
        raise NotImplementedError("Method not implemented yet")

    def hello_world(self):
        print("Hello World")

# TODO: Factor out common code back into base class when finished derived classes
