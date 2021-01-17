'''
Reverse Level Order Traversal (easy)

Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    
    # here we use deque to append the current element list at the beginning
    result = deque()
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        levelElements = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            levelElements.append(currentNode.val)
            
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        
        result.appendleft(levelElements)

    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))
