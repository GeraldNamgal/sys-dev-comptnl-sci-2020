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

    # TODO: Can check if this is working correctly per Piazza post (https://piazza.com/class/kc57xuuysdm64b?cid=388)
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
            return LinkedList(self._head, LinkedList(val, Nil()))

    # TODO: When do we return Nil (HW instructions Part B)? - Think in Nil()'s for_each?
    def for_each(self, fun):
        if self._tail:
            return LinkedList(fun(self._head), self._tail.for_each(fun))
        else:
            # TODO: How do we handle Nil() exactly? - Is this where we return it?
            return LinkedList(fun(self._head), Nil().for_each(fun))

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

    # TODO: Is prepend the same as append (looks like it should be)?
    def prepend(self, val):
        return LinkedList(val, Nil())

    def append(self, val):
        return LinkedList(val, Nil())

    # TODO: What exactly is this supposed to do (looks about right)?
    def for_each(self, fun):
        return Nil()


# TODO: Debugging... (erase / comment out later, i.e, no demo needed?)
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
# # PART B demo + append demo
# l = Nil().prepend(1).prepend(2).prepend(3).prepend(4)
# def square(x):
#     return x**2
# print(l)
# print(l.for_each(square))
# l = Nil().append(1).append(2).append(3).append(4)
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
# l = Nil().prepend(12)                # One-element linked list
# print(l.reduce_right(smaller))
