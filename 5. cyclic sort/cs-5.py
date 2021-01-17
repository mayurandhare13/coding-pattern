'''
Same cs-4.py problem
Solve without modifying array. if array has duplicate element multiple times. and find first duplicate.
'''

def find_start(arr, cycleLength):
    ptr1, ptr2 = arr[0], arr[0]
    # move ptr2 ahead of cycleLength (i.e. slow pointer)
    while cycleLength > 0:
        ptr2 = arr[ptr2]
        cycleLength -= 1
    
    # increment both pointers until they meet at the start of the cycle
    while ptr1 != ptr2:
        ptr1 = arr[ptr1]
        ptr2 = arr[ptr2]

    return ptr1


def find_duplicate(arr):
    
    # find duplicate element
    slow, fast = arr[0], arr[arr[0]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    # find cycle length
    current = arr[slow] # slow or fast => its same here
    cycleLength = 1
    while current != slow:
        current = arr[current]
        cycleLength += 1
    
    return find_start(arr, cycleLength)


if __name__ == "__main__":
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))
