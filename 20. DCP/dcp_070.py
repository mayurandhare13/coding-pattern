def getPerfectNumber(num):
    numSum = 0
    n = num
    while n > 0:
        q = n % 10
        numSum += q
        n = n // 10
    
    return num * 10 + (10 - numSum)


if __name__ == '__main__':
    assert getPerfectNumber(1) == 19
    assert getPerfectNumber(2) == 28
    assert getPerfectNumber(20) == 208
