# Custom Data Structure in Python

## Introduction

The following Python code defines a `CustomDataStructure` class, designed to create a custom data structure for efficiently storing and retrieving elements with indices ranging from 1 to n. The implementation aims to achieve O(n) memory complexity for initialization and O(1) time complexity for the `set` and `get` operations.

## Code Explanation

```python
class CustomDataStructure:
    def __init__(self):
        self.data = []

    def set(self, x, y):
        if x < 0:
            raise ValueError("Index cannot be negative.")
        elif x < len(self.data):
            self.data[x] = y
        else:
            self._resize_and_set(x, y)

    def _resize_and_set(self, i, y):
        new_data = [None] * (i - len(self.data) + 1)
        self.data += new_data
        self.data[i] = y

    def get(self, x):
        if 0 <= x < len(self.data):
            return self.data[x]
        else:
            raise IndexError("Index out of range.")
```

### Class Methods:

1. **`__init__(self)`**: Initializes the `CustomDataStructure` with an empty list.

2. **`set(self, x, y)`**: Sets the value `y` at index `x`. If `x` is negative, a `ValueError` is raised. If `x` is within the current length of the data, the value is updated. Otherwise, the `_resize_and_set` method is called to extend the data list.

3. **`_resize_and_set(self, i, y)`**: Resizes the data list to accommodate the index `i` and sets the value `y` at that index.

4. **`get(self, x)`**: Retrieves the value at index `x`. If `x` is out of range, an `IndexError` is raised.

## Usage

To use the `CustomDataStructure` class, instantiate an object and perform `set` and `get` operations.

Example:

```python
custom_ds = CustomDataStructure()

# Setting values
custom_ds.set(1, 10)
custom_ds.set(3, 30)

# Getting values
value_at_index_1 = custom_ds.get(1)
value_at_index_3 = custom_ds.get(3)

print(value_at_index_1)  # Output: 10
print(value_at_index_3)  # Output: 30
```

## Conclusion

The `CustomDataStructure` class provides an efficient solution for storing and retrieving elements with indices ranging from 1 to n. The implementation ensures O(n) memory complexity for initialization and O(1) time complexity for the `set` and `get` operations.
