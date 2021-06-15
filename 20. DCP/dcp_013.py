def longestSubstring(s: str, k: int) -> str:
    start = 0
    maxWindowStart, maxLen = 0, 0

    charFrequencyMap = {}
    for end in range(len(s)):
        endChar = s[end]

        if endChar not in charFrequencyMap:
            charFrequencyMap[endChar] = 0
        charFrequencyMap[endChar] += 1

        while len(charFrequencyMap) > k:
            startChar = s[start]
            charFrequencyMap[startChar] -= 1
            if charFrequencyMap[startChar] == 0:
                del charFrequencyMap[startChar]
            start += 1
        
        if end - start + 1 > maxLen:
            maxLen = end - start + 1
            maxWindowStart = start
    
    return s[maxWindowStart : maxWindowStart+maxLen]


if __name__ == '__main__':
    assert longestSubstring('abcba', 2) == 'bcb'
    assert longestSubstring('araaci', 2) == 'araa'
