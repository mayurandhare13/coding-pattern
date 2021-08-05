def singleNumbers(nums: list):
    xor = 0

    for num in nums:
        xor = xor ^ num
    
    # -x = ~x + 1   two's complement
    rightmostSetBit = xor & -xor

    x, y = 0, 0
    for num in nums:
        if rightmostSetBit & num:
            x = x ^ num

        else:
            y = y ^ num
    
    return (x, y)


if __name__ == '__main__':
    assert singleNumbers([2, 4, 6, 8, 10, 2, 6, 10]) == (4, 8)
