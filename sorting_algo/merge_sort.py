def merge(arr, low, middle, high):
    left_arr = arr[low:middle + 1]
    right_arr = arr[middle + 1:high + 1]
    i = low
    # Merge arrays:
    while len(left_arr) and len(right_arr):
        if left_arr[0] <= right_arr[0]:
            arr[i] = left_arr.pop(0)
        else:
            arr[i] = right_arr.pop(0)
        i += 1

    while len(left_arr):
        arr[i] = left_arr.pop(0)
        i += 1

    while len(right_arr):
        arr[i] = right_arr.pop(0)
        i += 1


def merge_sort(arr, low, high):
    if low < high:
        middle = (low + high) // 2
        merge_sort(arr, low, middle)
        merge_sort(arr, middle + 1, high)
        merge(arr, low, middle, high)


if __name__ == "__main__":
    arr = [100, 12, 5, 6, 2, 15, 11, 1, 4, 3, 1]
    merge_sort(arr, 0, len(arr))
    print(arr)
