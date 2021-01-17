'''
Sliding Window Median (hard)

Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
'''

from heapq import *
import heapq

class SlidingWindowMedian:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)]
        
        for i in range(len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.rebalanceHeap()

            # if we have at least 'k' elements in the sliding window
            if (i - k + 1 >= 0):
                # add median to list
                if len(self.maxHeap) == len(self.minHeap):
                    result[i - k + 1] = (-self.maxHeap[0] + self.minHeap[0]) / 2.0
                else:
                    result[i - k + 1] = -self.maxHeap[0] / 1.0

                # remove element which will go Out Of Scope/Window
                elementToRemove = nums[i - k + 1]
                if (elementToRemove <= -self.maxHeap[0]):
                    self.remove(self.maxHeap, -elementToRemove)
                else:
                    self.remove(self.minHeap, elementToRemove)
                
                self.rebalanceHeap()

        return result


    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]
        # we can use heapify to re-adjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if (ind < len(heap)):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)


    def rebalanceHeap(self):
        # max-heap can have atmost 1 element more than min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))

        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))


if __name__ == "__main__":

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))
