# Write a function `count_construct(target_string, string_arr)` that takes in a target_string and an array as strings.
# The function should return number of ways the target string can be built using elements in the string_arr.
# Conditions:
# 1. We can reuse an element any number of times.

# m - len of target string
# n - array length
# Brute Force
# Time Complexity: O(n ^ m * m) -->  n loops  m times and m for the slicing of the string.
# Space Complexity: O(m ^ 2) --> height of the tree * space required for storing the sliced string.

# Memoized
# Time Complexity: O(n * m * m)
# Space Complexity: O(m) --> height of the tree.

def count_construct(target_string: str, string_arr: list, memo=None):
    if memo is None:
        memo = {}
    if target_string in memo:
        return memo[target_string]
    if target_string == '':
        return 1

    total_count = 0
    for element in string_arr:
        if target_string.startswith(element):
            stripped = target_string[len(element):]
            count = count_construct(stripped, string_arr, memo)
            total_count += count
            memo[target_string] = total_count
    memo[target_string] = total_count
    return total_count


print(count_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct("abcdef", ['ab', 'abc', 'cd', 'def']))
print(count_construct("skateboard", ['ska', 'bo', 'rd', 'ate', 't', 'sk', 'boar']))
print(count_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
