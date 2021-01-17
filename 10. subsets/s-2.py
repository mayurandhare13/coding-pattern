'''
Subsets With Duplicates (easy)

Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

---
skip [], [1] <-- as it was already there when we chose 3 | skip prev len(subsets)-1
'''


def find_subsets(nums):
    nums.sort() # list.sort(nums)
    
    subsets = []
    subsets.append([])
    
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        # if current and the previous elements are same, create new subsets only from the subsets
        # added in the previous step | skipping subsets which was already exists before prev run of same element
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex
        endIndex = len(subsets)
        for j in range(startIndex, endIndex):
            _set = list(subsets[j])
            _set.append(nums[i])
            subsets.append(_set)

    return subsets


if __name__ == "__main__":

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 1, 2, 2])))
