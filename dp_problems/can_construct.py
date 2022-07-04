# Write a function `can_construct(target_string, string_arr)` that takes in a target_string and an array as strings.
# The function should return true if target string can be built using elements in the string_arr.
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

def can_construct(target_string: str, string_arr: list, memo=None):
    if memo is None:
        memo = {}
    if target_string in memo:
        return memo[target_string]
    if target_string == '':
        return True

    for element in string_arr:
        if target_string.startswith(element):
            stripped = target_string[len(element):]
            avail = can_construct(stripped, string_arr, memo)
            if avail:
                memo[target_string] = True
                return True
    memo[target_string] = False
    return False


print(can_construct("abcdef", ['ab', 'abc', 'cd', 'def']))
print(can_construct("skateboard", ['ska', 'bo', 'rd', 'ate', 't', 'sk', 'boar']))
print(can_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
