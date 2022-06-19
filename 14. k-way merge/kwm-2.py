'''
Kth Smallest Number in M Sorted Lists

Given 'M' sorted arrays, find the K'th smallest number among all the arrays.
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
'''

from heapq import *


def find_Kth_smallest(lists, k):
    minHeap = []

    # put the 1st element from each list in min heap
    for lst in lists:
        heappush(minHeap, (lst[0], 0, lst))

    numberCount, number = 0, 0
    while minHeap:
        number, idx, lst = heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            break
        
        # if the array of top element has more element 
        # add next element to the min heap
        if len(lst) > idx + 1:
            heappush(minHeap, (lst[idx+1], idx+1, lst))

    return number


if __name__ == "__main__":
    print(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], k=5))
