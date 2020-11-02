#!/usr/bin/env python3

# Sharer/Listener/Coder: Gerald Arocena, Timothy Williamson, Aditya Kumar

class Fibonacci:
    def __init__(self, num_elm):
        self.num_elm = num_elm

    def __iter__(self):
        return FibonacciIterator(self.num_elm)


class FibonacciIterator:
    def __init__(self, num_elm):
        self.f1 = 0
        self.f2 = 1
        self.index = 0
        self.num = 0
        self.num_elm = num_elm

    def __next__(self):
        if self.index >= self.num_elm:
            raise StopIteration()
        self.index += 1
        f3 = self.f1 + self.f2
        self.f1 = self.f2
        self.f2 = f3
        return f3

    def __iter__(self):
        return self


# Demo
example = Fibonacci(5)
print(list(iter(example)))
