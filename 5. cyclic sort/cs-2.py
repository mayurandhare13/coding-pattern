'''
Find the Missing Number (easy)

We are given an array containing 'n' distinct numbers taken from the range 0 to 'n'. Since the array has only 'n' numbers out of the total 'n+1' numbers, find the missing number.

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
'''


def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        if nums[i] < n and nums[i] != i:
            j = nums[i]
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i:
            return i

    return n

# 4^[(0^4)^(1^0)^(2^3)^(3^1)]
def find_missing_number2(nums):
    missing = len(nums)
    for key, val in enumerate(nums):
        missing ^= key ^ val

    return missing


if __name__ == "__main__":
    print(find_missing_number2([2, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
