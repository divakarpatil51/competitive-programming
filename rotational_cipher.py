import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(_input: str, rotation_factor):
    # Write your code here
    # 4 cases - Upper, lower, digit, non-alphanumeric
    rotated_str = ""
    for char in _input:
        if char.isalpha():
            first_val = ord('a') if char.islower() else ord('A')
            rotated_str += str(chr((ord(char) + rotation_factor - first_val) % 26 + first_val))
        elif char.isdigit():
            rotated_str += str((int(char) + rotation_factor) % 10)
        else:
            rotated_str += char
    return rotated_str


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here
