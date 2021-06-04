class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(node: Node):
    if not node:
        return

    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)


def isLeaf(node: Node):
    return node.left is None and node.right is None


def truncate(root: Node):
    if not root:
        return None
    
    root.left = truncate(root.left)
    root.right = truncate(root.right)

    if (root.left and root.right) or isLeaf(root):
        return root

    # if current node has exactly one child, then delete it
    # replace with child node
    child = root.left if root.left else root.right
    return child


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.left.right = Node(5)
    root.right.right = Node(4)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    root = truncate(root)
    inorder(root)

    print()

