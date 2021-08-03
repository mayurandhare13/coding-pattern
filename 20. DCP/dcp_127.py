class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

#  O(max(m, n)) time
def add(n1: Node = None, n2: Node = None, carry = 0):
    if not n1 and not n2 and carry == 0:
        return None

    n1Val = n1.val if n1 else 0
    n2Val = n2.val if n2 else 0

    total = n1Val + n2Val + carry

    n1Next = n1.next if n1 else None
    n2Next = n2.next if n2 else None

    carryNext = 1 if total >= 10 else 0

    return Node(total % 10, add(n1Next, n2Next, carryNext))


if __name__ == '__main__':
    n1 = Node(9, Node(9))
    n2 = Node(5, Node(2))

    r = add(n1, n2) # `4 -> 2 -> 1`

    current = r
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print(None)
