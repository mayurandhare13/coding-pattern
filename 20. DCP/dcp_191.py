def nonOverlap(intervals: list):
    # sort based on end time
    intervals.sort(key=lambda x : x[1])
    end = float('-inf')
    erased = 0

    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            # remove current interval
            erased += 1
    
    return erased


if __name__ == '__main__':
    assert nonOverlap([(7, 9), (2, 4), (5, 8)]) == 1
