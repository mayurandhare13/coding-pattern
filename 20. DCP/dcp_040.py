# https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers


def singleNumber(nums: list) -> int:
    # 2^m >= k
    # 2^2 >= 3 --> x1, x2
    # when x1 & x2 becomes k. reset the counter using mask
    # k = 3 --> 011  --> mask = ~(x1 & x2)
    # p = 1, single number counter. Here single number will appear only once

    x1, x2 = 0, 0

    for num in nums:
        x2 ^= x1 & num
        x1 ^= num

        mask = ~(x1 & x2)

        x2 &= mask
        x1 &= mask

    # return x1         # p = 1, in binary form p = '01', then p1 = 1, so return x1
    return x1 | x2


def singleNumber5(nums: list) -> int:
    # 2^m >= k
    # 2^3 >= 5 --> x1, x2, x3
    # when x1, x2, x3 becomes k. reset the counter using mask
    # k = 5 --> 101  --> mask = ~(x1 & ~x2 & x3)

    x1, x2, x3 = 0, 0, 0
    
    for num in nums:
        x3 ^= x2 & x1 & num
        x2 ^= x1 & num
        x1 ^= num

        mask = ~(x1 & ~x2 & x3)
        x3 &= mask
        x2 &= mask
        x1 &= mask
    
    return x1 | x2 | x3



if __name__ == '__main__':
    # p = 1
    assert singleNumber([6, 1, 3, 3, 3, 6, 6]) == 1
    assert singleNumber([13, 19, 13, 13]) == 19

    # p = 2
    assert singleNumber([6, 1, 1, 3, 3, 3, 6, 6]) == 1
    assert singleNumber([13, 19, 19, 13, 13]) == 19

    assert singleNumber5([6, 1, 1, 6, 6, 6, 6]) == 1
    assert singleNumber5([13, 19, 13, 13, 13, 13]) == 19
