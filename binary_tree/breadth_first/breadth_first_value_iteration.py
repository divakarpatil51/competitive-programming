# Time Complexiy: O(n) as we are visiting one node at a time
# Space complexity: O(n)

# Iteration Approach:
# Here, we add the current node on top of stack and then pop them one by one until all the nodes are visited.
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

def breadth_first_values(node):
    if not node:
        return []
    bfs = []
    queue = [node]
    while len(queue) > 0:
        curr = queue.pop(0)
        bfs.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return bfs


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

val = breadth_first_values(a)
print("First::::: ", val)
assert val == ['a', 'b', 'c', 'd', 'e', 'f']
#

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

val = breadth_first_values(a)
print("Second::::: ", val)
assert val == ['a', 'b', 'c', 'd', 'e', 'f', 'g']

a = Node('a')
#     a
val = breadth_first_values(a)
print("Third::::: ", val)
assert val == ['a']

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b
b.left = c
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

val = breadth_first_values(a)
print("fourth::::: ", val)
assert val == ['a', 'b', 'c', 'd', 'e']

val = breadth_first_values(None)
print("fifth::::: ", val)
assert val == []
