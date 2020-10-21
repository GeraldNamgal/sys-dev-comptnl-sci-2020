# Sharer, Listener, Coder: Nishu Lahoti, Bianca Cordazzo, Gerald Arocena

# Exercise 2

import numpy as np

x = 3
r = 4

def my_pow(r):
    def inner(f, seed_value=1): 
        return r*(x**(r-1))*seed_value
    return inner

if __name__ == "__main__":
    example = my_pow(r)
    example(x**r)
    print(example(x**r))