'''
K Pairs with Largest Sums (Hard) #

Given two sorted arrays in descending order, find 'K' pairs with the largest sum where each pair consists of numbers from both the arrays.

Input: L1=[5, 2, 1], L2=[2, -1], K=3
Output: [5, 2], [5, -1], [2, 2]
'''

from heapq import *


def find_k_largest_pairs(list1, list2, k):
    minHeap = []

    for i in range(0, min(k, len(list1))):
        for j in range(0, min(k, len(list2))):
            if len(minHeap) < k:
                heappush(minHeap, (list1[i] + list2[j], i, j))
            else:
                # sum of 2 numbers < smallest(top) from heap, then break
                # since, arrays are sorted descending
                # we will not have sum larger than top element from minHeap now onwards
                if list1[i] + list2[j] < minHeap[0][0]:
                    break
                else:
                    heappop(minHeap)
                    heappush(minHeap, (list1[i] + list2[j], i, j))
    
    result = []
    for (num, i, j) in minHeap:
        result.append([list1[i], list2[j]])
    
    return result


if __name__ == "__main__":
    print("Pair with largest sums: ", 
                find_k_largest_pairs([5, 2, 1], [2, -1], k=3))
    print("Pair with largest sums: ",
                find_k_largest_pairs([9, 8, 2], [6, 3, 1], k=3))
