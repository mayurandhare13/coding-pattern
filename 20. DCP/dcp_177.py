class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def printList(self):
        temp = self
        while temp is not None:
            print(temp.value, end=' -> ')
            temp = temp.next
        print('None')


def rotate(head: Node, rotations) -> Node:
    if head is None or head.next is None or rotations <= 0:
        return head
    
    last = head
    listLength = 1
    while last.next is not None:
        listLength += 1
        last = last.next
    
    # attach last node to head (make it circular ll)
    last.next = head

    rotations = rotations % listLength

    # (-1) to set the next node head
    skips = listLength - rotations - 1
    lastNodeRotatedList = head
    while skips > 0:
        lastNodeRotatedList = lastNodeRotatedList.next
        skips -= 1
    
    head = lastNodeRotatedList.next
    lastNodeRotatedList.next = None

    return head


if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print("Nodes of original LinkedList are: ", end='')
    head.printList()
    rotations = 3
    print("rotations: ", rotations)
    newHead = rotate(head, rotations)
    print("Nodes of rotated LinkedList are: ", end='')
    newHead.printList()

