from collections import defaultdict


def findAnagrams(S, pattern) -> list:
    charFrequencyMap = defaultdict(int)
    for c in pattern:
        charFrequencyMap[c] += 1
    
    indices = []
    start, end = 0, 0
    matches = 0

    for end in range(len(S)):
        rightChar = S[end]
        if rightChar in charFrequencyMap:
            charFrequencyMap[rightChar] -= 1
            if charFrequencyMap[rightChar] == 0:
                matches += 1
        
        if matches == len(charFrequencyMap):
            indices.append(start)
        
        if end >= len(pattern) - 1:
            leftChar = S[start]
            start += 1
            if leftChar in charFrequencyMap:
                if charFrequencyMap[leftChar] == 0:
                    matches -=1
                charFrequencyMap[leftChar] += 1

    return indices


if __name__ == "__main__":
    assert findAnagrams('abxaba', 'ab') == [0, 3, 4]
    assert findAnagrams('abbcabc', 'abc') == [2, 3, 4]
