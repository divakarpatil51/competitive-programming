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


def depth_first_values(node, search_term='e'):
    if not node:
        return False
    if node.value == search_term:
        return True

    is_left_found = depth_first_values(node.left, search_term)
    is_right_found = depth_first_values(node.right, search_term)

    return is_left_found or is_right_found


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

val = depth_first_values(a)
print("First::::: ", val)
assert val
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

val = depth_first_values(a)
print("Second::::: ", val)
assert val

a = Node('a')
#     a
val = depth_first_values(a)
print("Third::::: ", val)
assert val is False

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

val = depth_first_values(a)
print("fourth::::: ", val)
assert val

val = depth_first_values(None)
print("fifth::::: ", val)
assert val is False
