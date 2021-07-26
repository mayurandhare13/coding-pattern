def divide(dividend, divisor):
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    quotient = 0
    
    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend >= divisor:
        quotient += 1
        dividend -= divisor
    
    return sign * quotient


if __name__ == '__main__':
    assert divide(10, 3) == 3
    assert divide(43, -8) == -5
