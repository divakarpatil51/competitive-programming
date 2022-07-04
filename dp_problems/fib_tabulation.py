# Fib using tabulation
# Time complexity: O(n)
# Space complexity: O(n)

def fib(num):
    fib_table = [0] * (num + 1)
    fib_table[1] = 1
    for i in range(1, num):
        fib_table[i + 1] = fib_table[i] + fib_table[i - 1]

    return fib_table[-1]


def fib_with_constant_space(num):
    curr = 1
    prev = 0
    for _ in range(num):
        # next_number = curr + prev
        # prev = curr
        # curr = next_number
        prev, curr = curr, curr + prev

    return curr


def fib_with_classic_tabulation(num):
    table = [0] * (num + 1)
    table[1] = 1
    for i in range(num):
        table[i + 1] += table[i]
        if i + 2 <= num:
            table[i + 2] += table[i]

    return table[num]


# print(fib_with_constant_space(3))
print(fib_with_classic_tabulation(6))
# print(fib_with_constant_space(5))
# print(fib_with_constant_space(6))
# print(fib_with_constant_space(7))
# print(fib_with_constant_space(8))
# print(fib_with_constant_space(50))
# print(fib(6))
# print(fib(7))
# print(fib(8))
# print(fib(50))
