def mergeInvervals(intervals: list):

    # sort intervals based on start
    intervals.sort(key=lambda x : x[0])

    merged = []
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]
        # overlapping intervals
        if interval[0] <= end:
            end = max(interval[1], end)

        else:
            merged.append((start, end))
            start = interval[0]
            end = interval[1]

    merged.append((start, end))

    return merged


if __name__ == '__main__':
    assert mergeInvervals([(1, 3), (5, 8), (4, 10), (20, 25)]) \
         == [(1, 3), (4, 10), (20, 25)]

    assert mergeInvervals([(1, 4), (2, 6), (3, 5)]) == [(1, 6)]
