# Problem Statement:
# Find the shortest path between given src and dst. Consider each edge has a weight of 1. We will be give an edge list.
from  collections import deque


def shortest_path(edge_list, src, dst):
    # Convert edge_list to graph
    graph = to_graph(edge_list)
    # Traverse graph using BFS as it explores nodes evenly
    queue = deque()
    queue.append((src, 0))
    visited = []
    while len(queue) > 0:
        curr, cost = queue.popleft()
        if dst == curr:
            return cost
        if curr in visited:
            continue
        visited.append(curr)
        neighbors = graph.get(curr)
        for neighbor in neighbors:
            queue.append((neighbor, cost + 1))
    return -1


def to_graph(edge_list):
    graph = {}
    for edge in edge_list:
        n1, n2 = edge
        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph


op = shortest_path([
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
], 'w', 'z')

print(op)
assert op == 2

op = shortest_path([
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
], 'y', 'x')

print(op)
assert op == 1

op = shortest_path([
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
], 'a', 'e')

print(op)
assert op == 3

op = shortest_path([
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
], 'e', 'c')

print(op)
assert op == 2

op = shortest_path([
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
], 'b', 'g')

print(op)
assert op == -1

edges = [
    ['c', 'n'],
    ['c', 'e'],
    ['c', 's'],
    ['c', 'w'],
    ['w', 'e'],
]

op = shortest_path(edges, 'w', 'e')  # -> 1
print(op)
assert op == 1

edges = [
    ['c', 'n'],
    ['c', 'e'],
    ['c', 's'],
    ['c', 'w'],
    ['w', 'e'],
]

op = shortest_path(edges, 'n', 'e')  # -> 2

print(op)
assert op == 2

edges = [
    ['m', 'n'],
    ['n', 'o'],
    ['o', 'p'],
    ['p', 'q'],
    ['t', 'o'],
    ['r', 'q'],
    ['r', 's']
]

op = shortest_path(edges, 'm', 's')
print(op)
assert op == 6
