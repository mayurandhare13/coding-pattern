from collections import deque

# O(Nk)
def maxSlidingWindowBrute(nums: list, k: int) -> None:
    n = len(nums)

    for i in range(n - k + 1):
        print(max(nums[i : i+k]), end=' ')
    
    print()


def maxSlidingWindow(nums: list, k: int) -> None:
    # store nums[index] in in decresing order 
    deq = deque()
    result = []

    for i, val in enumerate(nums):
        # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while deq and nums[deq[-1]] <= val:
            deq.pop()

        deq.append(i)

        # remove OOB elements
        if i - deq[0] >= k:
            deq.popleft()

        # skipping elements if less than K window
        if i + 1 >= k:
            # front of deque has largest index
            result.append(nums[deq[0]])

    print(result)


if __name__ == '__main__':
    maxSlidingWindowBrute([10, 5, 2, 7, 8, 7], 3) # 10 7 8 8
    maxSlidingWindow([10, 5, 2, 7, 8, 7], 3) # 10 7 8 8
