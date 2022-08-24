"""
Heap sort Algorithm uses heap as its underlying structure to sort the data. It is an extension of selection sort
using a better data structure.

Time complexity: O(n log n)
Space Complexity: O(1)
"""


def heapify(arr, n, curr):
    """
    Heapifies the given array
    """
    largest = curr
    l_child = 2 * curr + 1
    r_child = 2 * curr + 2

    if l_child < n and arr[curr] < arr[l_child]:
        largest = l_child

    if r_child < n and arr[largest] < arr[r_child]:
        largest = r_child

    if largest != curr:
        arr[largest], arr[curr] = arr[curr], arr[largest]
        heapify(arr, n, largest)


def heap_sort(arr: list):
    n = len(arr)

    for curr in range(n // 2, -1, -1):
        heapify(arr, n, curr)

    for curr in range(n - 1, 0, -1):
        # Swap
        arr[curr], arr[0] = arr[0], arr[curr]

        # Heapify root element
        heapify(arr, curr, 0)


if __name__ == "__main__":
    arr = [10, 1, 12, 15, 5, 6]
    heap_sort(arr)
    print(arr)
