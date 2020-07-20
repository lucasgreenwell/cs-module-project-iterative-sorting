def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (high + low) // 2
        if arr[middle] == target:
            return middle
        elif arr[high] == target:
            return high
        elif arr[low] == target:
            return low
        elif target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1

    return -1




    return -1  # not found
