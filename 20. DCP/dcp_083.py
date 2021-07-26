class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def invertBinaryTree(root: Node):
    if root is None:
        return
    
    root.left, root.right = \
        invertBinaryTree(root.right), invertBinaryTree(root.left)
    
    return root


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
    b.right = e
    c.left = f

    invertRoot = invertBinaryTree(a)
    assert invertRoot.left == c
    assert invertRoot.right == b
    assert invertRoot.left.right == f
    assert invertRoot.right.right == d
