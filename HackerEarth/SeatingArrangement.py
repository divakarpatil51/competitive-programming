# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/
# 1. Get the matrix number and modulo from the seat number.

# Object containing modulo of the seats
seats = {1: (11, 'WS'),    2: (9, 'MS'),   3: (7, 'AS'),
         6: (1, 'WS'),     5: (3, 'MS'),   4: (5, 'AS'),
         7: (-1, 'WS'),    8: (-3, 'MS'),  9: (-5, 'AS'),
         0: (-11, 'WS'),  11: (-9, 'MS'), 10: (-7, 'AS')}

# TODO: Reduce time complexity and space complexity.
test_cases = int(input())
inputs = []
for test in range(0, test_cases):
    inputs.append(int(input()))

for num in inputs:
    opposite_seat, seat = seats[num % 12]
    print(num + opposite_seat, seat)
