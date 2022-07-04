# Write code to check if there is a path from src to destination node.

# Depth First Search and BFS time complexities:
# n - nodes, e - edges.
# Time Complexity: O(e) --> as we are going to traverse to the edges.
# Space Complexity: O(n) --> number of nodes in our graph


def has_path_dfs(graph, src, dst):
    if src == dst:
        return True

    neighbors = graph.get(src)
    for neighbor in neighbors:
        has_path = has_path_dfs(graph, neighbor, dst)
        if has_path:
            print(src, "--->", neighbor, "-->", dst)
            return True
    return False


def has_path_bfs(graph, src, dst):
    from collections import deque
    queue = deque()
    queue.append(src)
    while len(queue) > 0:
        print(queue)
        curr = queue.popleft()
        if curr == dst:
            return True
        queue.extend(graph.get(curr))

    return False


_graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [],
    "h": []
}

print("*" * 10)
print("DFS")
print(has_path_dfs(_graph, "f", "j"))
print("*" * 10)

print("*" * 10)
print("BFS")
print(has_path_bfs(_graph, "f", "j"))
print("*" * 10)
