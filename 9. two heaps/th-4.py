'''
Next Interval (hard) #

Given an array of intervals, find the next interval of each interval. In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

Write a function to return an array containing indices of the next interval of each input interval. If there is no next interval of a given interval, return -1. It is given that none of the intervals have the same start point.

Input: Intervals [[3,4], [1,5], [4,6]]
Output: [2, -1, -1]
Explanation: The next interval of [3,4] is [4,6] which has index ‘2’. There is no next interval for [1,5] and [4,6].
'''

from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    n = len(intervals)
    # heaps for finding the maximum start and end
    maxStartHeap, maxEndHeap = [], []
    result = [0 for _ in range(n)]

    for endIdx in range(n):
        heappush(maxStartHeap, (-intervals[endIdx].start, endIdx))
        heappush(maxEndHeap, (-intervals[endIdx].end, endIdx))

    for _ in range(n):
        topEnd, endIndex = heappop(maxEndHeap)
        result[endIndex] = -1

        if -maxStartHeap[0][0] >= -topEnd:
            topStart, startIndex = heappop(maxStartHeap)

            while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
            
            result[endIndex] = startIndex
            
            # put the interval back as it could be the next interval of other intervals
            heappush(maxStartHeap, (topStart, startIndex))

    return result


if __name__ == "__main__":

    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))
