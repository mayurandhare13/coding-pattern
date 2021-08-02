def findContinuousK(list, K):
    _sum = 0
    start, end = 0, 0

    while end < len(list):
        if _sum == K:
            return list[start: end]
        
        if _sum > K:
            _sum -= list[start]
            start += 1
        else:
            _sum += list[end]
            end += 1


if __name__ == '__main__':
    assert findContinuousK([1, 2, 3, 4, 5], 9) == [2, 3, 4]
    assert findContinuousK([5, 4, 3, 4, 5], 11) == [4, 3, 4]
