# Pick a Random Element from an Infinite Stream

import random

def pick(bigStream) -> int:
    randomElement = None

    for i, e in enumerate(bigStream):
        if i == 0:
            randomElement = e
        elif random.randint(1, i+1) == 1:
            randomElement = e

    return randomElement


def pick(bigStream, k) -> list:
    reservoir = []

    for i, val in enumerate(bigStream):
        if i < k:
            reservoir.append(val)
        
        randomIndex = random.randint(0, i)
        if randomIndex < k:
            reservoir[randomIndex] = val

    return reservoir


# random index of target (duplicated)
def pick(nums, target: int) -> int:
    k, idx = 0, 0

    for i, val in enumerate(nums):
        if val != target:
            continue
        
        randomIndex = random.randint(0, k)
        if randomIndex == 0:
            idx = i

        k += 1

    return idx
