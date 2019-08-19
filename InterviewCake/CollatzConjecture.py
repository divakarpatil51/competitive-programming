# Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one
# using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

from random import randint


def collatz_conjecture(random_int, steps):

    print("Random int: ", random_int)
    steps += 1
    if random_int == 1:
        return steps

    if random_int & 1 == 0:
        random_int = random_int // 2
    else:
        random_int = random_int * 3 + 1

    return collatz_conjecture(random_int, steps)


if __name__ == "__main__":
    print("Number of steps required: ", collatz_conjecture(randint(1, 100), 0))
