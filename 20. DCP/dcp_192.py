def canReachEnd(steps: list) -> bool:
    possibleSteps = steps[0]
    c = 0

    while c <= possibleSteps:
        if possibleSteps >= len(steps) - 1:
            return True

        # at any moment, I could have c + steps[c] jump indices
        # or possible jumps from previous index option
        possibleSteps = max(possibleSteps, c + steps[c])
        c += 1

    return False


if __name__ == '__main__':
    assert canReachEnd([1, 3, 1, 2, 0, 1])
    assert not canReachEnd([1, 2, 1, 0, 0])
