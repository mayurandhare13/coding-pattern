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

    for i in range(k):
        # remove all previous small element's index
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()

        deq.append(i)


    for i in range(k, len(nums)):
        # front of deque has largest index
        print(nums[deq[0]], end=' ')

        # remove OOB elements
        while deq and deq[0] < i-k+1:
            deq.popleft()


        # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()

        deq.append(i)
    
    # print max element from last window
    print(nums[deq[0]])


if __name__ == '__main__':
    maxSlidingWindowBrute([10, 5, 2, 7, 8, 7], 3) # 10 7 8 8
    maxSlidingWindow([10, 5, 2, 7, 8, 7], 3) # 10 7 8 8
