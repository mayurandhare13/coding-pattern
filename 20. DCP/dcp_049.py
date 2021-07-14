# Kadane's algorithm

def maxSubarray(nums: list):
    currentMaxsum, overallMaxsum = nums[0], nums[0]

    for num in nums[1:]:
        # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
        # if adding num to currentSubarray < num, then start over new subarray
        currentMaxsum = max(num, currentMaxsum + num)
        overallMaxsum = max(currentMaxsum, overallMaxsum)
    
    return max(overallMaxsum, 0)


if __name__ == '__main__':
    assert maxSubarray([34, -50, 42, 14, -5, 86]) == 137
    assert maxSubarray([-5, -1, -8, -9]) == 0
