import sys

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minSumPathHelper(node: Node, path, pathSum) -> list:
    subPath = path + [node.val]
    subPathSum = pathSum + node.val

    if not node.left and not node.right:
        return (subPath, subPathSum)

    leftPathSum, rightPathSum = sys.maxsize, sys.maxsize
    if node.left:
        leftPath, leftPathSum = minSumPathHelper(node.left, subPath, subPathSum)

    if node.right:
        rightPath, rightPathSum = minSumPathHelper(node.right, subPath, subPathSum)

    return (leftPath, leftPathSum) if leftPathSum < rightPathSum \
        else (rightPath, rightPathSum)


def minSumPath(root: Node):
    return minSumPathHelper(root, [], 0)[0]


if __name__ == '__main__':
    '''
         10
        /  \
       5    5
        \     \
         2    1
             /
           -1
    '''
    root = Node (
        val = 10,
        left = Node(5, right=Node(2)),
        right = Node(5, right=Node(1, left=Node(-1)))
    )

    assert minSumPath(root) == [10, 5, 1, -1]
