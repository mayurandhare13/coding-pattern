'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Sorting the array will take O(N*logN). The `searchPair()` function will take O(N). As we are calling `searchPair()` for every number in the input array, this means that overall searchTriplets() will take O(N*logN + N​^2)
'''

def searchTriplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if (i > 0 and arr[i] == arr[i-1]):
            continue
        searchPairs(arr, -arr[i], i+1, triplets)
    return triplets


def searchPairs(arr, targetSum, left, triplets):
    right = len(arr) - 1
    while (left < right):
        currentSum = arr[left] + arr[right]
        if (currentSum == targetSum):
            triplets.append([-targetSum, arr[left], arr[right]])
            left += 1
            right -= 1
            while (left < right and arr[left] == arr[left - 1]):
                left += 1
            while (left < right and arr[right] == arr[right + 1]):
                right -=1
        elif (currentSum < targetSum):
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    print(searchTriplets([-3, 0, 1, 2, -1, 1, -2]))
    print(searchTriplets([-5, 2, -1, -2, 3]))
