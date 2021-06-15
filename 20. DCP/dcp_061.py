def pow(x: int, n: int):
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
    print(pow(2, 9))
    print(pow(2, -2))
