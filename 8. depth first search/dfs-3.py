'''
Sum of Path Numbers (medium)

Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.

Output: 408 Explanation: The sum of all path numbers: 17 + 192 + 199
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    return find_all_sum_recursive(root, 0)


def find_all_sum_recursive(currentNode, total_sum):
    if currentNode is None:
        return 0
    
    total_sum = 10 * total_sum + currentNode.val

    if currentNode.left is None and currentNode.right is None:
        return total_sum
    
    return find_all_sum_recursive(currentNode.left, total_sum) + find_all_sum_recursive(currentNode.right, total_sum)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
