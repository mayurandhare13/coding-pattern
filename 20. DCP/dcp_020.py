class Node:
    def __init__(self, val) -> None:
        self.val = val
        self._next = None


def length(node: Node) -> int:
    size = 1
    current = node
    while current:
        size += 1
        current = current._next
    
    return size


def intersectingNode(l1: Node, l2: Node) -> Node:
    l1Size = length(l1)
    l2Size = length(l2)

    # get the difference between ll
    # make both ll same by moving bigger list pointer
    k = abs(l1Size - l2Size)
    if l1Size > l2Size:
        while k > 0:
            l1 = l1._next
            k -= 1
    
    elif l2Size > l1Size:
        while k > 0:
            l2 = l2._next
            k -= 1
    
    while l1 and l2:
        # as per que: l1.val == l2.val
        if l1 == l2:
            return l1
        l1 = l1._next
        l2 = l2._next
    
    return Node(-1)


if __name__ == '__main__':
    l1 = Node(3)
    l1._next = Node(7)
    l1._next._next = Node(8)
    l1._next._next._next = Node(10)

    l2 = Node(99)
    l2._next = Node(1)
    # l2._next._next = Node(8)
    # l2._next._next._next = Node(10)
    l2._next._next = l1._next._next
    assert intersectingNode(l1, l2).val == 8

    l1 = l1._next
    assert intersectingNode(l1, l2).val == 8
