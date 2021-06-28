from heapq import heappush, heappop


def rebalanceHeap(minHeap, maxHeap):
    # max-heap can have atmost 1 element more than min-heap
    if len(maxHeap) > len(minHeap) + 1:
        heappush(minHeap, -heappop(maxHeap))
    
    elif len(maxHeap) < len(minHeap):
        heappush(maxHeap, -heappop(minHeap))


def runningMedian(nums: list) -> list:
    # Max Heap --> elements < median
    # Min Heap --> elements > median
    minHeap, maxHeap = [], []

    medians = []

    for num in nums:
        if not maxHeap or num <= -maxHeap[0]:
            heappush(maxHeap, -num)
        else:
            heappush(minHeap, num)
        
        rebalanceHeap(minHeap, maxHeap)

        if len(maxHeap) == len(minHeap):
            medians.append((-maxHeap[0] + minHeap[0]) / 2)
        else:
            medians.append(-maxHeap[0])
    
    return medians


if __name__ == '__main__':
    assert runningMedian([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2.0, 2]
    assert runningMedian([3, 3, 3, 3]) == [3, 3, 3, 3]