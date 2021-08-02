from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderTraversal(root: Node) -> list:
    order = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        order.append(node.val)

        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)

    return order


if __name__ == '__main__':
    root = Node(1, Node(2), Node(3, Node(4), Node(5)))
    assert levelOrderTraversal(root) == [1, 2, 3, 4, 5]
