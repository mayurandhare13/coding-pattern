'''
Rearrange a LinkedList (medium) #
Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    if head is None and head.next is None:
        return
    
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    
    head_second_half = reverse(slow)
    head_first_half = head
    
    while head_second_half is not None and head_first_half is not None:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp
    
    # set the next of the last node to 'None'
    if head_first_half is not None:
        head_first_half.next = None


def reverse(head):
    prev = None
    while (head is not None):
        _next = head.next
        head.next = prev
        prev = head
        head = _next
    
    return prev


if __name__ == "__main__":
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    
    print("original: ")
    head.print_list()
    
    reorder(head)
    head.print_list()
