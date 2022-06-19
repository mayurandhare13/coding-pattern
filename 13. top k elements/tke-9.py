'''
Maximum Distinct Elements (medium)

Given an array of numbers and a number 'K', we need to remove 'K' numbers from the array such that we are left with maximum distinct numbers.

Input: [7, 3, 5, 8, 5, 3, 3], and K=2
Output: 3
Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have 
to skip 5 because it is not distinct and occurred twice. 
Another solution could be to remove one instance of '5' and '3' each to be left with three 
distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.
'''

from heapq import *


def find_maximum_distinct_elements(nums, k):
    distinctElementsCount = 0
    if len(nums) <= k:
        return distinctElementsCount

    # find frequency of each number
    numFrequencyMap = {}
    for i in nums:
        numFrequencyMap[i] = numFrequencyMap.get(i, 0) + 1
    
    # insert all the numbers with frequcency > 1 into minHeap
    minHeap = []
    for num, freq in numFrequencyMap.items():
        if freq == 1:
            distinctElementsCount += 1
        else:
            heappush(minHeap, (freq, num))
    
    # following greedy approach, try removing the least frequent numbers first from minHeap
    while k > 0 and minHeap:
        freq, num = heappop(minHeap)

        # to make element distinct, we need to remove all duplicate
        k -= freq - 1
        if k >= 0:
            distinctElementsCount += 1
    
    # if k > 0, then we need to remove remaining distinct element
    if k > 0:
        distinctElementsCount -= k
    return distinctElementsCount


if __name__ == "__main__":
    print(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], k=2))
    print(find_maximum_distinct_elements([3, 5, 12, 11, 12], k=3))
    print(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], k=2))
