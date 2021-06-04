def getFixedPoint(nums: list):
    for i, val in enumerate(nums):
        if i == val:
            return i
    
    return False


if __name__ == "__main__":
    print(getFixedPoint([-6, 0, 2, 40]))
    print(getFixedPoint([1, 5, 7, 8]))
