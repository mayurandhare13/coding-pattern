'''
Path With Given Sequence (medium)

Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    return find_path_helper(root, sequence, 0)


def find_path_helper(currentNode, sequence, index):
    if currentNode is None:
        return False

    seqLen = len(sequence)
    if index >= seqLen or currentNode.val != sequence[index]:
        return False
    
    if currentNode.left is None and currentNode.right is None and index == seqLen - 1:
        return True

    return find_path_helper(currentNode.left, sequence, index+1) or \
            find_path_helper(currentNode.right, sequence, index+1)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
