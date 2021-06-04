def firstMissingNumber(nums: list) -> int:
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1


if __name__ == '__main__':
    print(firstMissingNumber([3, 4, -1, 1]))
    print(firstMissingNumber([3, 4, 1, 1]))
