def canPartitionHelper(nums, _sum, index):
    if _sum == 0:
        return True
    
    if index >= len(nums):
        return False
    
    if nums[index] <= _sum:
        if canPartitionHelper(nums, _sum - nums[index], index + 1):
            return True
    
    return canPartitionHelper(nums, _sum, index + 1)



def canPatition(nums: list):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    return canPartitionHelper(nums, total // 2, 0)



if __name__ == '__main__':
    assert canPatition([15, 5, 20, 10, 35, 15, 10]) == True
    assert canPatition([15, 5, 20, 10, 35]) == False
