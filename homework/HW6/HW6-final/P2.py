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

    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        idx_of_extreme = idx                    # Set parent as extreme for now

        left_idx = self.left(idx)               # Left child idx
        if left_idx < self.size:                # Indexable / in bounds?
            if self.compare(left_idx, idx_of_extreme):      # Change extreme?
                idx_of_extreme = left_idx

        right_idx = self.right(idx)             # Right child idx
        if right_idx < self.size:               # Indexable / in bounds?
            if self.compare(right_idx, idx_of_extreme):     # Change extreme?
                idx_of_extreme = right_idx

        if idx_of_extreme != idx:               # Extreme changed from parent?
            self.swap(idx, idx_of_extreme)      # Swap node and parent
            self.heapify(idx_of_extreme)        # Recurse on parent at new idx

    def build_heap(self) -> None:
        idx = self.parent(self.size - 1)        # Start at last subtree
        while True:
            if idx < 0:                         # Don't index past first element
                break
            else:
                self.heapify(idx)               # Heapify
                idx -= 1                        # Preceding subtree next

    def heappush(self, key: int) -> None:
        self.elements.append(key)
        self.size += 1
        tmp_idx = self.size - 1                 # Bubble up appended element?...
        while self.parent(tmp_idx) >= 0\
                and self.compare(tmp_idx, self.parent(tmp_idx)):
            self.swap(tmp_idx, self.parent(tmp_idx))
            tmp_idx = self.parent(tmp_idx)

    def heappop(self) -> int:
        try:
            if self.size <= 0:
                raise IndexError('Heap is empty')
        except Exception:
            raise

        root = self.elements[0]                 # Save root
        self.swap(0, self.size - 1)             # Swap root with last element
        del self.elements[self.size - 1]        # Delete last element
        self.size -= 1

        if self.size > 0:                       # Are there still nodes?
            self.heapify(0)                     # Heapify root node

        return root                             # Return original root


class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if self.elements[a] < self.elements[b]:
            return True
        return False


class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        if self.elements[a] > self.elements[b]:
            return True
        return False


# TODO: Debugging
# # Part A     # TODO: Maybe follow up with Piazza post https://piazza.com/class/kc57xuuysdm64b?cid=501
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

# # Part C
# mn = MinHeap([1, 2, 3, 4, 5])
# print(mn)
# mn.heappush(-1)
# mn.heappush(6)
# print(mn)
# print(mn.heappop())
# print(mn.heappop())
# print(mn.heappop())
# print(mn.heappop())
# print(mn.heappop())
# print(mn)
# print(mn.heappop())
# print(mn)
# print(mn.heappop())
# print(mn)
# print(f'size is now {mn.size}')
# # print(mn.heappop())    # Should throw an empty error

# mx = MaxHeap([1, 2, 3, 4, 5])
# print(mx)
# mx.heappush(-1)
# mx.heappush(6)
# print(mx)
# print(mx.heappop())
# print(mx.heappop())
# print(mx.heappop())
# print(mx.heappop())
# print(mx.heappop())
# print(mx)
# print(mx.heappop())
# print(mx)
# print(mx.heappop())
# print(mx)
# print(f'size is now {mx.size}')
# # print(mx.heappop())      # Should throw an empty error
