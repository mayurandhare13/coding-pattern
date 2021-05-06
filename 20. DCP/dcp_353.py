def largestRectangleArea(heights: list[int]) -> int:
    maxArea = 0
    hStack, pStack = [], []
    heights.append(0)
    
    for i in range(len(heights)):
        lastWidth = len(heights) + 1
        while hStack and hStack[-1] > heights[i]:
            lastWidth = pStack[-1]
            currArea = (i - pStack.pop()) * hStack.pop()
            maxArea = max(maxArea, currArea)
        
        if not hStack or hStack[-1] < heights[i]:
            hStack.append(heights[i])
            pStack.append(min(i, lastWidth))
    
    return maxArea


if __name__ == '__main__':
    print(largestRectangleArea([1, 3, 2, 5]))
