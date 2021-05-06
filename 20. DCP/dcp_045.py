from random import randint
import math

def rand5():
    return randint(1, 5)

'''
we have to run rand5() function at least twice, as there are not enough numbers in the range of 1 to 7. By running rand5() twice, we can get integers from 1 to 25 uniformly.

Since 25 is not a multiple of 7, we have to use rejection sampling. Our desired range is integers from 1 to 21, which we can return the answer immediately. If not (the integer falls between 22 to 25), we reject it and repeat the whole process again.
'''
def rand7():
    idx, row, col = math.inf, 0, 0

    while idx > 21:
        row = rand5()
        col = rand5()
        idx = col + (row - 1) * 5

    # to get num within [1-7], idx = 7 --> 7 % 7 == 0
    # so, 1 + (7-1) % 7 == 1 + 6%7 = 1+6 = 7
    return 1 + (idx - 1) % 7


if __name__ == '__main__':
    for _ in range(7):
        print(rand7())
