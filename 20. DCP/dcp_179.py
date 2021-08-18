class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "{} => (l: {}, r: {})".format(
            self.val, self.left, self.right)


def reconstruct(seqs: list):
    head = Node(seqs[-1])

    if len(seqs) == 1:
        return head

    # find first greater val for right subtree
    for i in range(len(seqs) - 1):
        if seqs[i] > head.val:
            breakPoint = i
            break
    
    leq = seqs[ : breakPoint]
    gt = seqs[breakPoint : -1]
    head.left = reconstruct(leq) if leq else None
    head.right = reconstruct(gt) if gt else None

    return head


if __name__ == '__main__':
    tree = reconstruct([2, 4, 3, 8, 7, 5])
    assert tree.val == 5
    assert tree.left.val == 3
    assert tree.right.val == 7
    assert tree.left.left.val == 2
    assert tree.left.right.val == 4
    assert tree.right.right.val == 8
