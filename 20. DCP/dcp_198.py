def divisibleSubset(nums: list):
    nums.sort()

    numDivisors = [1 for _ in range(len(nums))]
    prevDivisorIndex = [-1 for _ in range(len(nums))]

    maxIndex = 0

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and (numDivisors[i] < numDivisors[j] + 1):
                numDivisors[i] = numDivisors[j] + 1
                prevDivisorIndex[i] = j
        
        if numDivisors[maxIndex] < numDivisors[i]:
            maxIndex = i


    result = []
    i = maxIndex
    while i >= 0:
        result.append(nums[i])
        i = prevDivisorIndex[i]

    return result


if __name__ == '__main__':
    assert divisibleSubset([3, 5, 10, 20, 21]) == [20, 10, 5]
    assert divisibleSubset([1, 3, 6, 24]) == [24, 6, 3, 1]
