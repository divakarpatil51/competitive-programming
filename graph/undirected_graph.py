# Write a program to check if we can travel from source to destination.

# Time complexity: O(e) --> number of edges in the graph
# Space complexity: 0(n) --> number of nodes in the graph

# Approach:
# 1. It is better to convert edgelist to adjacency list format as it is easier to travel.
# 2. We have to keep track of visited node as there can be cycle in our graph

def build_graph(_edge_list):
    graph = {}
    for edge in _edge_list:
        n1, n2 = edge
        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph


def undirected_graph(_edge_list, src, dst):
    graph = build_graph(_edge_list)
    return has_path_dfs(graph, src, dst, set()) == has_path_bfs(graph, src, dst, set())


def has_path_dfs(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        has_path = has_path_dfs(graph, neighbor, dst, visited)
        if has_path:
            return True

    return False


def has_path_bfs(graph, src, dst, visited):
    from collections import deque
    queue = deque(src)
    while len(queue) > 0:
        element = queue.popleft()
        if element == dst:
            return True
        if element in visited:
            continue
        visited.add(element)
        for neighbor in graph[element]:
            queue.append(neighbor)

    return False


edge_list = [
    ['i', 'j'],
    ['i', 'k'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(undirected_graph(edge_list, "i", 'n'))
