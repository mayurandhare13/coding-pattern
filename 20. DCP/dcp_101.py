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


# ------------------------------------------

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def primeSum(n):
    for i in range(2, n):
        if isPrime(i) and isPrime(n-i):
            return (i, n-i)

    return (-1, -1)



if __name__ == '__main__':
    print('p1  p2')

    p1, p2 = findPrimePair(4)
    # p1, p2 = primeSum(4)
    print(p1, ' ', p2)

    p1, p2 = findPrimePair(74)
    # p1, p2 = primeSum(74)
    print(p1, ' ', p2)

    p1, p2 = findPrimePair(66)
    # p1, p2 = primeSum(66)
    print(p1, ' ', p2)
