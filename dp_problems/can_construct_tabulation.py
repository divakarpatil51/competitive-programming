# Write a function `can_construct(target_string, string_arr)` that takes in a target_string and an array as strings.
# The function should return true if target string can be built using elements in the string_arr.
# Conditions:
# 1. We can reuse an element any number of times.

# m - len of target string
# n - array length
# Time Complexity: O(n * m * m)
# Space Complexity: O(m) --> table length.

def can_construct(target_string: str, string_arr: list, memo=None):
    table = [False] * (len(target_string) + 1)
    table[0] = True

    for i in range(len(target_string)):
        if table[i]:
            for ele in string_arr:
                if target_string[i:i + len(ele)] == ele:
                    table[i + len(ele)] = True
        
    return table[len(target_string)]


print(can_construct("abcdef", ['ab', 'abc', 'cd', 'def']))
print(can_construct("skateboard", ['ska', 'bo', 'rd', 'ate', 't', 'sk', 'boar']))
print(can_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
