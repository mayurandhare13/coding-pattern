def minStabPoints(intervals: list):
    startPoints, endPoints = zip(*intervals)
    return (min(endPoints), max(startPoints))


if __name__ == '__main__':
    assert minStabPoints([(1, 4), (4, 5), (7, 9), (9, 12)]) == (4, 9)
