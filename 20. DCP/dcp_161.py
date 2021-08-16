def reverseBits(n: int):
    rev = 0

    while n > 0:
        rev = rev << 1
        if n & 1 == 1:
            rev = rev ^ 1

        n = n >> 1

    return rev


if __name__ == '__main__':
    assert reverseBits(11) == 13
    assert reverseBits(4294967293) == 3221225471
