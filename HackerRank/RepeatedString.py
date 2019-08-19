# Given an integer, , find and print the number of letter a's in the first n letters of Lilah's infinite string.
# s = 'abc'
# n = 10
# o/p: 4


def repeated_string(s, n):

    count = s.count('a')
    if count == 0:
        return 0

    repetitions = int(n / len(s))
    remainder = n % len(s)
    total_count = (repetitions * count) + s.count('a', 0, remainder)

    return total_count


if __name__ == "__main__":
    print(repeated_string('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', 549382313570))
