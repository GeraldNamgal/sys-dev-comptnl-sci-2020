#!/usr/bin/env python3

class LinkedList:

    def __init__(self, head, tail):
        assert isinstance(tail, LinkedList) or isinstance(tail, Nil), TypeError(
            'tail should either be a LinkedList or a Nil')
        self._head, self._tail = head, tail

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __str__(self):
        return str(self._head) + ' -> ' + str(self._tail)

    def __repr__(self):
        return f'LinkedList({repr(self._head)}, {repr(self._tail)})'

    def __len__(self):
        return 1 + len(self._tail)

    def __getitem__(self, i):
        return self._head if i == 0 else self._tail[i-1]

    def prepend(self, val):
        return LinkedList(val, self)

    def append(self, val):
        if self._tail:                # Recurse (tail is a LinkedList)
            return LinkedList(self._head, self._tail.append(val))
        else:                         # Base case (tail is a Nil)
            return LinkedList(self._head, LinkedList(val, self._tail))

    def for_each(self, fun):
        return LinkedList(fun(self._head), self._tail.for_each(fun))

    def summation(self):
        return self._head + self._tail.summation() if self._tail else self._head

    def minimum(self):
        def smaller(a, b):
            return a if a < b else b
        return smaller(self._head, self._tail.minimum()) if self._tail else self._head

    def reduce_right(self, fun):
        if self._tail:
            return fun(self._head, self._tail.reduce_right(fun))
        else:
            return self._head


class Nil():

    def __str__(self):
        return 'Nil'

    def __repr__(self):
        return 'Nil()'

    def __len__(self):
        return 0

    def __getitem__(self, i):
        raise IndexError('index out of range')

    def __bool__(self):
        return False

    def prepend(self, val):
        return LinkedList(val, self)

    def append(self, val):
        return LinkedList(val, Nil())

    def for_each(self, fun):
        return self


# TODO: Debugging...
# # Create a linked list
# llist = Nil().append(6)
#
# # APPEND demo
# llist = llist.append(7)
# llist = llist.append(8)
# # Print elements
# print(llist)
#
# # PREPEND demo
# llist = llist.prepend(7)
# llist = llist.prepend(8)
# # Print elements
# print(llist)
#
# PART B demo + append demo
# l = Nil().prepend(1).prepend(2).prepend(3).prepend(4)
# print(f'\n{type(l)}, {l.head}, {type(l.tail)}; {l.tail}, {len(l.tail)}\n')
# def square(x):
#     return x**2
# print(l)
# print(l.for_each(square))
# l = Nil().append(1).append(2).append(3).append(4)
# print(f'\n{type(l)}, {l.head}, {type(l.tail)}; {l.tail}, {len(l.tail)}\n')
# print(l)
# print(l.for_each(square))
#
# # PART C demo
# l = Nil().prepend(1).prepend(2).prepend(3).prepend(4)
# def smaller(a, b): # our "combine" function
#     return a if a < b else b
# print(l)
# print(l.reduce_right(smaller))
# def bigger(a, b): # our "combine" function
#     return a if a > b else b
# print(l.reduce_right(bigger))
#
# # Testing getitem
# print(l[1])                      # Should be 3
#
# l = Nil().prepend(12)            # One-element linked list
# print(l.reduce_right(smaller))   # Should be 12
