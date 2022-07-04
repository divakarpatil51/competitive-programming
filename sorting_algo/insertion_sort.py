# Time Complexity:
# Worst case: O(n ^ 2)

# Space Complexity: O(1) --> Since we are doing sorting in place

# We are moving elements from unsorted array to sorted array.
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j -= 1
    return arr


op = insertion_sort([10, 2, 1, 3, 2])
print(op)
