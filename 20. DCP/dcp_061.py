def pow(x: int, n: int):
    # if power is negative, make it positive
    # easy to divide positive number till 1
    if n < 0:
        n = -n
        x = 1/x
    
    ans = 1
    prod = x

    while n > 0:
        if n % 2 == 1:
            ans = ans * prod
        
        prod = prod * prod
        n = n // 2
    
    return ans


if __name__ == '__main__':
    assert pow(2, 9) == 512
    assert pow(2, -2) == 0.25
