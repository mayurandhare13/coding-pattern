from sys import maxsize

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def largestBstSubtree(root: Node):
    maxLen = 0
    maxRoot = None

    def helper(root: Node):
        nonlocal maxLen
        nonlocal maxRoot

        if root is None:
            return (0, maxsize, -maxsize)

        left = helper(root.left)
        right = helper(root.right)

        if left[2] < root.val and root.val < right[1]:
            localLen = left[0] + right[0] + 1
            if localLen > maxLen:
                maxLen = localLen
                maxRoot = root

            return (localLen, min(root.val, left[1]), max(root.val, right[2]))

        else:
            return (0, -maxsize, maxsize)


    helper(root)
    return maxRoot


if __name__ == '__main__':

    a = Node(1)
    b = Node(2)
    c = Node(6)
    d = Node(1)
    e = Node(3)
    f = Node(4)
    g = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    assert largestBstSubtree(a) == b
