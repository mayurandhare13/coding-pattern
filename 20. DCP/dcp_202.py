def isPalindrome(num: int) -> bool:
    n = num
    tmp = 0

    while n > 0:
        tmp = tmp * 10 + (n % 10)
        n = n // 10
    
    if tmp == num:
        return True
    
    return False


if __name__ == '__main__':
    print(isPalindrome(789))
    print(isPalindrome(121))
