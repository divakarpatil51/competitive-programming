# Write a function `how_sum(target_sum, numbers)` that takes in a target_sum and an array as input.
# The function should return an array consisting of the combinations of numbers that add exactly upto target sum
# Conditions:
# 1. We can reuse an element any number of times.
# 2. Input numbers are non-negative

# m -> Target sum, n--> array length

# Brute Force
# Time Complexity: O(m * m * n)
# Space Complexity: O(m * m)


def how_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []
    for i in range(target_sum):
        if table[i] is not None:
            for number in numbers:
                if number + i < len(table):
                    table[number + i] = [*table[i], number]

    return table[target_sum]


print(how_sum(7, [5, 3, 4, 7]))  # [4,3]
print(how_sum(7, [2, 3]))  # [2, 2,3]
print(how_sum(7, [2, 4]))  # None
print(how_sum(8, [2, 5, 3]))  # [2, 2, 2, 2]
print(how_sum(8, [1, 4, 5]))  # [1, 1, 1, 1, 1, 1, 1, 1]
print(how_sum(300, [
    10]))  # [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
