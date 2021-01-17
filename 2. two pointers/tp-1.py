'''
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

time complexity O(n)
'''

def pair_with_targetsum(arr, target_sum):
  left, right = 0, len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:
      return [left, right]

    if target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum
  return [-1, -1]



# Search for ‘Y’ (which is equivalent to “Target−X”) in the HashTable
def pair_with_targetsum2(arr, target_sum):
  nums_map = {}  # to store numbers and their indices
  for i, num in enumerate(arr):
    if target_sum - num in nums_map:
      return [nums_map[target_sum - num], i]
    else:
      nums_map[arr[i]] = i
  return [-1, -1]


if __name__ == "__main__":
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum2([2, 5, 9, 11], 11))
