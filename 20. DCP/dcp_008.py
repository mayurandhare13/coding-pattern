class Node:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def univalHelper(node: Node, value: int):
    if node is None:
        return True
    if node.val == value:
        return univalHelper(node.left, value) and univalHelper(node.right, value)
    
    return False


def isUnival(root: Node):
    return univalHelper(root, root.val)


# O(n^2)
def countUnivalTrees(root: Node):
    if root is None:
        return 0

    lCount = countUnivalTrees(root.left)
    rCount = countUnivalTrees(root.right)

    return 1 + lCount + rCount if isUnival(root) else lCount + rCount


def helper(root: Node) -> tuple:
    if root is None:
        return 0, True

    lCount, isLeftUnival = helper(root.left)
    rCount, isRightUnival = helper(root.right)
    total = lCount + rCount

    if isLeftUnival and isRightUnival:
        if root.left is not None and root.val != root.left.val:
            return total, False
        if root.right is not None and root.val != root.right.val:
            return total, False

        return 1 + total, True

    return total, False


# O(n)
def countUnivalTrees2(root: Node):
    count, _ = helper(root)
    return count


if __name__ == '__main__':
    r = Node(0)
    r.left = Node(1)
    r.right = Node(0)
    r.right.left = Node(1)
    r.right.left.left = Node(1)
    r.right.left.right = Node(1)
    r.right.right = Node(0)

    assert countUnivalTrees(r) == 5
    assert countUnivalTrees2(r) == 5
