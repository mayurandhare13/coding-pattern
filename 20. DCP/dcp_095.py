def nextPermutation(nums: list):
    def swap(nums, a, b):
        # in-place swapping
        nums[a], nums[b] = nums[b], nums[a]
    
    def reverse(nums, a, b):
        # reverse inclusive [a, b]
        nums[a:b+1] = reversed(nums[a:b+1])
    
    # Find first index where nums[idx] < nums[idx + 1]
    pivot = len(nums) - 2
    while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
        pivot -= 1
    
    # Find the next-largest number to swap with
    if pivot >= 0:
        successor = len(nums) - 1
        while successor >= 0 and nums[successor] <= nums[pivot]:
            successor -= 1
        
        swap(nums, pivot, successor)
    
    reverse(nums, pivot + 1, len(nums) - 1)


if __name__ == '__main__':
    nums = [1, 2, 3]
    nextPermutation(nums)
    assert nums == [1, 3, 2]
    
    nums = [1, 3, 2]
    nextPermutation(nums)
    assert nums == [2, 1, 3]
    
    nums = [3, 2, 1]
    nextPermutation(nums)
    assert nums == [1, 2, 3]
