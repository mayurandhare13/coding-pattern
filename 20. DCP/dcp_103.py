from collections import defaultdict


def findSubstring(str, pattern):
    assert pattern != ''

    charFrequency = defaultdict(int)
    for ch in pattern:
        charFrequency[ch] += 1

    minLen = len(str) + 1
    start, end = 0, 0
    subStart = 0
    matched = 0

    for end in range(len(str)):
        rightChar = str[end]
        if rightChar in charFrequency:
            charFrequency[rightChar] -= 1
            if charFrequency[rightChar] >= 0:
                matched += 1

        while matched == len(pattern):
            if minLen > (end - start + 1):
                minLen = end - start + 1
                subStart = start

            leftChar = str[start]
            if leftChar in charFrequency:
                if charFrequency[leftChar] >= 0:
                    matched -= 1
                charFrequency[leftChar] += 1

            start += 1

    if minLen > len(str):
        return ''

    return str[subStart : subStart + minLen]


if __name__ == '__main__':
    assert findSubstring('figehaeci', 'aei') == 'aeci'
    assert findSubstring('aabdec', 'abc') == 'abdec'
