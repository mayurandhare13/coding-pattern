class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f"node: {self.val}, left: {self.left}, right: {self.right}\n"


def printTree(r: Node):
    if not r:
        return

    print(r)
    printTree(r.left)
    printTree(r.right)


def prune(root):
    if root is None:
        return root

    root.left, root.right = prune(root.left), prune(root.right)

    if root.left is None and root.right is None and root.val == 0:
        return None

    return root



if __name__ == '__main__':
    '''
     0
    / \
   1   0
      / \
     1   0
    / \
   0   0
    '''
    root = Node (
        val = 0,
        left = Node(1),
        right = Node(0, Node(1, Node(0), Node(0)), Node(0))
    )

    r = prune(root)
    printTree(r)
