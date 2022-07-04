# Write a function `can_sum(target_sum, numbers)` that takes in a target_sum and an array as input.
# The function should return a boolean indicating whether it is possible to generate target_sum using the
# elements in the array.
# Conditions:
# 1. We can reuse an element any number of times.
# 2. Input numbers are non-negative


def can_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}

    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        if can_sum(target_sum - num, numbers):
            memo[target_sum - num] = True
            return True
    memo[target_sum] = False
    return False


print(can_sum(1994, [2, 3]))
