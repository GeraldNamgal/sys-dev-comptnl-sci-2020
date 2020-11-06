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
        try:
            get_node(node, key).val = val           # Update node if exists
        except Exception:
            node = add_node(node, key, val)         # Else add it to tree
        return node

    # TODO: Check that updating size of nodes is working right
    def _get(self, node, key):
        if node is None:
            raise KeyError
        print(node.size)  # TODO: Remove this later
        if key == node.key:
            return node.val
        if key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    @staticmethod
    def _size(node):
        return node.size if node else 0


# Utility function
def get_node(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node
    if node.key > key:
        return get_node(node.left, key)
    else:
        return get_node(node.right, key)


# Utility function
def add_node(node, key, val):
    if node is None:
        return BSTNode(key, val)  # Add new node
    if node.key > key:
        node.left = add_node(node.left, key, val)
    if node.key < key:
        node.right = add_node(node.right, key, val)
    node.size += 1
    return node


# TODO: Debugging...
# greektoroman = BSTTable()
# greektoroman.put('Athena',    'Minerva')
# greektoroman.put('Eros',      'Cupid')
# greektoroman.put('Aphrodite', 'Venus')
# print(greektoroman.get('Eros'))
# print()
# print(greektoroman)
# # Test that value gets replaced (i.e., instead of added) --
# greektoroman.put('Aphrodite', 'Dumbledore')
# print()
# print(greektoroman.get('Eros'))   # Size should stay the same for just updates
# print()
# print(greektoroman)

tree = BSTTable()
list = [13,7,19,17,3,29,5,31,2,11]
# list = [7,19,17,3,29,5,31,2,11]
# list = [13,7,19,17,3,5,31,2,11]
# list = [13,7,19,17,3,29,5,2,11]
for num in list:
    tree.put(num, num)
print(tree)
tree.get(17)
tree.put(29, 'update')
print(tree)
tree.get(17)                        # Size should stay the same for just updates
tree.put(70, 70)
print(tree)
tree.get(70)