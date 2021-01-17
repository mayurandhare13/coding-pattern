'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
'''

def combinationSum(k, n):
    results = []

    def backtrack(remain, subset, start):
        if remain == 0 and len(subset) == k:
            results.append(list(subset))
            return

        if remain < 0 or len(subset) == k:
            # exceeds the scopes. no need to explore further
            return

        # iterate over the reduced list of candidates
        for i in range(start, 9):
            subset.append(i+1)
            
            backtrack(remain-i-1, subset, i+1)
            
            # backtrack the current choice
            subset.pop()

    backtrack(n, [], 0)
    return results


if __name__ == "__main__":
    print(combinationSum(k = 3, n = 7))
    print(combinationSum(k = 3, n = 9))
    print(combinationSum(k = 3, n = 2))
    print(combinationSum(k = 9, n = 45))
