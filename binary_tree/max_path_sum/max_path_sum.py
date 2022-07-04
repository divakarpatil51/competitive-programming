# Time Complexiy: O(n) as we are visiting one node at a time
# Space complexity: O(n)

# Iteration Approach:
# Here, we add the current node on top of stack and then pop them one by one until all the nodes are visited.
import math


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def depth_first_values(node: Node):
    if not node:
        return 0
    left_val = depth_first_values(node.left)
    right_val = depth_first_values(node.right)
    return max(node.value + left_val, node.value + right_val)


a = Node(10)
b = Node(-5)
c = Node(3)
d = Node(2)
e = Node(15)
f = Node(12)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      10
#    /   \
#   -5     3
#  / \     \
# 2   15     12

val = depth_first_values(a)
print("First::::: ", val)
assert val == 25
#

a = Node(10)
b = Node(5)
c = Node(3)
d = Node(2)
e = Node(15)
f = Node(12)
g = Node(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      10
#    /   \
#   5     3
#  / \     \
# 2   15     12
#    /
#   1

val = depth_first_values(a)
print("Second::::: ", val)
assert val == 31

a = Node(10)
#     a
val = depth_first_values(a)
print("Third::::: ", val)
assert val == 10

a = Node(10)
b = Node(5)
c = Node(3)
d = Node(2)
e = Node(15)
a.right = b
b.left = c
c.right = d
d.right = e

#      10
#       \
#        5
#       /
#      3
#       \
#        2
#         \
#          15

val = depth_first_values(a)
print("fourth::::: ", val)
assert val == 35

val = depth_first_values(None)
print("fifth::::: ", val)
assert val == 0
