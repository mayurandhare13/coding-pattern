from sys import maxsize

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maxPathSum(root: Node):
    if not root:
        return (-maxsize, 0)
    
    leftMaxSum, leftPath = maxPathSum(root.left)
    rightMaxSum, rightPath = maxPathSum(root.right)

    # Calculates the maximum path through the root
    rootMaxSum = max(leftPath, 0) + root.val + max(rightPath, 0)

    # Find the maximum path, including or excluding the root
    maxSum = max(rootMaxSum, leftMaxSum, rightMaxSum)

    # Find the maximum path including and ending at the root
    rootPath = max(leftPath, rightPath, 0) + root.val

    return (maxSum, rootPath)


if __name__ == '__main__':

    a = Node(1)
    assert maxPathSum(a)[0] == 1

    b = Node(2)
    a.left = b
    assert maxPathSum(a)[0] == 3

    c = Node(3)
    a.right = c
    assert maxPathSum(a)[0] == 6

    a.val = -1
    assert maxPathSum(a)[0] == 4
