
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)

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

print("\t  a")
print("\t/\t\\")
print("\tb\t\tc")
print("   /  \\      \\")
print("  d\t   e\t\tf")

print("="*100)
print("Inorder")
in_order(a)
print("="*100)

print("="*100)
print("Post order")
post_order(a)
print("="*100)

print("="*100)
print("Pre order")
pre_order(a)
print("="*100)

