# Write a function `all_construct(target_string, string_arr)` that takes in a target_string and an array as strings.
# The function should return all the combinations the target string can be built using elements in the string_arr.
# Conditions:
# 1. We can reuse an element any number of times.

# m - len of target string
# n - array length
# Brute Force
# Time Complexity: O(n ^ m ) -->  n loops  m times
# Space Complexity: O(m) --> height of the tree * space required for storing the sliced string.

# Memoized
# Time Complexity: O(n ^ m ) -->  n loops  m times
# Space Complexity: O(m) --> height of the tree * space required for storing the sliced string.

def all_construct(target_string: str, string_arr: list, memo=None):
    if target_string == '':
        return [[]]

    available_constructs = []
    for element in string_arr:
        if target_string.startswith(element):
            stripped = target_string[len(element):]
            curr_construct = all_construct(stripped, string_arr, memo)
            data = list(map(lambda ele: [element, *ele], curr_construct))
            available_constructs.append(*data)

    return available_constructs


# print(all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'ef']))
# print(all_construct("skateboard", ['ska', 'bo', 'rd', 'ate', 't', 'sk', 'boar']))
# print(all_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
# print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
