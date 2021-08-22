def helper(nums: list, low, high):
    while low < high:
        mid = (low + high) // 2

        if nums[mid] < nums[high]:
            high = mid - 1
        else:
            low = mid + 1

    return nums[low]


def findMinElement(nums: list):
    return helper(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    assert findMinElement([5, 7, 10, 3, 4]) == 3
    assert findMinElement([10, 9, 8, 7, 1]) == 1
