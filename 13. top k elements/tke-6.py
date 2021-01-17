'''
Frequency Sort (medium)

Given a string, sort it based on the decreasing frequency of its characters.

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
'''

from heapq import *


def sort_characters_by_frequency(str):
    # calc freq of each character
    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1
    

    # add all characters to max heap
    maxHeap = []
    for char, freq in charFrequencyMap.items():
        heappush(maxHeap, (-freq, char))
    
    # build string
    sortedString = []
    while maxHeap:
        freq, char = heappop(maxHeap)
        for _ in range(-freq):
            sortedString.append(char)
    
    return ''.join(sortedString)


if __name__ == "__main__":
    print(sort_characters_by_frequency("Programming"))
    print(sort_characters_by_frequency("abcbab"))
