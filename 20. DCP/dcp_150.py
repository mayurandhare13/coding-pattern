from heapq import heappush, heappop


def _distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def closestKPoints(points: list[tuple], center: tuple, k):
    maxHeap = []
    
    for i in range(k):
        dist = _distance(center, points[i])
        # keep largest element at top
        heappush(maxHeap, (-dist, points[i]))
    
    for i in range(k, len(points)):
        dist = _distance(center, points[i])

        # compare with largest element
        if -dist > maxHeap[0][0]:
            heappop(maxHeap)
            heappush(maxHeap, (-dist, points[i]))

    return [ point for _, point in maxHeap]


if __name__ == '__main__':
    assert closestKPoints(points=[(0, 0), (5, 4), (3, 1)], 
                        center=(1, 2), k=2) == [(0, 0), (3, 1)]
