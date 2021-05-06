from random import random

'''
We call tossBiased() two times. Both calls will return 0 with a 70% probability. So the two pairs (0, 1) and (1, 0) will be generated with equal probability from two calls of foo().
(0, 1): The probability to get 0 followed by 1 from two calls of tossBiased() = 0.7 * 0.3 = 0.21 
(1, 0): The probability to get 1 followed by 0 from two calls of tossBiased() = 0.3 * 0.7 = 0.21

call tossBiased() until we get different coin
'''


def tossBiased():
    return int(random() < 0.3)

def fairCoin():
    coin1, coin2 = 0, 0
    while coin1 == coin2:
        coin1, coin2 = tossBiased(), tossBiased()
    
    return coin1


if __name__ == '__main__':
    print(sum(fairCoin() for _ in range(100000)))
