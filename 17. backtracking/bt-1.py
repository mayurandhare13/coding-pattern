'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
  [7],
  [2,2,3]
'''


def combinationSum(candidates, target):
    result = []

    def backtrack(remain, subset, start):
        if remain < 0:
            return

        if remain == 0:
            result.append(list(subset))
            return
        
        for i in range(start, len(candidates)):
            subset.append(candidates[i])
            
            # give current number another chance to find exact subset
            backtrack(remain - candidates[i], subset, i)

            # to choose another number | remove current
            subset.pop()
    
    backtrack(target, [], 0)
    return result


if __name__ == "__main__":
    print(combinationSum([2, 3, 6, 7], target = 7))
    print(combinationSum([2, 3, 5], target = 8))
