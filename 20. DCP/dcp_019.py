from copy import deepcopy
from sys import maxsize

# O(k^n)
def minPaintHouseHelper(costs: list[list], result: list, currHouse, prevColor, currCost):
    if currHouse == len(costs):
        result.append(currCost)
        return
    
    for i in range(len(costs[0])):
        if i != prevColor:
            minPaintHouseHelper(costs, result, currHouse + 1, i, currCost + costs[currHouse][i])


def minPaintHouse(costs: list[list]) -> int:
    result = []
    minPaintHouseHelper(costs, result, 0, -1, 0)
    return min(result)


# ---------------------------------------------------------------
# O(n*k*k)
def paintHouse(costs: list[list]) -> int:
    n = len(costs)      # houses
    k = len(costs[0])   # colors

    for i in range(1, n):
        for j in range(0, k):
            prevColor = maxsize

            for p in range(0, k):
                if p != j:
                    prevColor = min(prevColor, costs[i-1][p])
            
            costs[i][j] += prevColor
    
    return min(costs[-1])

# ---------------------------------------------------------------

# O(n*k)
def paintHouse2(costs: list[list]) -> int:
    n = len(costs)      # houses
    k = len(costs[0])   # colors

    least, secLeast = maxsize, maxsize

    # process first house
    for i in range(k):
        if costs[0][i] <= least:
            secLeast = least
            least = costs[0][i]
        
        elif costs[0][i] <= secLeast:
            secLeast = costs[0][i]
    
    for i in range(1, n):
        newLeast, newSecLeast = maxsize, maxsize

        for j in range(k):
            if costs[i-1][j] == least:
                costs[i][j] += secLeast

            else:
                costs[i][j] += least

            # find lease and second least for current til current house
            if costs[i][j] <= newLeast:
                newSecLeast = newLeast
                newLeast = costs[i][j]

            elif costs[i][j] <= newSecLeast:
                newSecLeast = costs[i][j]

        least = newLeast
        secLeast = newSecLeast

    return least


if __name__ == '__main__':
    costs = [[1,2,3,4], [1,2,1,0], [6,1,1,5], [2,3,5,5]]
    assert minPaintHouse(costs) == 4

    costs = [
        [7, 3, 8, 6, 1, 2],
        [5, 6, 7, 2, 4, 3],
        [10, 1, 4, 9, 7, 6],
        [10, 1, 4, 9, 7, 6]
    ]
    assert paintHouse(deepcopy(costs)) == 8
    assert paintHouse2(deepcopy(costs)) == 8
