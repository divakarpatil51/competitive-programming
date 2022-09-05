"""
QuickSort Algorithm: It is based on divide and conquer approach. Better performance for scattered pivots.

Time Complexity:
Worst case: O(n ^ 2)
Avg case: O(n * lg n)

Space Complexity: O(lg n)
"""


def partition(arr, low, high):
    pivot = high
    new_high = low

    for i in range(low, high):
        if arr[i] < arr[pivot]:
            arr[i], arr[new_high] = arr[new_high], arr[i]
            new_high += 1
    arr[pivot], arr[new_high] = arr[new_high], arr[pivot]

    return new_high


def quick_sort(arr, low, high):
    if high > low:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


if __name__ == "__main__":

    _arr = [10, 1, 5, 3, 11, 15, 20, 100]
    print(_arr)
    quick_sort(_arr, 0, len(_arr) - 1)
    print(_arr)
