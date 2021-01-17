'''
Longest Bitonic Subsequence
bitonic if sequence is monotonically increasing and then monotonically decreasing.

Input: {4,2,5,9,7,6,10,3,1}
Output: 7
Explanation: The LBS is {4,5,9,7,6,3,1}.
'''

def find_LBS_length(nums):
    maxLength = 0
    for i in range(len(nums)):
        c1 = find_LDS_length(nums, i, -1)
        c2 = find_LDS_length_rev(nums, i, -1)
        maxLength = max(maxLength, c1 + c2 - 1)
    
    return maxLength

# prevIndex in both the cases is `-1`
# because we want to consider that index value as the starting point

# find longest decreasing sequence from current index to end of array
def find_LDS_length(nums, currentIndex, prevIndex):
    if currentIndex >= len(nums):
        return 0

    c1 = 0
    if prevIndex == -1 or nums[currentIndex] < nums[prevIndex]:
        c1 = 1 + find_LDS_length(nums, currentIndex + 1, currentIndex)
    
    c2 = find_LDS_length(nums, currentIndex + 1, prevIndex)

    return max(c1, c2)


# find longest decreasing sequence from current index to start of the array
def find_LDS_length_rev(nums, currentIndex, prevIndex):
    if currentIndex < 0:
        return 0

    c1 = 0
    if prevIndex == -1 or nums[currentIndex] < nums[prevIndex]:
        c1 = 1 + find_LDS_length_rev(nums, currentIndex - 1, currentIndex)
    
    c2 = find_LDS_length_rev(nums, currentIndex - 1, prevIndex)

    return max(c1, c2)
    


if __name__ == "__main__":
    print(find_LBS_length([4, 2, 3, 6, 10, 1, 12]))
    print(find_LBS_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))

