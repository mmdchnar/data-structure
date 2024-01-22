# Sorting Algorithm for -1, 0, 1 Elements in Python

## Introduction

This Python code provides an efficient sorting algorithm for lists containing only the elements -1, 0, and 1. The algorithm aims to achieve a time complexity of O(n), making it suitable for educational purposes, particularly in the context of data structure lessons.

## Code Explanation

```python
def sort_array(array):
    low, mid, high = 0, 0, len(array) - 1

    while mid <= high:
        if array[mid] == -1:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] == 0:
            mid += 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
    return array
```

### Algorithm Steps:

1. Initialize pointers `low`, `mid`, and `high` to the start, mid, and end of the array, respectively.
2. Iterate through the array using the `mid` pointer.
3. If the element at `mid` is -1, swap it with the element at `low` and increment both pointers.
4. If the element at `mid` is 0, increment only the `mid` pointer.
5. If the element at `mid` is 1, swap it with the element at `high` and decrement the `high` pointer.
6. Continue these steps until `mid` surpasses `high`.

### Time Complexity:

The algorithm achieves a time complexity of O(n), where n is the length of the input array. This efficiency is achieved through a single pass over the array.

## Usage

To use the `sort_array` function, simply pass a list containing only -1, 0, and 1 elements as an argument.

Example:

```python
my_list = [1, 0, -1, 1, 0, -1]
sorted_list = sort_array(my_list)
print(sorted_list)
```

Output:

```
[-1, -1, 0, 0, 1, 1]
```

## Conclusion

This sorting algorithm provides a practical solution for sorting lists with specific elements in linear time. It serves as an educational tool for understanding sorting algorithms and their applications in real-world scenarios.
