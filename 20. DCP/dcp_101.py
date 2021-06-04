# Generate all prime numbers less than n.
def sieveOfEratosthenes(n):
    primeList = [True] * (n+1)
    primeList[0] = primeList[1] = False

    p = 2
    while p*p <= n:
        if primeList[p]:
            for i in range(p*p, n+1, p):
                primeList[i] = False
        
        p += 1

    return primeList


def findPrimePair(n):
    primeList = sieveOfEratosthenes(n)

    for i in range(n):
        if primeList[i] and primeList[n-i]:
            return (i, n-i)
    
    return (-1, -1)


if __name__ == '__main__':
    print('p1  p2')

    p1, p2 = findPrimePair(4)
    print(p1, ' ', p2)

    p1, p2 = findPrimePair(74)
    print(p1, ' ', p2)

    p1, p2 = findPrimePair(66)
    print(p1, ' ', p2)
