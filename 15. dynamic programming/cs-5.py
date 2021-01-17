'''
Maximum Sum Increasing Subsequence

Input: {4,1,2,6,10,1,12}
Output: 32
Explanation: The increasing sequence is {4,6,10,12}. 
Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.
'''

def find_MIS_sum_helper(nums, currentIndex, prevIndex, runningSum):
    if currentIndex == len(nums):
        return runningSum
    
    s1 = 0
    if prevIndex == -1 or nums[prevIndex] < nums[currentIndex]:
        s1 = find_MIS_sum_helper(
            nums, currentIndex + 1, currentIndex, runningSum + nums[currentIndex])

    s2 = find_MIS_sum_helper(nums, currentIndex + 1, prevIndex, runningSum)

    return max(s1, s2)


def find_MIS_sum(nums):
    return find_MIS_sum_helper(nums, 0, -1, 0)


if __name__ == "__main__":
    print(find_MIS_sum([4, 1, 2, 6, 10, 1, 12]))
    print(find_MIS_sum([-4, 10, 3, 7, 15]))
