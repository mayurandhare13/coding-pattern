from sys import maxsize

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isValidBSTHelper(node: Node, lb, ub):
    if not node:
        return True
    
    if node.val < lb or node.val > ub:
        return False
    
    return isValidBSTHelper(node.left, lb, node.val) and \
        isValidBSTHelper(node.right, node.val, ub)


def isValidBST(root: Node):
    return isValidBSTHelper(root, -maxsize, maxsize)


if __name__ == '__main__':
    assert isValidBST(None)

    a = Node(3)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(3)
    f = Node(4)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    assert isValidBST(a)


    a = Node(1)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(3)
    f = Node(4)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    assert not isValidBST(a)
