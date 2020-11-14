#!/usr/bin/env python3

class BSTNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    # TODO: Remove size printing when submit
    def __str__(self):
        return f'BSTNode({self.key}, {self.val}) [SIZE={self.size}]' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None
        self._removednode = False

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node:
            return BSTNode(key, val)
        if key < node.key:
            node.left = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0

    # TODO: Check that this works with other trees like one in notebook?
    def _removemin(self, node):
        if not node:
            return node
        elif not node.left:             # At the min node?
            if node.right:              # Has a right child?
                node = node.right         # TODO: Switch this with node = None stuff?
                # tmp_node = node.right   # TODO: This node = None stuff necessary?
                # node = None
                # return tmp_node
            else:                       # No children?
                node = None
                # return None             # TODO: Need return (see above)?
        else:
            node.left = self._removemin(node.left)
            node.size -= 1                # TODO: Double-check that size is updating correctly
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)
        if self._removednode:           # Reset _removednode?
            self._removednode = False

    # TODO
    def _remove(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if key < node.key:
            node.left = self._remove(node.left, key)
            if self._removednode:
                node.size -= 1
        elif key > node.key:
            node.right = self._remove(node.right, key)
            if self._removednode:
                node.size -= 1
        else:                           # Found node to remove
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:   # TODO: Test this out (Check that size is updating correctly, etc.)
                min_node = self._getmin(node.right)     # Min from right child
                node.key = min_node.key
                node.val = min_node.val
                node.size -= 1
                node.right = self._removemin(node.right)
            self._removednode = True
        return node

    def _getmin(self, node):
        if not node:
            return node
        elif not node.left:             # At the min node?
            return node
        else:
            return self._getmin(node.left)


# TODO: Debugging...
# # Part A
# t = BSTTable()
# t.put(5, 'a')
# t.put(1, 'b')
# t.put(2, 'c')
# t.put(0, 'd')
# print(t._root)
# print()
# print(t._removemin(t._root))
# t.put(0, 'd')
# t.put(0.5, '?')
# print()
# print(t._root)
# print()
# print(t._removemin(t._root))
# Part B
t = BSTTable()
t.put(5, 'a')
t.put(1, 'b')
t.put(2, 'c')
t.put(0, 'd')
print(t._root)
print()
print(t._remove(t._root, 5))
print()
print(t._remove(t._remove(t._root, 5), 1))
# print(t._remove(t._root, 10))   # Should return an error
