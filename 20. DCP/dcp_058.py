def searchRotatedArray(nums: list, key):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == key:
            return mid
        
        # left is ascending
        if nums[start] <= nums[mid]:
            if key >= nums[start] and key < nums[mid]:
                end = mid
            else:
                start = mid

        # right is ascending
        else:
            if key > nums[mid] and key <= nums[end]:
                start = mid
            else:
                end = mid
    
    return -1



if __name__ == "__main__":
    assert searchRotatedArray([13, 18, 25, 2, 8, 10] , key = 8) == 4
    assert searchRotatedArray([10, 15, 1, 3, 8], key = 15) == 1
    assert searchRotatedArray([4, 5, 7, 9, 10, -1, 2], key = 10) == 4
