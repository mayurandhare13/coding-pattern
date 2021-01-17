'''
Minimum Deletions to Make a Sequence Sorted
Input: {4,2,3,6,10,1,12}
Output: 2
Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.
'''

def find_minimum_deletions_helper(nums, currentIndex, prevIndex):
    if currentIndex >= len(nums):
        return 0

    c1 = 0
    if prevIndex == -1 or nums[prevIndex] < nums[currentIndex]:
        c1 = 1 + find_minimum_deletions_helper(nums, currentIndex + 1, currentIndex)
    
    c2 = find_minimum_deletions_helper(nums, currentIndex + 1, prevIndex)

    return max(c1, c2)


def find_minimum_deletions(nums):
    return len(nums) - find_minimum_deletions_helper(nums, 0, -1)


if __name__ == "__main__":
    print(find_minimum_deletions([4,2,3,6,10,1,12]))
    print(find_minimum_deletions([-4,10,3,7,15]))
    print(find_minimum_deletions([3,2,1,0]))
    