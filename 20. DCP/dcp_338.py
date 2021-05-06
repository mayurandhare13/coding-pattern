'''
10011100
00011100 - right most string of 1's in x
00000011 - right shifted pattern except left most bit ------> [A]
00010000 - isolated left most bit of right most 1's pattern
00100000 - shiftleft-ed the isolated bit by one position ------> [B]
10000000 - left part of x, excluding right most 1's pattern ------> [C]
10100000 - add B and C (OR operation) ------> [D]
10100011 - add A and D which is required number 163
'''

# Same Number Of One Bits
def snoob(x: int):
    next = 0

    # right most set bit
    rightOne = x & -x

    # reset the pattern and
    # set next higher bit left part of x will be here [D]
    nextHigherOneBit = x + int(rightOne)

    rightOnesPattern = x ^ int(nextHigherOneBit)

    # right adjust pattern
    rightOnesPattern = rightOnesPattern // int(rightOne)

    # correction factor
    rightOnesPattern = rightOnesPattern >> 2

    next = nextHigherOneBit | rightOnesPattern

    return next


if __name__ == '__main__':
    print(snoob(6))
