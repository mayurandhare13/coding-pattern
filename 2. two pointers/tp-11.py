'''
Quadruple Sum to Target (medium)

Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.  
O(N*logN+N^3)

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
'''

def search_quadruplets(arr, target):
    arr.sort()
    quadruples = []
    for i in range(len(arr)-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue                            # avoid duplicate
        for j in range(i+1, len(arr)-2):
            if j > i+1 and arr[j] == arr[j-1]:
                continue                        # avoid duplicate
            search_pairs(arr, i, j, target, quadruples)
    return quadruples


def search_pairs(arr, first, second, target, quadruples):
    left, right = second+1, len(arr)-1
    while(left < right):
        current_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if current_sum == target:
            quadruples.append([arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1                       # avoid duplicate
            while left < right and arr[right] == arr[right+1]:
                right -= 1                      # avoid duplicate
        elif current_sum < target:
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))
