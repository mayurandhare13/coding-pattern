def towerOfHanoi(n, a='1', b='2', c='3'):
    if n > 0:
        # move n - 1 from `a` to "b" using `c`
        towerOfHanoi(n - 1, a, c, b)

        print(f"Move {a} to {c}")

        # move n - 1 from `b` to "c" using `a`
        towerOfHanoi(n - 1, b, a, c)


if __name__ == '__main__':
    towerOfHanoi(3)
