'''
If a point lies left (or right) of all edges of a polygon whose edges are in anticlockwise (or clockwise) direction then we can say point is inside Polygon. 

A point p(x, y) lies on the _ of line segment
    Left  : Ax + By + C > 0
    Right : Ax + By + C < 0
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


'''
Line: Ax + By + C = 0
    A = -(y2 - y1)
    B = (x2 - x1)
    C = -(Ax1 + By1)
'''
def inPolygon(polygon, point):
    A, B, C = [], [], []
    size = len(polygon)

    for i in range(size):
        p1 = polygon[i]
        p2 = polygon[(i+1) % size]

        a = -(p2.y - p1.y)
        b = p2.x - p1.x
        c = -(a * p1.x + b * p1.y)

        A.append(a)
        B.append(b)
        C.append(c)
    
    D = []
    for i in range(len(A)):
        d = A[i] * point.x + B[i] * point.y + C[i]
        D.append(d)
    
    t1 = all(d >= 0 for d in D)
    t2 = all(d <= 0 for d in D)

    return t1 or t2


if __name__ == '__main__':
    polygon = [
        Point(0, 0), Point(5, 0), Point(6, 7),
        Point(2, 3), Point(0, 4)
    ]

    print(inPolygon(polygon, Point(1, 1)))
    print(inPolygon(polygon, Point(6, 2)))
    print(inPolygon(polygon, Point(0, 4)))
