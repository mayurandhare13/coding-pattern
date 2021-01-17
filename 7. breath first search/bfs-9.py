'''
Right View of a Binary Tree (easy) #

Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            currentNode = queue.popleft()
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

            # if it is the last node of this level, add it to the result
            if i == levelSize - 1:
                result.append(currentNode.val)

    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ", end='')
    for node in result:
        print(str(node), " ", end='')
