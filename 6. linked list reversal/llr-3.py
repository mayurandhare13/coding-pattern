'''
Reverse every K-element Sub-list (medium)

Given the head of a LinkedList and a number 'k', reverse every 'k' sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than 'k' elements, reverse it too.
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    current, previous = head, None

    while True:
        last_node_of_previous_part = previous
        last_node_of_sub_list = current        # after reversing the LinkedList 'current' will become the last node of the sub-list

        _next = None
        i = 0
        while current is not None and i < k:
            _next = current.next
            current.next = previous
            previous = current
            current = _next
            i += 1
        
        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous
        
        # connect with the next part
        last_node_of_sub_list.next = current

        if current is None:
            break

        previous = last_node_of_sub_list

    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
