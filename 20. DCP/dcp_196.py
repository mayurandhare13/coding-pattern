from collections import Counter


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def findFrequentTreeSum(root: TreeNode):
    counts = Counter()

    def dfs(node):
        if not node:
            return 0

        res = node.val + dfs(node.left) + dfs(node.right)
        counts[res] += 1

        return res

    dfs(root)

    return max(counts.items(), key = lambda x : x[1])[0]


if __name__ == '__main__':
    root = TreeNode(5, left=TreeNode(2), right=TreeNode(-5))
    assert findFrequentTreeSum(root) == 2    
