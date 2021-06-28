def trappedWater(heights: list) -> int:
    totalWater = 0
    size = len(heights)

    leftMax = [0] * size
    rightMax = [0] * size

    leftMax[0] = heights[0]

    for i in range(1, size):
        leftMax[i] = max(heights[i], leftMax[i-1])

    rightMax[size-1] = heights[size - 1]

    for i in range(size-2, -1, -1):
        rightMax[i] = max(heights[i], rightMax[i+1])

    for i in range(1, size - 1):
        totalWater += min(leftMax[i], rightMax[i]) - heights[i]

    return totalWater


if __name__ == '__main__':
    assert trappedWater([1, 2, 0, 1, 2]) == 3
    assert trappedWater([2, 1, 2]) == 1
    assert trappedWater([3, 0, 1, 3, 0, 5]) == 8
