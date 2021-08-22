def findGCD(x, y):
    while y:
        x, y = y, x % y

    return x


if __name__ == '__main__':
    nums = [42, 56, 14]
    gcd = findGCD(nums[0], nums[1])
    for i in range(2, len(nums)):
        gcd = findGCD(gcd, nums[i])
    
    assert gcd == 14
