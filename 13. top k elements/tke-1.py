'''
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]

O(K∗logK + (N−K)∗logK), which is asymptotically equal to O(N∗logK)
'''

from heapq import *

def find_k_largest_numbers(nums, k):
    minHeap = []

    # push k elements in Min Heap
    for i in range(k):
        heappush(minHeap, nums[i])

    # iterate over remaining elements
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    
    print(minHeap[0])   # returns K'th largest number
    # minHeap will only have K elements
    return list(minHeap)


if __name__ == "__main__":
    print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
    print(find_k_largest_numbers([5, 12, 11, -1, 12], 2))
