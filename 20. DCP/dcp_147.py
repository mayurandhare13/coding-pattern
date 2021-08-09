def getMaxIndex(l: list):
    return l.index(max(l))


def reverse(l: list, i, j):
    while i < j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1


# O(n^2) time
def pancakeSort(nums: list):
    for size in reversed(range(len(nums))):
        maxIndex = getMaxIndex(nums[:size + 1])

        # move max element at start
        reverse(nums, 0, maxIndex)

        # move max element at end
        reverse(nums, 0, size)

    return nums


if __name__ == '__main__':
    assert pancakeSort([0, 6, 4, 2, 5, 3, 1]) == \
                            [0, 1, 2, 3, 4, 5, 6]
    assert pancakeSort([0, 6, 4, 2, 5, 3, 1, 10, 9]) == \
                            [0, 1, 2, 3, 4, 5, 6, 9, 10]
    assert pancakeSort([0, 6, 4, 2, 5, 3, 1, 2, 3]) == \
                            [0, 1, 2, 2, 3, 3, 4, 5, 6]
    assert pancakeSort([0, 6, 4, 2, 5, 3, 1, 11]) == \
                        [0, 1, 2, 3, 4, 5, 6, 11]
