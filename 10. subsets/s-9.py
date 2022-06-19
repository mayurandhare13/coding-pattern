'''
Count of Structurally Unique Binary Search Trees (hard) #

Given a number 'n', write a function to return the count of structurally unique Binary Search Trees (BST) that can store values 1 to 'n'.
Catalan number problem

Input: 3
Output: 5
Explanation: There will be 5 unique BSTs that can store numbers from 1 to 5.

Estimated time complexity will be O(n*2^n) but the actual time complexity O(4^n/√n) is bounded by the Catalan number 
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_trees(n):
    if n <= 1:
        return 1
    
    count = 0
    for i in range(1, n+1):
        countLeftSubtrees = count_trees(i - 1)
        countRightSubtrees = count_trees(n - i)
        count += (countLeftSubtrees * countRightSubtrees)
    
    return count


if __name__ == "__main__":
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))
