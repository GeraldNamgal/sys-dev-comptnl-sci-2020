#!/usr/bin/env python3

from enum import Enum


class BSTNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    # TODO: Remove size printing when submit including space before bracket
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


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


# Referenced https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.nodes = []
        self.index = 0
        self.num_nodes = len(tree)

        if traversalType is DFSTraversalTypes.INORDER:
            self.inorder(tree)
        elif traversalType is DFSTraversalTypes.PREORDER:
            self.preorder(tree)
        elif traversalType is DFSTraversalTypes.POSTORDER:
            self.postorder(tree)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.num_nodes:
            raise StopIteration()
        node = self.nodes[self.index]
        self.index += 1
        return node

    def inorder(self, bst: BSTTable):
        self._inorder(bst._root)
        return

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            self.nodes.append(node)
            self._inorder(node.right)

    def preorder(self, bst: BSTTable):
        self._preorder(bst._root)
        return

    def _preorder(self, node):
        if node:
            self.nodes.append(node)
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self, bst: BSTTable):
        self._postorder(bst._root)
        return

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            self.nodes.append(node)


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
# t.put(0, 'q')
# t.put(0.5, '?')
# print()
# print(t._root)
# print()
# print(t)
# print()
# print(t._removemin(t._root))

# # Part B
# t = BSTTable()
# t.put(5, 'a')
# t.put(1, 'b')
# t.put(2, 'c')
# t.put(0, 'd')
# print(t._root)
# print()
# print(t._remove(t._root, 5))
# print()
# print(t._remove(t._remove(t._root, 5), 1))
# # print(t._remove(t._root, 10))   # Should return an error

# # Piazza: This demo _remove`s two nodes from the root, thus not changing the original tree
# print('This demo _remove`s two nodes from the root, thus not changing the original tree\n')
# t = BSTTable()
# t.put(5, 'a')
# t.put(1, 'b')
# t.put(2, 'c')
# t.put(0, 'd')
# print(t)
# print()
# print(t._remove(t._root, 5))
# print()
# print(t._remove(t._root, 1))
# print()
#
# # Piazza: This demo _remove`s two non-root nodes, thus changing the original tree
# print('This demo _remove`s two non-root nodes, thus changing the original tree\n')
# t2 = BSTTable()
# t2.put(5, 'a')
# t2.put(1, 'b')
# t2.put(2, 'c')
# t2.put(0, 'd')
# print(t2)
# print()
# print(t2._remove(t2._root, 2))
# print()
# print(t2._remove(t2._root, 1))

# # REGULAR remove testing
# t = BSTTable()
# t.put(5, 'a')
# t.put(1, 'b')
# t.put(2, 'c')
# t.put(0, 'd')
# print(t)
# print()
# t.remove(1)
# print(t)
# print()
# t.remove(2)
# print(t)
# print()

# # Part C
# input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
# bst = BSTTable()
# for key, val in input_array:
#     bst.put(key, val)
# # print(bst)
# traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
# for node in traversal:
#     print(str(node.key) + ', ' + node.val)
# print()
# traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
# check = iter(traversal)
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# # print(str(next(check).key))      # Should throw an error
# print()
# traversal = DFSTraversal(bst, DFSTraversalTypes.PREORDER)
# for node in traversal:
#     print(str(node.key) + ', ' + node.val)
# print()
# traversal = DFSTraversal(bst, DFSTraversalTypes.PREORDER)
# check = iter(traversal)
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# # print(str(next(check).key))      # Should throw an error
# print()
# traversal = DFSTraversal(bst, DFSTraversalTypes.POSTORDER)
# for node in traversal:
#     print(str(node.key) + ', ' + node.val)
# print()
# traversal = DFSTraversal(bst, DFSTraversalTypes.POSTORDER)
# check = iter(traversal)
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# print(str(next(check).key))
# # print(str(next(check).key))      # Should throw an error
