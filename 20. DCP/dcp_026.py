class Node:
    def __init__(self, val):
        self.val = val
        self._next = None

    def __repr__(self) -> str:
        current = self
        returnList = ''
        while current:
            returnList += str(current.val) + ' '
            current = current._next
        
        return returnList


def removeKthElementFromLast(head: Node, k: int) -> Node:
    # corner case
    # dummy head needed if head node is going to be deleted
    dummy = Node(0)
    dummy._next = head
    current, runner = dummy, dummy

    while k >= 0:
        runner = runner._next
        k -= 1

    while runner:
        runner = runner._next
        current = current._next
    
    current._next = current._next._next

    return dummy._next


if __name__ == '__main__':
    head = Node(1)
    head._next = Node(2)
    head._next._next = Node(3)
    head._next._next._next = Node(4)
    head._next._next._next._next = Node(5)

    head = removeKthElementFromLast(head, 4)
    print(head) # 1 3 4 5
