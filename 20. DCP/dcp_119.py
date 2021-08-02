def isIntersecting(x, y):
    return not (x[0] > y[1] or y[0] > x[1])


def covering(intervals: list[list]):
    intervals.sort(key=lambda x: x[0])
    result = []
    i = 0

    while i < len(intervals):
        interval = intervals[i]

        while i < len(intervals) and isIntersecting(interval, intervals[i]):
            interval = (
                max(interval[0], intervals[i][0]),
                min(interval[1], intervals[i][1])
            )
            i += 1

        result.append(interval)

    if len(result) == 1:
        return result[0]
    
    return (result[0][1], result[-1][0])



if __name__ == '__main__':
    assert covering([[0, 3], [2, 6], [3, 4], [6, 9]]) == (3, 6)
    assert covering([[10, 20], [1, 6], [3, 8], [7, 12], [25, 30]]) == (6, 25)
    assert covering([[1, 6], [3, 8]]) == (3, 6)
