'''
Permutations (medium)

Given a set of distinct numbers, find all of its permutations.
If a set has 'n' distinct elements it will have n! permutations.
'''

from collections import deque


def find_permutations(nums):
    result = []
    permutations = deque()
    permutations.append([])

    for num in nums:
        # we will take all existing permutations and add the current number to create new permutations
        _len = len(permutations)
        for _ in range(_len):
            oldPermutation = permutations.popleft()
            for i in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                
                # insert new element at every position
                newPermutation.insert(i, num)
                
                if len(newPermutation) == len(nums):
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)

    return result


if __name__ == "__main__":
    print("Here are all the permutations: " +
          str(find_permutations([1, 3, 5])))


# overall time complexity of our algorithm O(N * N!)
