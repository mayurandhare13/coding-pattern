def squareroot(n, error=0.00001):
    low = 0.0
    high = n
    guess = low + (high - low) / 2

    while abs(guess ** 2 - n) >= error:
        if guess ** 2 > n:
            high = guess
        
        else:
            low = guess
        
        guess = low + (high - low) / 2
    
    return guess


if __name__ == '__main__':
    print(squareroot(9))
