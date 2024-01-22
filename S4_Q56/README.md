# Height Comparison in Python

## Introduction

The Python code provides a function to check if the tallest height in a given list is equal to or taller than twice the height of the shortest person. This functionality is achieved in O(n) time complexity, making it suitable for various applications involving human height data.

## Code Explanation

```python
def is_tallest_double_of_shortest(heights: list):
    if not heights or len(heights) < 2:
        return False

    shortest_height = float('inf')
    tallest_height = float('-inf')

    for height in heights:
        if height < shortest_height:
            shortest_height = height
        if height > tallest_height:
            tallest_height = height

    return tallest_height >= 2 * shortest_height
```

### Algorithm Steps:

1. Initialize `shortest_height` and `tallest_height` to positive and negative infinity, respectively.
2. Iterate through the given `heights` list.
3. Update `shortest_height` if the current height is smaller.
4. Update `tallest_height` if the current height is larger.
5. Check if the tallest height is equal to or taller than twice the shortest height.
6. Return `True` if the condition is met; otherwise, return `False`.

### Time Complexity:

The algorithm achieves a time complexity of O(n), where n is the length of the input list.

## Examples

### Example 1: False
```python
heights_list_false = [160, 175, 150, 180, 155]
result_false = is_tallest_double_of_shortest(heights_list_false)
print(result_false)  # Output: False
```

### Example 2: True
```python
heights_list_true = [60, 175, 150, 180, 155, 190]
result_true = is_tallest_double_of_shortest(heights_list_true)
print(result_true)  # Output: True
```

## Conclusion

This height comparison function provides an efficient solution for determining if the tallest person in a given list is equal to or taller than twice the height of the shortest person. It operates in O(n) time complexity, making it suitable for various scenarios involving height analysis.
