'''
Find the Duplicate Number (easy)

We are given an unsorted array containing 'n+1' numbers taken from the range 1 to 'n'. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Input: [1, 4, 4, 3, 2]
Output: 4
'''


def find_duplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1

    return -1

def find_duplicate2(nums):
    slow, fast = nums[0], nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
        
    curr = nums[0]
    while curr != slow:
        curr = nums[curr]
        slow = nums[slow]
    
    return curr


if __name__ == "__main__":
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate2([1, 3, 4, 2, 2]))



'''
[1, 5, 4, 3]
nums[0] = 1                     nums[i]
nums[nums[0] - 1] = nums[0]     nums[nums[i] - 1] = nums[i] --> nums[j] = nums[i] - 1
'''