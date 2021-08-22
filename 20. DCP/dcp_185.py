def area(L1, R1, L2, R2):
    x, y = 0, 1
    X = min(R1[x], R2[x]) - max(L1[x], L2[x])
    Y = max(R1[y], R2[y]) - min(L1[y], L2[y])

    return abs(X * Y)


def overlapArea(rect1: dict, rect2: dict):
    L1 = rect1['topLeft']
    dimensions1 = rect1['dimensions']
    R1 = (L1[0] + dimensions1[0],
                    L1[1] - dimensions1[1])

    print(L1, ' ', R1)

    L2 = rect2['topLeft']
    dimensions2 = rect2['dimensions']
    R2 = (L2[0] + dimensions2[0],
                    L2[1] - dimensions2[1])

    print(L2, ' ', R2)

    return area(L1, R1, L2, R2)


if __name__ == '__main__':
    assert overlapArea({
        "topLeft": (1, 4),
        "dimensions": (3, 3)
        }, {
            "topLeft": (0, 5),
            "dimensions": (4, 3)
        }) == 6

    r1 = {"topLeft": (0, 5), "dimensions": (5, 5)}
    r2 = {"topLeft": (1, 4), "dimensions": (2, 2)}
    assert overlapArea(r1, r2) == 4
