'''
Sum of Elements (medium)

Given an array, find the sum of all numbers between the K1'th and K2'th smallest elements of that array.

Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
between 5 and 15 is 23 (11+12).
'''

from heapq import *


def find_sum_of_elements(nums, k1, k2):
    minHeap = []

    # insert all elements in minHeap
    for num in nums:
        heappush(minHeap, num)

    # remove first k1 smallest elements from heap
    for _ in range(k1):
        heappop(minHeap)

    elementSum = 0
    for _ in range(k2 - k1 - 1):
        elementSum += heappop(minHeap)

    return elementSum


if __name__ == "__main__":
    print(find_sum_of_elements([1, 3, 12, 5, 15, 11], k1=3, k2=6))
    print(find_sum_of_elements([3, 5, 8, 7], k1=1, k2=4))
