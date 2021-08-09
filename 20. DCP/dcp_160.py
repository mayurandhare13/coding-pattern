from math import inf


class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


def longestPath(root):
    _, path = longestHeightPath(root)
    return path


def longestHeightPath(root):
    longestPathSumSoFar = -inf
    highest, secondHighest = 0, 0

    for child, weight in root.children:
        height, longestPathSum = longestHeightPath(child)

        longestPathSumSoFar = max(longestPathSumSoFar, longestPathSum)

        if height + weight > highest:
            highest, secondHighest = height + weight, highest

        elif height + weight > secondHighest:
            secondHighest = height + weight


    return highest, max(longestPathSumSoFar, highest + secondHighest)


if __name__ == '__main__':

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')

    e.children = [(g, 1), (h, 1)]
    d.children = [(e, 2), (f, 4)]
    a.children = [(b, 3), (c, 5), (d, 8)]

    assert longestPath(a) == 17
