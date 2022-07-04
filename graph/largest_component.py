# Problem Statement:
# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph.
# The function should return the number of connected components within the graph

from collections import deque


def largest_component(_graph):
    largest_component_size = 0
    visited = set()

    for element in _graph:
        if element in visited:
            continue
        component_size = 0
        queue = deque()
        queue.append(element)
        while len(queue) > 0:
            ele = queue.popleft()
            if ele in visited:
                continue
            visited.add(ele)
            component_size += 1
            for neighbor in _graph[ele]:
                queue.append(neighbor)
        largest_component_size = max(largest_component_size, component_size)

    return largest_component_size


_count = largest_component({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}) # -> 4

assert _count == 4

_count = largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 6

assert _count == 6

_count = largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 5

assert _count == 5

_count = largest_component({}) # -> 0

assert _count == 0

_count = largest_component({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) # -> 3

assert _count == 3