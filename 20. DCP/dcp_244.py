def sieveOfEratosthenes(n) -> list:
    primes = [True] * (n+1)

    p = 2
    while p*p <= n:
        # If primes[p] is not changed, then it is a prime
        if primes[p] == True:
            for i in range(p*p, n+1, p):
                primes[i] = False
        
        p += 1

    numbers = []
    for p in range(2, n+1):
        if primes[p]:
            numbers.append(p)
    
    return numbers


if __name__ == '__main__':
    print(sieveOfEratosthenes(10))

