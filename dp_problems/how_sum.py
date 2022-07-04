# Write a function `how_sum(target_sum, numbers)` that takes in a target_sum and an array as input.
# The function should return an array consisting of the combinations of numbers that add exactly upto target sum
# Conditions:
# 1. We can reuse an element any number of times.
# 2. Input numbers are non-negative

# m -> Target sum, n--> array length

# Brute Force
# Time Complexity: O(n ^ m * m)
#       --> Why o(n^m)? --> m is the height of the tree and in each iteration we iterate over array of n size.
#       --> *m --> due to the array we are creating
# Space Complexity: O(m)

# Memoization:
# Time Complexity: O(n * m^2)
# Space Complexity: O(m ^ 2)


def how_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        val = how_sum(remainder, numbers, memo)
        if val is not None:
            memo[target_sum] = [*val, num]
            return memo[target_sum]

    memo[target_sum] = None
    return None


print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(8, [2, 5, 3]))
print(how_sum(8, [1, 4, 5]))
print(how_sum(300, [10]))
