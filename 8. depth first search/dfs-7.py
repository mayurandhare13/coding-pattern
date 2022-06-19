'''
Path with Maximum Sum (hard) #
Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum. A path can be defined as a sequence of nodes between any two nodes and doesn't necessarily pass through the root.
'''

import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxPathSum:
    def __init__(self):
        self.global_max_sum = -math.inf

    def find_maximum_path_sum(self, root):
        self.find_maximum_path_sum_handler(root)
        return self.global_max_sum

    def find_maximum_path_sum_handler(self, currentNode):
        if currentNode is None:
            return 0
        
        leftPathSum = self.find_maximum_path_sum_handler(currentNode.left)
        rightPathSum = self.find_maximum_path_sum_handler(currentNode.right)
        
        # ignore paths with negative sums, since we need to find the maximum sum we should
        # ignore any path which has an overall negative sum.
        leftPathSum = max(leftPathSum, 0)
        rightPathSum = max(rightPathSum, 0)

        localMaxSum = leftPathSum + rightPathSum + currentNode.val
        self.global_max_sum = max(self.global_max_sum, localMaxSum)

        return max(leftPathSum, rightPathSum) + currentNode.val


if __name__ == "__main__":
    maxSum = MaxPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("Maximum Path Sum: " + str(maxSum.find_maximum_path_sum(root)))
    
    maxSum = MaxPathSum()
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maxSum.find_maximum_path_sum(root)))

    maxSum = MaxPathSum()
    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(maxSum.find_maximum_path_sum(root)))
