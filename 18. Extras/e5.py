'''
Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 (170) should be 01010101 (85).
'''

def swapBits(num):
    EVEN = 0b10101010
    ODD = 0b01010101

    return (num & EVEN) >> 1 | (num & ODD) << 1


if __name__ == '__main__':
    print(swapBits(170))
