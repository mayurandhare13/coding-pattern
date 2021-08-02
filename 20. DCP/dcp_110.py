class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getAllPaths(node: Node):
    if not node:
        return []
    
    nodePaths = []
    leftPaths = getAllPaths(node.left)
    for path in leftPaths:
        nodePaths.append([node.val] + path)

    rightPaths = getAllPaths(node.right)
    for path in rightPaths:
        nodePaths.append([node.val] + path)

    return nodePaths if nodePaths else [[node.val]]


if __name__ == '__main__':
    root = Node(1, Node(2), Node(3, Node(4), Node(5)))
    assert getAllPaths(root) == [[1, 2], [1, 3, 4], [1, 3, 5]]
