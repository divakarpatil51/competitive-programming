# Write a function `best_sum(target_sum, numbers)` that takes in a target_sum and an array as input.
# The function should return an array consisting of the shortest combinations of numbers that add exactly upto target
# sum
# Conditions:
# 1. We can reuse an element any number of times.
# 2. Input numbers are non-negative

# m -> Target sum, n--> array length

# Brute Force
# Time Complexity: O(n ^ m * m)
#       --> Why o(n^m)? --> m is the height of the tree and in each iteration we iterate over array of n size.
#       --> *m --> due to the array we are creating
# Space Complexity: O(m ^ 2) --> due to the shortest combination variable.

# Memoization:
# Time Complexity: O(n * m^2)
# Space Complexity: O(m ^ 2)

def best_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = best_sum(remainder, numbers, memo)
        if remainder_result is not None:
            new_combination = [*remainder_result, num]
            memo[target_sum] = new_combination
            if shortest_combination is None or len(new_combination) < len(shortest_combination):
                shortest_combination = new_combination
    memo[target_sum] = shortest_combination
    return shortest_combination


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 5, 3]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
