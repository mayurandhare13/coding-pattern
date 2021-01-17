'''
Palindrome LinkedList (medium) #
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
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


def is_palindromic_linked_list(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    
    reverse_second_half = reverse(slow)

    head_second_half = reverse_second_half
    current = head
    
    while current is not None and head_second_half is not None:
        if current.value != head_second_half.value:
            return False
        current = current.next
        head_second_half = head_second_half.next

    reverse(reverse_second_half)

    return True


def reverse(head):
    prev = None
    while head is not None:
        _next = head.next
        head.next = prev
        prev = head
        head = _next
    return prev


if __name__ == "__main__":
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))
