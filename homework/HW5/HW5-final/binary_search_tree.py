#!/usr/bin/env python3

class BSTNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if node is None:
            return BSTNode(key, val)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        else:
            node.right = self._put(node.right, key, val)
        node.size += 1
        return node

    def _get(self, node, key):
        if node is None:
            raise KeyError
        if key == node.key:
            return node.val
        if key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    @staticmethod
    def _size(node):
        return node.size if node else 0


# # TODO: Debugging... (erase / comment out later, i.e., no demo needed?)
# greektoroman = BSTTable()
# greektoroman.put(13, 'M')
# greektoroman.put(1, 'A')
# greektoroman.put(26, 'Z')
# greektoroman.put(2, 'B')
# greektoroman.put(25, 'Y')
# greektoroman.put(3, 'C')
# greektoroman.put(24, 'X')
#
# print(f'Getting 1: ')
# print(greektoroman.get(1))
# print(f'Getting 2: ')
# print(greektoroman.get(2))
# print(f'Getting 3: ')
# print(greektoroman.get(3))
# print(f'Getting 26: ')
# print(greektoroman.get(26))
# print(greektoroman)
