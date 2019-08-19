
input_number = int(input())

prime = []


def is_prime(num1, divisor):
    if divisor == 1:
        return True
    if num1 % divisor != 0:
        return is_prime(num1, divisor - 1)
    return False


for num in range(2, input_number + 1):
    if is_prime(num, int(num/2)):
        prime.append(num)

# * --> For printing array
print(*prime)
