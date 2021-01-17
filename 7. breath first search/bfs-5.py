'''
Minimum Depth of a Binary Tree (easy)

Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    if (root is None):
        return -1

    queue = deque()
    queue.append(root)
    minHeight = 0

    while (queue):
        minHeight += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()
            
            # check if it is a leaf node
            if not currentNode.left and not currentNode.right:
                return minHeight
            
            # otherwise insert childrens
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))



'''
Similar Problems #
Given a binary tree, find its maximum depth (or height).
traverse the whole tree. once queue is empty. you reach the end. Thats the maximum level
'''