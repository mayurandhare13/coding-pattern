class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


def getValues(node: Node):
    while node:
        yield node.val
        node = node.next


def isPalindrome(node: Node):
    values = getValues(node)                            # generator
    valuesReversed = reversed(list(getValues(node)))    # list_reverseiterator

    return all(x == y for x, y in zip(values, valuesReversed))


#--------------------------------------------------------------

def reverse(node: Node) -> Node:
    prev = None
    while node:
        _next = node.next
        node.next = prev
        prev = node
        node = _next

    return prev


def isPalindrome2(head: Node):
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    reverseHead = reverse(slow)
    reverseHalf = reverseHead
    current = head

    while current and reverseHalf:
        if current.val != reverseHalf.val:
            return False
        current = current.next
        reverseHalf = reverseHalf.next
    
    reverse(reverseHead)
    return True


if __name__ == '__main__':
    a = Node('1')
    b = Node('4')
    c = Node('3')
    d = Node('4')
    e = Node('1')

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    assert isPalindrome2(a)

    m = Node('8')
    n = Node('9')
    m.next = n
    assert not isPalindrome2(m)
