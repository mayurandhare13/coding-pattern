'''
Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
'''

from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"

    # use for max heap | NOTE `>` in less than | only in maxHeap
    # we are using min-heap. but modified the comparison operator
    # so max point is at the root
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        # ignoring sqrt
        return (self.x * self.x) + (self.y * self.y)


def find_closest_points(points, k):
    maxHeap = []

    for i in range(k):
        heappush(maxHeap, points[i])

    for i in range(k, len(points)):
        if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
            heappop(maxHeap)    # used the __lt__
            heappush(maxHeap, points[i])

    return list(maxHeap)


def dist_origin(point):
    return point[0]*point[0] + point[1]*point[1]

def find_closest_points2(points, k):
    maxHeap = []

    for i in range(k):
        dist = dist_origin(points[i])
        heappush(maxHeap, (-dist, points[i]))
    
    for i in range(k, len(points)):
        dist = dist_origin(points[i])
        if -dist > maxHeap[0][0]:
            heappop(maxHeap)
            heappush(maxHeap, (-dist, points[i]))
    
    closest_points = []
    while maxHeap:
        closest_points.append(heappop(maxHeap)[1])
    
    return closest_points




if __name__ == "__main__":
    closest_points = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1), Point(1, 1)], 2)

    for point in closest_points:
        print(point)

    closest_points = find_closest_points2([[1, 3], [3, 4], [2, -1], [1, 1]], 2)

    for point in closest_points:
        print(point)

