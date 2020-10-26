#!/usr/bin/env python3

# Sharer: Haoxin Li
# Coder: Thee Ngamsangrat
# Listener: Gerald Arocena

import numpy as np


def make_layer(shape, actv):
    def layer(inputs, weights, bias):
        return actv(np.dot(inputs, weights) + bias)
    return layer


def sigmoid(x):
    return 1/(1 + np.exp(-x))


t = np.random.uniform(0.0, 1.0, 100).reshape(1, -1)  # input to the network

shape1 = (100, 16)  # Define the shape of w1, (100, 16)
shape2 = (16, 1)  # Define the shape of w1, (16, 1), the output shape is 1 with tanh

layer1 = make_layer(shape1, np.tanh)  # Define layer 1
layer2 = make_layer(shape2, np.tanh)  # Define layer 2

# Initialize weights and biases
w1 = np.random.normal(0.0, 1.0, shape1)  # Define w1 with N(0, 1), shape (100, 16)
w2 = np.random.normal(0.0, 1.0, shape2)  # Define w2 with N(0, 1), shape (16, 1)
b1 = np.random.normal(0.0, 1.0, shape1[1])  # Define b1 with N(0, 1), shape (16, )
b2 = np.random.normal(0.0, 1.0, shape2[1])  # Define b1 with N(0, 1), shape (1, )

# Run through the network
h1 = layer1(t, w1, b1)  # First layer, the shape is (1,16)
h2 = layer2(h1, w2, b2)  # Last layer, the shape is (1, 1)

print('h1 is: ')
print(h1)
print('The shape of h1 is:', h1.shape)

print('h2 is: ')
print(h2)
print('The shape of h2 is:', h1.shape)
