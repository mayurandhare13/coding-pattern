import sys

def largestTowerRange(listners: list, towers: list) -> int:
    l_len = len(listners)
    t_len = len(towers)

    # compare listerners distance from its left and right towers respectively
    leftTower = -sys.maxsize - 1
    rightTower = towers[0]

    l, t = 0, 0
    maxRange = 0

    while l < l_len:
        if listners[l] < rightTower:
            left = listners[l] - leftTower
            right = rightTower - listners[l]

            localMax = left if left < right else right
            maxRange = max(maxRange, localMax)

            l += 1
        
        else:
            leftTower = towers[t]
            t += 1
            if t < t_len:
                rightTower = towers[t]
            else:
                rightTower = sys.maxsize
    
    return maxRange


if __name__ == '__main__':
    listeners = [1, 5, 11, 20]
    towers = [4, 8, 15]

    assert largestTowerRange(listeners, towers) == 5
    assert largestTowerRange([12, 13, 11, 80], [4, 6, 15, 60]) == 20

