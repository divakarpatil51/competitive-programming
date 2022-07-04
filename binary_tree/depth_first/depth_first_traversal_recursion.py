# Time Complexity: O(n) as we are visiting one node at a time
# Space complexity: O(n)

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def depth_first_values(node: Node):
    if not node:
        return []
    left = depth_first_values(node.left)
    right = depth_first_values(node.right)
    return [node.value, *left, *right]


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
print(val)
assert val == ['a', 'b', 'd', 'e', 'c', 'f']
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
assert val == ['a', 'b', 'd', 'e', 'g', 'c', 'f']

a = Node('a')
#     a
val = depth_first_values(a)
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

val = depth_first_values(a)
assert val == ['a', 'b', 'c', 'd', 'e']

val = depth_first_values(None)
assert val == []