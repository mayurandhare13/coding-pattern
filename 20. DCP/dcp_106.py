def canReachEnd(hops: list) -> bool:
    stepsLeft = 1
    for i in range(len(hops) - 1):
        stepsLeft = max(stepsLeft - 1, hops[i])
        if stepsLeft == 0:
            return False
    
    return True


if __name__ == '__main__':
    assert canReachEnd([2, 0, 1, 0]) == True
    assert canReachEnd([1, 1, 0, 1]) == False
