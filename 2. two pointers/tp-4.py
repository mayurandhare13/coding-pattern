'''
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

time complexity O(n)
'''


def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highestSqIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSq = arr[left] * arr[left]
        rightSq = arr[right] * arr[right]
        if leftSq > rightSq:
            squares[highestSqIdx] = leftSq
            left += 1
        else:
            squares[highestSqIdx] = rightSq
            right -= 1
        highestSqIdx -= 1

    return squares


if __name__ == "__main__":
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))
