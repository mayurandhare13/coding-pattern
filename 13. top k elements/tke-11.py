'''
Rearrange String (hard)

Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.
'''

from heapq import *


def rearranged_string(str):
    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

    # add all characters to the maxHeap
    maxHeap = []
    for char, freq in charFrequencyMap.items():
        heappush(maxHeap, (-freq, char))

    prevChar, prevFreq = None, 0
    resultString = []
    while maxHeap:
        freq, char = heappop(maxHeap)
        # add prev entry back to the maxHeap
        if prevChar and -prevFreq > 0:
            heappush(maxHeap, (prevFreq, prevChar))

        resultString.append(char)
        prevChar = char
        prevFreq = freq + 1 # decrement the freqency

    return ''.join(resultString) if len(resultString) == len(str) else ""


if __name__ == "__main__":
    print(rearranged_string("aappp"))
    print(rearranged_string("Programming"))
    print(rearranged_string("aapa"))
