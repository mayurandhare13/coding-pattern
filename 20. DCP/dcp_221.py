'''
represent number in binary
N = 5 --> 101
1 * pow(7, 0) + 0 * pow(7, 1) + 1 * pow(7, 2)
----------------------------------------------
1*1             +      0*7        +     1*49    == 50
'''

def sevenishNumber(N):
    ans = 0
    prod = 1

    while N:

        if N & 1:
            ans += prod
        
        prod = prod * 7
        N = N >> 1
    
    return ans


if __name__ == '__main__':
    print(sevenishNumber(1))
    print(sevenishNumber(2))
    print(sevenishNumber(3))
    print(sevenishNumber(4))
    print(sevenishNumber(5))

