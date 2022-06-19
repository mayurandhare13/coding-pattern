'''
Top 'K' Frequent Numbers (medium)

Given an unsorted array of numbers, find the top 'K' frequently occurring numbers in it.

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
'''

from heapq import *

def find_k_frequent_numbers(nums, k):
    
    # calc frequency of each number
    numsFrequencyMap = {}
    for num in nums:
        numsFrequencyMap[num] = numsFrequencyMap.get(num, 0) + 1
    
    # go through all numbers of numFrequencyMap and push them in minHeap, which will have
    # top K numbers. If heap size > K, we remove smallest(top) number

    minHeap = []
    for num, freq in numsFrequencyMap.items():
        heappush(minHeap, (freq, num))
        if len(minHeap) > k:
            heappop(minHeap)

    topNumbers = []
    while minHeap:
        topNumbers.append(heappop(minHeap)[1])

    return topNumbers


if __name__ == "__main__":
    print(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], k = 2))
    print(find_k_frequent_numbers([5, 12, 11, 3, 11], k = 2))
