from collections import defaultdict
from queue import Queue
import queue


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minLevelSum(root: Node):
    queue = Queue()
    queue.put((root, 0))
    levelSum = defaultdict(int)

    while not queue.empty():
        node, level = queue.get()
        levelSum[level] += node.val

        if node.left:
            queue.put((node.left, level + 1))
        
        if node.right:
            queue.put((node.right, level + 1))
    
    return min(levelSum, key=levelSum.get)


if __name__ == '__main__':
    """
         1
       /  \
     -2   -3            (level 1 is the minimum)
         /  \
        4   -5
    """
    root = Node (
        val = 1,
        left = Node(-2),
        right = Node(-3, Node(4), Node(-5))
    )

    assert minLevelSum(root) == 1

    #--------------------------

    """
            1
        /       \
        2          3
    /  \          \
    4    5          6
        \       /   \
        -1   -7     -8   (level 3 is the minimum)

    """
    root = Node(
        val = 1,
        left = Node(2, Node(4), Node(5, Node(-1))),
        right = Node(
            val = 3,
            right = Node(6, Node(-7), Node(-8))
        )
    )

    assert minLevelSum(root) == 3
