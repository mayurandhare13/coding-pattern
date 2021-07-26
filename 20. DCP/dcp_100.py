# since we can move in all directions. diagonal = vertical = horizontal distance
def getMinDistance(x1, y1, x2, y2):
    # get diagonal distance component
    dist1 = min(abs(x2 - x1), abs(y2 - y1))

    # get horizontal/vertical distance component
    dist2 = max(abs(x2 - x1), abs(y2 - y1)) - dist1

    return dist1 + dist2


def coverPoints(coordinates: list):
    total = len(coordinates)

    distance = 0
    for i in range(1, total):
        x1, y1 = coordinates[i - 1]
        x2, y2 = coordinates[i]
        distance += getMinDistance(x1, y1, x2, y2)

    return distance


if __name__ == '__main__':
    assert coverPoints([(0, 0), (1, 1), (1, 2)]) == 2
    assert coverPoints([(0, 0), (1, 1), (1, 2), (3, 6)]) == 6
