def aOrb(x, y, b):
    return x * b + y * (1-b)

if __name__ == '__main__':
    assert aOrb(3, 4, 1) == 3
    assert aOrb(3, 4, 0) == 4
