'''
Kth Smallest Number in a Sorted Matrix (Hard)

Given an N∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
'''

from heapq import *

def find_Kth_smallest(matrix, k):
    minHeap = []
    
    # put 1st element of each row in min heap
    # we don't need to put more than k element in the heap
    for i in range(min(k, len(matrix))):
        heappush(minHeap, (matrix[i][0], 0, matrix[i]))

    numberCount, number = 0, 0
    while minHeap:
        number, idx, row = heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            break

        if len(row) > idx + 1:
            heappush(minHeap, (row[idx+1], idx+1, row))
    
    return number


if __name__ == "__main__":
    print("Kth smallest number is: ", 
                        find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], k=5))
