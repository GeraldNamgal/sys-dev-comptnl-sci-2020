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

    # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        idx_of_min = idx                     # Set parent as min for now
        left_idx = self.left(idx)
        right_idx = self.right(idx)

        # TODO: Debugging (remove later)
        # print(self)

        if left_idx < self.size:             # Indexable / in bounds?
            if self.compare(left_idx, idx_of_min):      # New min?
                idx_of_min = left_idx
        if right_idx < self.size:            # Indexable / in bounds?
            if self.compare(right_idx, idx_of_min):     # New min?
                idx_of_min = right_idx
        if idx_of_min != idx:                # Was a new min set?
            self.swap(idx, idx_of_min)       # Swap node and parent
            self.heapify(idx_of_min)         # Recurse on parent at new idx

    def build_heap(self) -> None:
        idx = self.parent(self.size - 1)     # Start at last subtree
        while True:
            if idx < 0:
                break
            else:
                self.heapify(idx)
                idx -= 1                     # Preceding subtree

    def heappush(self, key: int) -> None:
        self.elements.append(key)
        self.size += 1
        tmp_idx = self.size - 1              # Bubble up appended element...
        while self.parent(tmp_idx) >= 0:
            if self.compare(tmp_idx, self.parent(tmp_idx)):
                self.swap(tmp_idx, self.parent(tmp_idx))
                tmp_idx = self.parent(tmp_idx)

    # Referenced https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
    def heappop(self) -> int:
        root = self.elements[0]
        self.swap(0, self.size - 1)
        del self.elements[-1]
        self.size -= 1
        # # TODO: Debugging (remove later)
        # print(f'Root is now: {self.elements[0]}')
        self.heapify(0)
        return root


class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if (self.elements[a] < self.elements[b]):
            return True
        return False


class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if (self.elements[a] > self.elements[b]):
            return True
        return False


# TODO: Debugging
# # Part A
# h = Heap([-1, 0, 0, 15, 23, 1, 2, 3])  # The heap tree will be built during initialization
# print(h)
# g = Heap([5, 8, 1, 0, 10, -2, -4, 21])
# print(g)
# # Part B
# g.heappush(6)
# print(g)
# g.heappush(-1)
# print(g)
# print(f'Removed/popped root: {g.heappop()}')
# print()
# print(g)
# Part C
mn = MinHeap([1, 2, 3, 4, 5])
mx = MaxHeap([1, 2, 3, 4, 5])
print(mn)
# print(mx)
mn.heappush(-1)
print(mn)
