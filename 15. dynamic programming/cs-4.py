'''
Longest Increasing Subsequence

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LIS is {2,3,6,10,12}.
'''

def find_LIS_lengths_helper(nums, currentIndex, prevIndex):
    if currentIndex >= len(nums):
        return 0

    # include current index if value > last index value
    c1 = 0
    if prevIndex == -1 or nums[prevIndex] < nums[currentIndex]:
        c1 = 1 + find_LIS_lengths_helper(nums, currentIndex + 1, currentIndex)
    
    # exclude the current index
    c2 = find_LIS_lengths_helper(nums, currentIndex + 1, prevIndex)

    return max(c1, c2)


def find_LIS_lengths(nums):
    return find_LIS_lengths_helper(nums, 0, -1)


if __name__ == "__main__":
    print(find_LIS_lengths([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS_lengths([-4, 10, 3, 7, 15]))
    print(find_LIS_lengths([0,1,0,3,2,3]))
