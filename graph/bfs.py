# Breadth first traversal of Graph with given start node.
# We use Queue as DS.

from collections import deque


def breadth_first_print(graph, start_node):
    queue = deque(start_node)
    while len(queue) > 0:
        element = queue.popleft()
        print(element)
        queue.extend(graph[element])
    # queue = [start_node]
    # while len(queue) > 0:
    #     curr_node = queue.pop(0)
    #     print(curr_node)
    #     neighbours = graph.get(curr_node)
    #     queue.extend(neighbours)


_graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

breadth_first_print(_graph, 'a')

