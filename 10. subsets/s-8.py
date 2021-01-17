'''
Structurally Unique Binary Search Trees (hard) #
Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "\nRT:" + str(self.val) + " L:" + str(self.left) + "  R:" + str(self.right)

def find_unique_trees(n):
    return find_unique_trees_handler(1, n)


def find_unique_trees_handler(start, end):
    result = []
    # base condition, return 'None' for an empty sub-tree
    # consider n = 1, in this case we will have start = end = 1, this means we should have only one tree
    # we will have two recursive calls, findUniqueTreesRecursive(1, 0) & (2, 1)
    # both of these should return 'None' for the left and the right child
    if start > end:
        result.append(None)
        return result
    
    for i in range(start, end+1):
        leftSubtrees = find_unique_trees_handler(start, i-1)
        rightSubtrees = find_unique_trees_handler(i+1, end)
        
        for leftTree in leftSubtrees:
            for rightTree in rightSubtrees:
                root = TreeNode(i)
                root.left = leftTree
                root.right = rightTree
                result.append(root)
    
    return result


if __name__ == "__main__":
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: ", find_unique_trees(3))
    print("Total trees: " + str(len(find_unique_trees(3))))
