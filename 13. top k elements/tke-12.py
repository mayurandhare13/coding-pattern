'''
Rearrange String K Distance Apart (hard) #

Given a string and a number 'K', find if the string can be rearranged such that the same characters are at least 'K' distance apart from each other.

Input: "mmpp", K=2
Output: "mpmp" or "pmpm"
Explanation: All same characters are 2 distance apart.
'''

from heapq import *
from collections import deque


def reorganize_string(str, k):
    if k <= 1:
        return str

    # calc character frequency map
    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

    # insert character in max heap 
    maxHeap = []
    for char, freq in charFrequencyMap.items():
        heappush(maxHeap, (-freq, char))

    queue = deque()
    resultString = []
    while maxHeap:
        freq, char = heappop(maxHeap)
        resultString.append(char)

        # decrement the char frequency and add to the queue
        queue.append((char, freq+1))
        if len(queue) == k:
            char, freq = queue.popleft()
            if -freq > 0:
                heappush(maxHeap, (freq, char))

    # while maxHeap:
    #     waitList = []
    #     n = k
    #     while maxHeap and n > 0:
    #         n -= 1
    #         freq, char = heappop(maxHeap)
    #         resultString.append(char)
    #         if -freq > 1:
    #             waitList.append((freq + 1, char))
        
    #     if n != 0:
    #         break

    #     for freq, char in waitList:
    #         heappush(maxHeap, (freq, char))

    return ''.join(resultString) if len(resultString) == len(str) else ''


if __name__ == "__main__":
    print(reorganize_string("mmpp", 2))
    print(reorganize_string("Programming", 3))
    print(reorganize_string("aab", 2))
    print(reorganize_string("aappa", 3))
    print(reorganize_string("aaadbbcc", 2))
