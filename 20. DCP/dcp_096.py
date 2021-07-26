# O(n!)
def permutation(nums: list):
    if len(nums) == 1:
        return [nums]
    
    output = []
    for l in permutation(nums[1:]):
        for idx in range(len(nums)):
            output.append(l[:idx] + [nums[0]] + l[idx:])

    return output


def permute(nums):
    def helper(nums, index, output):
        if index == len(nums):
            output.append(nums.copy())

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            helper(nums, index + 1, output)
            nums[i], nums[index] = nums[index], nums[i]


    output = []
    helper(nums, 0, output)
    return output


if __name__ == '__main__':
    assert permutation([1, 2, 3]) == [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]

    assert permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
