class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def deepestNodeHelper(node: Node, depth):
    if node.left is None and node.right is None:
        return (node, depth)

    leftDepth, rightDepth = depth, depth

    if node.left:
        leftNode, leftDepth = deepestNodeHelper(node.left, depth + 1)

    if node.right:
        rightNode, rightDepth = deepestNodeHelper(node.right, depth + 1)

    return (leftNode, leftDepth) if leftDepth > rightDepth else \
            (rightNode, rightDepth)


def deepestNode(root: Node) -> int:
    return deepestNodeHelper(root, 0)[0]


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d

    assert deepestNode(a) == d

    c.left = e
    e.left = f


    assert deepestNode(a) == f
