#!/usr/bin/env python3

# Coder: Gerald Arocena & Martha Obasi
# Sharer: Martha Obasi

# PP5

import numpy as np


class Layer:

    def __init__(self, shape, actv):
        self.weights = np.random.normal(0.0, 1.0, shape[0]*shape[1]).reshape(shape[0], shape[1])
        self.biases = np.random.normal(0.0, 1.0, shape[1])
        self.actv = actv
        self.shape = shape

    def forward(self, inputs):
        return self.actv(np.dot(inputs, self.weights) + self.biases)

    def __repr__(self):
        return "Layer({!r}, actv_fxn)".format(self.shape)

    def __str__(self):
        return "This class returns a layer for a neural network."

    def __eq__(self, other):
        return (self.shape[0] == other.shape[0]) and (self.shape[1] == other.shape[1])


inputs = np.random.normal(0.0, 1.0, 100).reshape(1, -1)  # input to the network

shape1 = [100, 16]
shape2 = [16, 1]
shape3 = [100, 16]

layer1 = Layer(shape1, np.tanh)  # define layer 1
layer2 = Layer(shape2, np.tanh)  # define layer 2
layer3 = Layer(shape3, np.tanh)

h1 = layer1.forward(inputs)
print("h1:", h1)
h2 = layer2.forward(h1)
print("h2:", h2)

print(layer1)
print(layer1 == layer2)
print(layer1 == layer3)
