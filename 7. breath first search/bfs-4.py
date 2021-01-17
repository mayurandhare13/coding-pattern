'''
Level Averages in a Binary Tree (easy)
Given a binary tree, populate an array to represent the averages of all of its levels.
'''

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if (root is None):
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        _sum = 0.0
        for _ in range(levelSize):
            currentNode = queue.popleft()
            _sum += currentNode.val
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.append(_sum / levelSize)

    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


'''
Similar Problems #
Find the largest value on each level of a binary tree.
'''