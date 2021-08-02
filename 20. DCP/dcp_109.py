def swapBits(num):
    return ((num & 0b01010101) << 1) | ((num & 0b10101010) >> 1)


if __name__ == '__main__':
    assert swapBits(255) == 255
    assert swapBits(170) == 85
