# Problem Statement:
# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph.
# The function should return the number of connected components within the graph

from collections import deque


def connected_components_count(_graph):
    count = 0
    visited = set()

    for element in _graph:
        if element in visited:
            continue
        queue = deque()
        queue.append(element)
        while len(queue) > 0:
            ele = queue.popleft()
            if ele in visited:
                continue
            visited.add(ele)
            for neighbor in _graph[ele]:
                queue.append(neighbor)

        count += 1

    return count


_count = connected_components_count({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}) # -> 2

print(_count)
