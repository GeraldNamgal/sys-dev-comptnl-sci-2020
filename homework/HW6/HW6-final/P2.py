#!/usr/bin/env python3

from math import floor
from typing import List


class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array)  # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            # buf = buf + str(self.elements[idx]) + '\n' # use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                self.to_string(new_prefix, self.left(idx), True) + \
                self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> str:
        return self.size

    def heapify(self, idx: int) -> None:
        idx_of_min = idx                     # Set parent as min for now
        left_idx = self.left(idx)
        right_idx = self.right(idx)

        # TODO: Debugging (remove later)
        # print(self)

        if left_idx < self.size:             # Is indexable/inbounds?
            if self.elements[left_idx] < self.elements[idx_of_min]:   # New min?
                idx_of_min = left_idx
        if right_idx < self.size:            # Is indexable/inbounds?
            if self.elements[right_idx] < self.elements[idx_of_min]:  # New min?
                idx_of_min = right_idx
        if idx_of_min != idx:                # Was a new min set?
            self.swap(idx, idx_of_min)       # Swap nodes
            self.heapify(idx_of_min)         # Recurse on new min

    def build_heap(self) -> None:
        idx = self.parent(self.size - 1)     # Start at last subtree
        while True:
            if idx < 0:
                break
            else:
                self.heapify(idx)
                idx -= 1                     # Preceding subtree


# TODO: Debugging
# Part A
h = Heap([-1, 0, 0, 15, 23, 1, 2, 3])  # The heap tree will be built during initialization
print(h)
g = Heap([5, 8, 1, 0, 10, -2, -4, 21])
print(g)
