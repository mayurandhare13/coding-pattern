class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def leftMost(curr: Node):
    while curr.left:
        curr = curr.left

    return curr



def inorderSuccessor(root: Node, p: Node):
    # if node has right child
    if p.right:
        return leftMost(p.right)

    # traverse tree from root --> p
    curr, successor = root, None

    while curr != p:
        if curr.val < p.val:
            curr = curr.right
        else:
            successor = curr
            curr = curr.left

    return successor


def inorderSuccessor2(node: Node):
    if node.right:
        return leftMost(node.right)
    
    parent = node.parent

    while parent and parent.left != node:
        node = parent
        parent = parent.parent

    return parent


if __name__ == '__main__':
    '''
        10
       /  \
      5    30
          /  \
         22    35
    '''
    root = Node (
        val = 10,
        left = Node(5),
        right = Node(30, Node(22), Node(35))
    )

    assert inorderSuccessor(root, root.right.left).val == 30

