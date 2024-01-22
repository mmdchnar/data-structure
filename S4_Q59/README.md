# Binary Search Tree (BST) for X-Axis Points in Python

## Introduction

The Python code defines a Binary Search Tree (BST) data structure tailored for storing points on the X-axis. It supports efficient insertion, deletion, and finding points within a given range [a, b]. The time complexities for the key operations are as follows:
- Insertion: O(log n)
- Deletion: O(log n)
- Finding points within range [a, b]: O(log n + k), where k is the number of points in the specified range.

## Code Explanation

```python
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
```

### Class Components:

1. **`Node` Class**: Represents a node in the BST, containing a value (`val`), left and right child references, and the size of the subtree rooted at the node.

2. **`BST` Class**: Implements the Binary Search Tree with the following methods:

    - **`__init__(self)`:** Initializes an empty BST with a `None` root.
    
    - **`insert(self, x)`:** Inserts a value `x` into the BST. The private `_insert` method is called recursively for the insertion operation.
    
    - **`_insert(self, node, x)`:** Recursively inserts a value `x` into the BST and updates the size of the current node's subtree.
    
    - **`delete(self, x)`:** Deletes a node with value `x` from the BST. The private `_delete` method is called recursively for the deletion operation.
    
    - **`_delete(self, node, x)`:** Recursively deletes a node with value `x` from the BST and updates the size of the current node's subtree.
    
    - **`find(self, a, b)`:** Finds points within the range [a, b] in the BST. The private `_find` method is called recursively for the search operation.
    
    - **`_find(self, node, a, b, result)`:** Recursively finds points within the range [a, b] in the BST and appends them to the `result` list.
    
    - **`_size(self, node)`:** Returns the size of the subtree rooted at the given node, or 0 if the node is `None`.
    
    - **`_min(self, node)`:** Returns the minimum value in the subtree rooted at the given node.

### Time Complexities:

- **Insertion (`insert` and `_insert`):** O(log n) - logarithmic time complexity.
  
- **Deletion (`delete` and `_delete`):** O(log n) - logarithmic time complexity.
  
- **Finding Points (`find` and `_find`):** O(log n + k), where k is the number of points in the specified range [a, b].

## Usage

```python
bst = BST()

# Inserting values
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(9)

# Deleting a value
bst.delete(4)

# Finding points in the range [3, 7]
points_in_range = bst.find(3, 7)
print(points_in_range)  # Output: [3, 5, 6, 7]
```

## Conclusion

The Binary Search Tree implemented in this code provides an efficient way to store and retrieve points on the X-axis. The time complexities for insertion, deletion, and finding points within a specified range make it suitable for various applications where these operations are crucial.
