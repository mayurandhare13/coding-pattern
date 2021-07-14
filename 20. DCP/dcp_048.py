# preorder: visit - left - right
# inorder: left - visit - right

'''
Consider this input:

preorder: [1, 2, 4, 5, 3, 6]
inorder: [4, 2, 5, 1, 6, 3]
The obvious way to build the tree is:

Use the first element of preorder, the 1, as root.
Search it in inorder.
Split inorder by it, here into [4, 2, 5] and [6, 3].
Split the rest of preorder into two parts as large as the inorder parts, here into [2, 4, 5] and [3, 6].
Use preorder = [2, 4, 5] and inorder = [4, 2, 5] to add the left subtree.
Use preorder = [3, 6] and inorder = [6, 3] to add the right subtree.
'''

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# O(n^2)
def buildTree(inOrder: list, preOrder: list):
    if inOrder:
        rootVal = preOrder.pop(0)
        root = Node(rootVal)

        idx = inOrder.index(rootVal)
        
        root.left = buildTree(inOrder[0:idx], preOrder)
        root.right = buildTree(inOrder[idx+1:], preOrder)

        return root


# ---------------------------------------------------------------------
def buildTreeOptimized(inorder: list, preorder: list) -> Node:

    def listToTree(left, right):
        if left > right:
            return None
        
        nonlocal preOrderIndex

        rootVal = preorder[preOrderIndex]
        root = Node(rootVal)

        preOrderIndex += 1

        root.left = listToTree(left, inOrderIndexMap[rootVal] - 1)
        root.right = listToTree(inOrderIndexMap[rootVal] + 1, right)

        return root


    preOrderIndex = 0
    inOrderIndexMap = {}
    for idx, val in enumerate(inorder):
        inOrderIndexMap[val] = idx

    return listToTree(0, len(inorder)-1)



def printInOrder(root: Node):
    if root is None:
        return
    
    printInOrder(root.left)
    print(root.val, end=' ')
    printInOrder(root.right)


if __name__ == '__main__':

    inOrder = ['D', 'B', 'E', 'A', 'F', 'C', 'G']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    root = buildTree(inOrder, preOrder)
    printInOrder(root)
    print()

    inOrder = ['D', 'B', 'E', 'A', 'F', 'C', 'G']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    root = buildTreeOptimized(inOrder, preOrder)
    printInOrder(root)
    print()
