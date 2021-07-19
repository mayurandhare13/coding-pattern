def multipleCount(n, x):
    if n == 1:
        return n

    tuples = list()
    for i in range(1, x//2 + 1):
        if x % i == 0 and (x / i) <= n:
            tuples.append((i, x // i))

    print(tuples)
    return len(tuples)


if __name__ == '__main__':
    assert multipleCount(1, 1) == 1
    assert multipleCount(6, 12) == 4
    assert multipleCount(2, 4) == 1
    assert multipleCount(3, 6) == 2
