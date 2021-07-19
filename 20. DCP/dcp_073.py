class Node:
    def __init__(self, key) -> None:
        self.key = key
        self._next = None
        self._prev = None


def printLL(node: Node):
    current = node
    while current:
        print(current.key, end=' -> ')
        current = current._next

    print('None')


def reverse(head: Node) -> Node:
    current = head
    prev = None

    while current:
        next = current._next
        current._next = prev
        prev = current
        current = next

    return prev


if __name__ == '__main__':
    head = Node(1)
    head._next = Node(2)
    head._next._next = Node(3)
    head._next._next._next = Node(4)
    head._next._next._next._next = Node(5)

    h = reverse(head)
    printLL(h)
