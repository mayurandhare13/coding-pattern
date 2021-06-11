MAXN = 105

# dp[i] = number of max heaps for i distinct integers
dp = [0] * MAXN
nck = [[0 for _ in range(MAXN)] for _ in range(MAXN)]

# log2[i] = floor of logarithm of base 2 of i
log2 = [0] * MAXN


# initialize arrays
def init(n):
    for i in range(n+1):
        dp[i] = -1
    
    for i in range(n+1):
        for j in range(n+1):
            nck[i][j] = -1
    
    currLog2 = -1
    currPower2 = 1

    # for each power of 2, find log
    for i in range(1, n+1):
        if currPower2 == i:
            currLog2 += 1
            currPower2 *= 2
        log2[i] = currLog2


def choose(n, k):
    if k > n:
        return 0
    
    if n <= 1 or k == 0:
        return 1

    if nck[n][k] != -1:
        return nck[n][k]
    
    # Binomial Coefficient
    # nCk = n! / k! * (n-k)!
    nck[n][k] = choose(n - 1, k - 1) + choose(n - 1, k)

    return nck[n][k]


#  l elements in the left sub-tree
def getLeft(n):
    if n == 1:
        return 0
    
    h = log2[n]
    
    # max number of elements that can be present in the 
    # hth level of any heap
    numH = (1 << h)     # 2^h

    # number of elements that are actually present in
    # last level(hth level)
    # (2^h - 1)
    numLast = n - ((1 << h) - 1)

    if numLast >= numH // 2:
        return (1 << h) - 1     # (2^h) - 1
    else:
        return (1 << h) - 1 - ((numH // 2) - numLast)


def numberOfHeaps(n):
    if n <= 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    # for the root, l + r = n-1
    # we can choose any l of the remaining n-1 elements for the left sub-tree as they are all smaller than the root. (nCk)
    # T(n) = {n-1}choose{l}  * T(L) * T(R).
    left = getLeft(n)
    dp[n] = choose(n-1, left) * numberOfHeaps(left) * numberOfHeaps(n - 1 - left)

    return dp[n]


if __name__ == '__main__':
    init(3)
    assert numberOfHeaps(3) == 2
    
    init(10)
    assert numberOfHeaps(10) == 3360
