'''
All Paths for a Sum (medium)

Given a binary tree and a number 'S', find all paths from root-to-leaf such that the sum of all the node values of each path equals 'S'.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    find_paths_helper(root, sum, [], allPaths)
    return allPaths


def find_paths_helper(currentNode: TreeNode, sum, currentPath: list, allPaths: list):
    if currentNode is None:
        return
    
    currentPath.append(currentNode.val)
    
    if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        find_paths_helper(currentNode.left, sum - currentNode.val, currentPath, allPaths)
        find_paths_helper(currentNode.right, sum - currentNode.val, currentPath, allPaths)
    
    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    currentPath.pop()


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))



'''
As we know that there can't be more than N/2 leaves in a binary tree, therefore the maximum number of elements in allPaths will be O(N/2)=O(N). 
Now, each of these paths can have many nodes in them. For a balanced binary tree (like above), each leaf node will be at maximum depth. As we know that the depth (or height) of a balanced binary tree is O(logN) we can say that, at the most, each path can have logN nodes in it. This means that the total size of the allPaths list will be O(N*logN). If the tree is not balanced, we will still have the same worst-case space complexity.

So, the overall space complexity of our algorithm is O(N*logN).

----

Problem 1: Given a binary tree, return all root-to-leaf paths.

Solution: We can follow a similar approach. We just need to remove the “check for the path sum”.

Problem 2: Given a binary tree, find the root-to-leaf path with the maximum sum.

Solution: We need to find the path with the maximum sum. As we traverse all paths, we can keep track of the path with the maximum sum.
'''