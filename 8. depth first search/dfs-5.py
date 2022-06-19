'''
Count Paths for a Sum (medium)

Given a binary tree and a number 'S', find all paths in the tree such that the sum of all the node values of each path equals 'S'. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count_paths_helper(root, S, [])


def count_paths_helper(currentNode, S, currentPath):
    if currentNode is None:
        return 0
    
    # add currentNode to the path
    currentPath.append(currentNode.val)

    # find all sum of sub_path in currentPath list
    pathSum, pathCount = 0, 0
    for i in range(len(currentPath)-1, -1, -1):
        pathSum += currentPath[i]

        if pathSum == S:
            pathCount += 1

    pathCount += count_paths_helper(currentNode.left, S, currentPath)
    pathCount += count_paths_helper(currentNode.right, S, currentPath)

    # remove the current node from the path to backtrack
    # we need to remove the current node while we are going up the recursive call stack
    del currentPath[-1] # currentPath.pop()

    return pathCount


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))



'''
The time complexity of the above algorithm is O(N^2) in the worst case (skew tree / linked list), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once, but for every node, we iterate the current path.
Balanced Tree -> O(NlogN) if the tree is balanced, then the current path will be equal to the height of the tree
'''