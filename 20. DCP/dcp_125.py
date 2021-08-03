class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchPair(root: Node, total):
    def inorder(node: Node):
        if node is None:
            return
        inorder(node.left)
        arr.append(node.val)
        inorder(node.right)

    arr = []
    inorder(root)

    l, r = 0, len(arr) - 1
    while l < r:
        left, right = arr[l], arr[r]
        _sum = left + right
        if _sum == total:
            return [left, right]
        
        elif _sum > total:
            r -= 1

        else:
            l += 1

    return [-1, -1]


if __name__ == '__main__':
    """
          10
        /   \
       5    15
            /  \
          11    15
    """
    root = Node (
        val = 10,
        left = Node(5),
        right = Node(15, Node(11), Node(15))
    )

    assert searchPair(root, 20) == [5, 15]
