class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val



def depth(node: Node):
    count = 0
    while node:
        count += 1
        node = node.parent
    
    return count


def lca(a: Node, b: Node):
    depthA = depth(a)
    depthB = depth(b)

    if depthA > depthB:
        while depthA > depthB:
            a = a.parent
            depthA -= 1
    
    elif depthB > depthA:
        while depthB > depthA:
            b = b.parent
            depthB -= 1
    
    while a and b and (a is not b):
        a = a.parent
        b = b.parent
    
    return a if (a is b) else None


# without parent pointer
def lowestCommonAncestor(root: Node, p: Node, q: Node) -> Node:
    if not root:
        return None

    if root in (p, q):
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    
    return left or right


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    a.parent = c
    c.parent = e
    e.parent = f

    b.parent = d
    d.parent = f

    f.parent = g

    assert lca(a, b) == f
