def josephus(n, k):
    """
        n: The number of objects in the circle (array)
        k: The number of skips after an object is removed
        return: The position of the final object left
    """
    if n == 1:
        return 1
    else:
        # The position returned by josephus(n - 1, k) is adjusted
        # because the recursive call josephus(n - 1, k) considers
        # the original position k%n + 1 as position 1
        # for 0-index (J(n-1, k) + k) % n
        
        return (josephus(n-1, k) + k-1) % n + 1


if __name__ == '__main__':
    print(josephus(14, 2))
    print(josephus(5, 2))
    print(josephus(7, 3))
