def partition(nums: list, x) -> list:
    i, j = 0, 0
    k = len(nums) - 1

    while j < k:
        if nums[j] < x:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        
        elif nums[j] == x:
            j += 1
        
        else:
            # as we don't know after swapping nums[j] == k ??
            # so, we do not increment j
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1

    return nums

if __name__ == '__main__':
    
    assert partition([9, 12, 3, 5, 14, 10, 10], 10) == [9, 3, 5, 10, 10, 14, 12]
    assert partition([9, 12, 3, 5, 14, 10, 10], 8) == [5, 3, 12, 14, 10, 10, 9]
