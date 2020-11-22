#!/usr/bin/env python3

from random import sample
from time import time
from P2 import *


class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError  # TODO

    def get(self):
        raise NotImplementedError  # TODO

    def peek(self):
        raise NotImplementedError  # TODO


def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))

    return merged


def generatelists(n, length=20, dictionary_path='../data/words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed


class NaivePriorityQueue(PriorityQueue):
    def put(self, val):
        try:
            if len(self.elements) >= self.max_size:
                raise IndexError('Priority queue is full')
            self.elements.append(val)
        except Exception:
            raise

    def get(self):
        try:
            if not self.elements:
                raise IndexError('Priority queue is empty')
            # TODO: Are we allowed to use min() and remove()?
            min_val = min(self.elements)
            self.elements.remove(min_val)
            return min_val
        except Exception:
            raise

    def peek(self):
        try:
            if not self.elements:
                raise IndexError('Priority queue is empty')
            # TODO: Are we allowed to use min()?
            return min(self.elements)
        except Exception:
            raise


class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.elements = MinHeap([])

    def put(self, val):
        try:
            if len(self.elements) >= self.max_size:
                raise IndexError('Priority queue is full')
            self.elements.heappush(val)
        except Exception:
            raise

    def get(self):
        try:
            if not self.elements:
                raise IndexError('Priority queue is empty')
            return self.elements.heappop()
        except Exception:
            raise

    def peek(self):
        try:
            if not self.elements:
                raise IndexError('Priority queue is empty')
            root = self.elements.heappop()
            self.elements.heappush(root)
            return root
        except Exception:
            raise


# TODO: Debugging
# # Part A
# q = NaivePriorityQueue(2)
# q.put(1)
# q.put(2)
# print(q.peek())
# print(q.get())
# print(q.get())
# # print(q.get())  # Should raise an error
# Part B
q = HeapPriorityQueue(2)
q.put(1)
q.put(2)
print(q.peek())
print(q.get())
print(q.get())
# print(q.get())  # Should raise an error
