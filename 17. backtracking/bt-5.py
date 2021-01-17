'''
Permutations
Given a collection of distinct integers, return all possible permutations.
Input: [1,2,3]
Output:
[
  [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
]
'''


def permute(nums):

    # start --> with which index we swap other integers
    def backtrack(start = 0):
        if start == n - 1:
            results.append(nums[:])
            return
        
        for i in range(start, n):
            # place i'th integer first in current permutation
            nums[start], nums[i] = nums[i], nums[start]

            # use next integer to complete permutation
            backtrack(start + 1)

            # backtrack
            nums[start], nums[i] = nums[i], nums[start]

    n = len(nums)
    results = []
    backtrack()
    return results


if __name__ == "__main__":
    print(permute([1, 2, 3]))
