def longestConsecutive(numbers: list):
    maxLen = 0
    bounds = {}

    for num in numbers:
        if num in bounds:
            continue

        leftBound, rightBound = num, num
        if num - 1 in bounds:
            leftBound = bounds[num - 1][0]
        if num + 1 in bounds:
            rightBound = bounds[num + 1][1]
        
        bounds[num] = (leftBound, rightBound)
        bounds[leftBound] = (leftBound, rightBound)
        bounds[rightBound] = (leftBound, rightBound)

        maxLen = max(rightBound - leftBound + 1, maxLen)
    
    return maxLen


if __name__ == '__main__':
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
