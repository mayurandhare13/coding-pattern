'''
         1
        / \
       2   3
      / \  / \
     4  5  6  7

[
    [1],
    [2, 3],
    [4, 5, 6, 7]
]


[1, 2, 3, 4, 5, 6, 7. .....]

'''

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# [[1], [2, 3], [5, 4, 7, 6]]
# [[1], [3, 2], [6, 7, 4, 5]]


def swap(node: Node, K=2, level=1):
    if not node:
        return None
    
    l, r = node.left, node.right
    if level % K != 0:
        node.left = swap(r, K, level+1)
        node.right = swap(l, K, level+1)
    else:
        node.left = swap(l, K, level+1)
        node.right = swap(r, K, level+1)

    return node


def levelTraversal(root: Node) -> list:
    order = deque()

    que = deque()
    que.append(root)

    while que:
        size = len(que)
        levelOrder = []
        while size > 0:
            node = que.popleft()
            levelOrder.append(node.val)

            if node.left:
                que.append(node.left)

            if node.right:
                que.append(node.right)
            
            size -= 1
        
        # order.appendleft(levelOrder)
        order.append(levelOrder)
    
    return list(order)


if __name__ == '__main__':
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(levelTraversal(root))

    r1 = swap(root)
    print(levelTraversal(r1))















