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
        if node.key == key:
            node.val = val
        elif node.key > key:
            if node.left is None:        # Adding a new node?
                node.size += 1           # Increase node count
            node.left = self._put(node.left, key, val)
        else:
            if node.right is None:       # Adding a new node?
                node.size += 1           # Increase node count
            node.right = self._put(node.right, key, val)
        return node

    # TODO: Check that updating size of nodes is working right
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


# TODO: Debugging...
greektoroman = BSTTable()
greektoroman.put('Athena',    'Minerva')
greektoroman.put('Eros',      'Cupid')
greektoroman.put('Aphrodite', 'Venus')
print(greektoroman.get('Eros'))
print()
print(greektoroman)
# Test that value gets replaced (i.e., instead of added) --
greektoroman.put('Aphrodite', 'Dumbledore')
print()
print(greektoroman)

# tree = BSTTable()
# list = [13,7,19,17,3,29,5,31,2,11]
# # list = [7,19,17,3,29,5,31,2,11]
# # list = [13,7,19,17,3,5,31,2,11]
# # list = [13,7,19,17,3,29,5,2,11]
# for num in list:
#     tree.put(num, num)
# print(tree)
