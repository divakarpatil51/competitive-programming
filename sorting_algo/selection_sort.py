# Time Complexity:
# Worst case: O(n ^ 2)

# Space Complexity: O(1) --> Since we are doing sorting in place

# We are moving elements from unsorted array to sorted array by finding the smallest element in unsorted array.
def selection_sort(arr: list):
    for i in range(len(arr)):
        curr = i
        for j in range((i + 1), len(arr)):
            if arr[j] < arr[curr]:
                curr = j
        arr[i], arr[curr] = arr[curr], arr[i]
    return arr


op = selection_sort([-1, 100, 2, 1, 3, 2])
print(op)
