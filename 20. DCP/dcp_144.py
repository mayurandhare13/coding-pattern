# O(N)
def nearestLargest(nums: list, i):
    # j --> distance from i
    for j in range(1, len(nums)):
        low = i - j
        high = i + j
        if low >= 0 and nums[low] > nums[i]:
            return low
        
        if high < len(nums) and nums[high] > nums[i]:
            return high
    
    return None

# ------------------------------------------------------

def _preprocess(nums: list):
    stack, res = [], [-1] * len(nums)

    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            res[stack.pop()] = i

        stack.append(i)

    # fill up missing -1
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            res[stack.pop()] = i
        
        if not stack:
            break

    return res


def nearestLargest2(nums: list):
    cache = _preprocess(nums)

    for i in range(len(nums)):
        print(f"{i} --> {cache[i]}")


if __name__ == '__main__':
    print(nearestLargest([4, 1, 3, 5, 6], 0))
    nearestLargest2([4, 1, 3, 5, 6])
