# Write a function `can_sum(target_sum, numbers)` that takes in a target_sum and an array as input.
# The function should return a boolean indicating whether it is possible to generate target_sum using the
# elements in the array.
# Conditions:
# 1. We can reuse an element any number of times.
# 2. Input numbers are non-negative

# Time Complexity: O(m * n)
# Space Complexity: O(m)
# where, m is target_sum and n is len(input_numbers)


def can_sum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True

    for curr in range(target_sum):
        if not table[curr]:
            continue
        for num in numbers:
            if curr + num < len(table):
                table[curr + num] = True
    return table[target_sum]


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [5, 3, 2]))
print(can_sum(8, [1, 4, 5]))
print(can_sum(300, [14, 7]))
