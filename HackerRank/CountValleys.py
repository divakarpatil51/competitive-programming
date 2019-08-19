def countingValleys(n, s):
    mountain = 0
    valley = 0

    for path in s:
        if path == 'U':
            mountain += 1
            
            if mountain == 0:
                valley += 1
        else:
            mountain -= 1


    return valley


if __name__ == '__main__':
    print(countingValleys(8, "UDDDUDUU"))
