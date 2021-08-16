# [5, 4, 1, 4, 2]

def duplicate(nums: list):
    size = len(nums)

    i = 0
    while i < size:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1

    return -1


if __name__ == '__main__':
    assert duplicate([5, 4, 1, 4, 2]) == 4
