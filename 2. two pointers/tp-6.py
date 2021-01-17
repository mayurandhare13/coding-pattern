'''
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
'''

import math

def triplet_sum_close_to_target(arr, targetSum):
    arr.sort()
    smallestDiff = math.inf
    for i in range(len(arr) - 2): # arr[i], {left} -> arr[i-2], arr[i-1]
        left = i + 1
        right = len(arr) - 1
        while left < right:
            targetDiff = targetSum - arr[i] - arr[left] - arr[right]
            if targetDiff == 0:         # triplet with exact sum
                return targetSum        # smallestDiff
            
            # if abs(targetDiff) < abs(smallestDiff) or \
            #     (abs(targetDiff) == abs(smallestDiff) and targetDiff > smallestDiff):
            
            if abs(targetDiff) < abs(smallestDiff):
                smallestDiff = targetDiff
            
            if targetDiff > 0:
                left += 1           # we need triplet with bigger sum
            else:
                right -= 1          # we need triplet with smaller sum
    
    return targetSum - smallestDiff


if __name__ == "__main__":
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
    print(triplet_sum_close_to_target([1, 1, 1, 0], -100))
