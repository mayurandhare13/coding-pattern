'''
Kth Largest Number in a Stream (medium)

Design a class to efficiently find the Kth largest element in a stream of numbers.
The class should have the following two things:
- The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
- The class should expose a function add(int num) which will store the given number and return the Kth largest number.

Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.
'''


from heapq import *


class KthLargestNumberInStream:
    minHeap = []

    def __init__(self, nums, k):
        self.k = k
        for n in nums:
            self.add(n)
    
    def add(self, num):
        # add number to the minHeap
        heappush(self.minHeap, num)

        # if heap has > k numbers, remove one number
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        
        # return kth largest number
        return self.minHeap[0]


if __name__ == "__main__":
   kthLargestNumberInStreamObj = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], k = 4)
   print(kthLargestNumberInStreamObj.add(6))
   print(kthLargestNumberInStreamObj.add(13))
   print(kthLargestNumberInStreamObj.add(4))



# when asked KthSmallest, change num -> -num in heap