'''
Kth Smallest Number (easy)

Given an unsorted array of numbers, find Kth smallest number in it.

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2]
'''

'''
[1, 5, 12], 3rd smallest = 12
if we maintain maxHeap then at root element we have largest element. (if next is 70)
if we maintain minHeap then root will be smallest element, then we have to pop elements in the end till we find kth smallest

maintain maxHeap will `-ve` numbers. then -12 at root, if next is 70 -> -70, if (-70 > -12) then insert. but actually (-70 < -12).
so we always have kth smallest at root. O(1)

ALL OF THIS JUST TO RETRIEVE Kth SMALLEST AT ROOT
'''

from heapq import *

def find_kth_smallest_number(nums, k):
    maxHeap = []

    for i in range(k):
        heappush(maxHeap, -nums[i])

    
    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]: # (-2 > -12)
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])

    return -maxHeap[0]


if __name__ == "__main__":
    print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3))
    print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4))
    print(find_kth_smallest_number([5, 12, 11, -1, 12], 3))
