class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head = head
    

    def getMiddle(self, h):
        if h is None:
            return h
        
        slow = h
        fast = h

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


    def merge(self, a, b):
        if a is None:
            return b
        
        if b is None:
            return a
        
        result = None
        if a.val <= b.val:
            result = a
            result.next = self.merge(a.next, b)
        else:
            result = b
            result.next = self.merge(a, b.next)

        return result


    def mergeSort(self, h: Node):
        if h is None or h.next is None:
            return h
        
        middle = self.getMiddle(h)
        nextToMiddle = middle.next
        middle.next = None

        left = self.mergeSort(h)
        right = self.mergeSort(nextToMiddle)

        sortedList = self.merge(left, right)

        return sortedList


def printList(head):
    if head is None:
        print(' ')
        return

    curr = head
    while curr:
        print(f"{curr.val}", end = " -> ")
        curr = curr.next
    
    print('None')


if __name__ == '__main__':
    head = Node(4, Node(1, Node(-3, Node(99))))
    ll = LinkedList(head)
    newHead = ll.mergeSort(head)
    printList(newHead) # -3 -> 1 -> 4 -> 99 -> None
