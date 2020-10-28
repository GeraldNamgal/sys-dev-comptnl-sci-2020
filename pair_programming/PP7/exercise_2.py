#!/usr/bin/env python3

# Sharer, Listener, Coder: Nishu Lahoti, Bianca Cordazzo, Gerald Arocena

# Exercise 2

def my_pow(r):
    def inner(eval_point, seed_value=1):
        return r * (eval_point ** (r-1)) * seed_value
    return inner


# Demoing my_pow --
if __name__ == "__main__":
    x, r = 3, 4
    example = my_pow(r)
    print(example(x))                      # Should be 108
