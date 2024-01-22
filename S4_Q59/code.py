class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1  # Number of nodes in the subtree rooted at this node


class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, node, x):
        if node is None:
            return Node(x)
        if x < node.val:
            node.left = self._insert(node.left, x)
        else:
            node.right = self._insert(node.right, x)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, node, x):
        if node is None:
            return None
        if x < node.val:
            node.left = self._delete(node.left, x)
        elif x > node.val:
            node.right = self._delete(node.right, x)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_val = self._min(node.right)
            node.val = min_val
            node.right = self._delete(node.right, min_val)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def find(self, a, b):
        result = []
        self._find(self.root, a, b, result)
        return result

    def _find(self, node, a, b, result):
        if node is None:
            return
        if a <= node.val <= b:
            result.append(node.val)
        if node.val >= a:
            self._find(node.left, a, b, result)
        if node.val <= b:
            self._find(node.right, a, b, result)

    def _size(self, node):
        return node.size if node else 0

    def _min(self, node):
        while node.left:
            node = node.left
        return node.val
