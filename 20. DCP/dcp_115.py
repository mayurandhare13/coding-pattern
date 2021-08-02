class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: Node):
    order = []
    stack = [root]

    while stack:
        node = stack.pop()

        if not node:
            order.append('.')
            continue

        order.append(str(node.val))
        stack.append(node.right)
        stack.append(node.left)

    return ','.join(order)


def isSubtree(t: Node, s: Node):
    tOrder = preorder(t)
    sOrder = preorder(s)

    # O(M + N) time in the average case
    # O(M * N) in the worst case.
    return sOrder in tOrder


#-----------------------------------------------------

def isSubtree2(t: Node, s: Node):
    def isEqual(t: Node, s: Node):
        if t is None and s is None:
            return True

        if t is None or s is None:
            return False
        
        if t.val != s.val:
            return False
        
        return isEqual(t.left, s.left) and isEqual(t.right, s.right)

    if t is None:
        return False
    
    if isEqual(t, s):
        return True
    
    return isEqual(t.left, s) or isEqual(t.right, s)



if __name__ == '__main__':
    t = Node(1, Node(2), Node(3, Node(4), Node(5)))
    s = Node(3, Node(4), Node(5))

    assert isSubtree2(t, s)
