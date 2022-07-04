# Depth first traversal of Graph with given start node.
# We use STACK as we are going in multiple levels.

def depth_first_print_recursive(graph, start_node):
    print(start_node)
    neighbours = graph.get(start_node)
    for neighbour in neighbours:
        depth_first_print_recursive(graph, neighbour)


def depth_first_print_iterative(graph, start_node):
    stack = [start_node]
    while len(stack) > 0:
        curr_node = stack.pop()
        print(curr_node)
        neighbours = graph.get(curr_node)
        stack.extend(neighbours)


_graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

print("Depth first Recursive")
depth_first_print_recursive(_graph, 'a')


print("Depth first Iterative")
depth_first_print_iterative(_graph, 'a')
