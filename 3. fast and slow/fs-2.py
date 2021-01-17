'''
Start of LinkedList Cycle (medium)
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

time complexity O(N)
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_start(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            cycle_length = find_cycle_length(slow)
            break

    # return find_start(head, cycle_length)
    return find_cycle_start_node(head, slow)


def find_cycle_start_node(head, slow):
    current = head
    while current != slow:
        current = current.next
        slow = slow.next
    
    return current


def find_cycle_length(slow):
    current = slow.next
    cycle_length = 1
    while current is not slow:
        cycle_length += 1
        current = current.next
    
    return cycle_length


def find_start(head, cycle_length):
    pointer1, pointer2 = head, head
    while cycle_length > 0:
        pointer1 = pointer1.next
        cycle_length -= 1
    
    while pointer2 is not pointer1:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
