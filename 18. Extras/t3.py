# (n * nlogn)
def runningMedianBrute(nums: list):
    medians = []
    # [1, 2, 3] --> 3 // 2 = 1
    # [1, 2] --> 2 // 2 = 1

    for i in range(1, len(nums)+1):
        tmp = nums[:i]
        tmp.sort()

        if len(tmp) % 2 == 0:
            f, s = (len(tmp) // 2 - 1), (len(tmp) // 2)
            m = (tmp[f] + tmp[s]) / 2
        else:
            f = len(tmp) // 2
            m = tmp[f]

        medians.append(m)

    print(medians)

# -------------------------------------

from heapq import heappush, heappop

def rebalanceHeap(maxHeap, minHeap):
    if len(maxHeap) > len(minHeap) + 1:
        heappush(minHeap, -heappop(maxHeap))


def runningMedian(nums: list):
    medians = []
    minHeap, maxHeap = [], []

    for num in nums:
        heappush(maxHeap, -num)
        rebalanceHeap(maxHeap, minHeap)

        if len(maxHeap) - len(minHeap) == 1:
            medians.append(-maxHeap[0])
        else:
            f, s = -maxHeap[0], minHeap[0]
            medians.append((f + s) / 2)

    print(medians)



runningMedianBrute([7, 3, 5, 2])
runningMedian([7, 3, 5, 2, 1])



'''
7, 3, 5, 2, 1, -1

3      7
3 5    7
2, 3   5, 7

2, 1, 3   5, 7                  len(maxHeap) + 1 > len(minHeap)
-1, 1, 2   3, 5, 7  (2+3)/2         maxHeap pop --> add to minHeap


5, 3, 7, 6

-6 < -7

-7
-5
-6
-3

'''
