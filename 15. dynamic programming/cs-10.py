'''
Longest Alternating Subsequence
{a1 > a2 < a3 } or { a1 < a2 > a3}. 

Input: {3,2,1,4}
Output: 3
Explanation: The LAS are {3,2,4} and {2,1,4}.

for DP:-
dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
if dp[previousIndex + 1][currentIndex][1 if isAsc else 0] == -1:
'''

def find_LAS_length_helper(nums, currentIndex, prevIndex, isAsc):
    if currentIndex == len(nums):
        return 0

    c1 = 0
    # ascending: current element should be bigger
    if isAsc:
        if prevIndex == -1 or nums[prevIndex] < nums[currentIndex]:
            c1 = 1 + find_LAS_length_helper(nums, currentIndex + 1, currentIndex, not isAsc)
    else:
        if prevIndex == -1 or nums[currentIndex] < nums[prevIndex]:
            c1 = 1 + find_LAS_length_helper(nums, currentIndex + 1, currentIndex, not isAsc)

    # skip the current element to find other possible sequence
    c2 = find_LAS_length_helper(nums, currentIndex + 1, prevIndex, isAsc)

    return max(c1, c2)


def find_LAS_length(nums):
    # we have to start with two recursive calls, one where we will consider that the first element 
    # is bigger than the second element and one where the first element is smaller than the second element
    return max(
        find_LAS_length_helper(nums, 0, -1, True),
        find_LAS_length_helper(nums, 0, -1, False)
    )


if __name__ == "__main__":
    print(find_LAS_length([1, 2, 3, 4]))
    print(find_LAS_length([3, 2, 1, 4]))
    print(find_LAS_length([1, 3, 2, 4]))

