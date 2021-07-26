# using rejection sampling, we generate a (uniformly) random integer between 0 and n-1 (inclusive).
# Then, we check whether the random integer is found within the list l. If it is found, then generate repeat the process. 
# If it is not found, then return that number.
# Since this solution involves repeatedly generating a new random number, it could have up to infinite worst-case runtime.


from random import randrange

# O(n)
def processList(n, l: list):
    allNumsSet = set(range(n))
    lSet = set(l)

    numsSet = allNumsSet - lSet
    return list(numsSet)


# O(1)
def randomNumberExcludingList(n, l: list):
    numsList = processList(n, l)
    idx = randrange(0, len(numsList))

    return numsList[idx]


if __name__ == '__main__':
    print(randomNumberExcludingList(4, [1, 2, 5]))
