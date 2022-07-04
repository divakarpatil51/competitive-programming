# Write a function `best_sum(target_sum, numbers)` that takes in a target_sum and an array as input.
# The function should return an array consisting of the shortest combinations of numbers that add exactly upto target
# sum
# Conditions:
# 1. We can reuse an element any number of times.
# 2. Input numbers are non-negative

# m -> Target sum, n--> array length

# Time Complexity: O(n * m^2)
# Space Complexity: O(m ^ 2)

def best_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []
    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                if num + i <= target_sum:
                    curr_target = table[num + i]
                    new_target = [*table[i], num]
                    if table[num + i] is None or len(new_target) < len(curr_target):
                        table[num + i] = new_target

    return table[target_sum]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 5, 3]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
