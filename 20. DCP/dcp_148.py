def greyCode(n):
    if n == 0:
        return ['']

    bases = greyCode(n - 1)
    l0 = ['0' + x for x in bases]
    l1 = ['1' + x for x in reversed(bases)]

    return l0 + l1


if __name__ == '__main__':
    assert greyCode(1) == ['0', '1']
    assert greyCode(2) == ['00', '01', '11', '10']
    assert greyCode(3) == ['000', '001', '011',
                                '010', '110', '111', '101', '100']
