def nonAdjacentSum(nums: list) -> int:
    incl, excl = 0, 0

    for num in nums:
        # excl = if we are excluding current element
        # then max sum excluding current element could be previoud `incl | excl`
        tmp = excl if excl > incl else incl

        incl = excl + num
        excl = tmp
    
    return max(incl, excl)


if __name__ == '__main__':
    assert nonAdjacentSum([2, 4, 6, 8]) == 12
    assert nonAdjacentSum([5, 1, 1, 5]) == 10
    assert nonAdjacentSum([5, 5, 10, 100, 10, 5]) == 110
