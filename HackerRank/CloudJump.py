
def cloud_jump(c):
    jump_count = 0
    curr_pos = 0

    while curr_pos < len(c) - 1:

        if curr_pos + 2 < len(c) and c[curr_pos + 2] == 0:
            jump_count += 1
            curr_pos += 2
        else:
            jump_count += 1
            curr_pos += 1

    return jump_count


if __name__ == "__main__":
    print(cloud_jump([0, 0, 0, 1, 0, 0]))
