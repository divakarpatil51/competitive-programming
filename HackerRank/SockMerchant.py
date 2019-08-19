
def sock_merchant(ar):
    sock_map = {}
    count = 0
    for sock_color in ar:

        if sock_color in sock_map.keys():
            if sock_map[sock_color] & 1 == 1:
                count += 1
            sock_map[sock_color] = (sock_map[sock_color] + 1)
        else:
            sock_map[sock_color] = 1

    return count


if __name__ == "__main__":
    print(sock_merchant([1, 2, 1, 3, 1, 2]))
