'''
Smallest Number Range (Hard)
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
'''

from heapq import *
import math

def find_smallest_range(lists):
    minHeap = []
    rangeStart, rangeEnd = 0, math.inf
    currentMaxNumber = -math.inf

    # put 1st number from each list into min heap
    for lst in lists:
        heappush(minHeap, (lst[0], 0, lst))
        currentMaxNumber = max(currentMaxNumber, lst[0])

    # take the smallest(top) element from min heap, if it gives smaller range then update it
    # if list of top element has more element, then insert the next element in min heap
    while len(minHeap) == len(lists):
        num, i, lst = heappop(minHeap)
        if rangeEnd - rangeStart > currentMaxNumber - num:
            rangeStart = num
            rangeEnd = currentMaxNumber
        
        if len(lst) > i + 1:
            heappush(minHeap, (lst[i+1], i+1, lst))
            currentMaxNumber = max(currentMaxNumber, lst[i+1])

    return [rangeStart, rangeEnd]


if __name__ == "__main__":
    print("smallest range is: ", 
            find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]]))

    print("smallest range is: ",
            find_smallest_range([[1, 9], [4, 12], [7, 10, 16]]))
