class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def evaluateExpression(root: Node):
    if not root:
        return 0
    
    if root.val.isnumeric():
        return float(root.val)

    l = evaluateExpression(root.left)
    r = evaluateExpression(root.right)

    total = 0

    if root.val == '+':
        total = l + r
    elif root.val == '-':
        total = l - r
    elif root.val == '*':
        total = l * r
    elif root.val == '/':
        total = l / r
    
    return total


if __name__ == '__main__':
    d = Node('3')
    e = Node('2')
    f = Node('4')
    g = Node('5')

    b = Node('+')
    b.left = d
    b.right = e

    c = Node('+')
    c.left = f
    c.right = g

    a = Node('*')
    a.left = b
    a.right = c

    assert evaluateExpression(a) == 45
    assert evaluateExpression(c) == 9
    assert evaluateExpression(b) == 5
    assert evaluateExpression(d) == 3
