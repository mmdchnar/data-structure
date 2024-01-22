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
