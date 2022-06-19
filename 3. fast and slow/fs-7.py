'''
Cycle in a Circular Array (hard) #
We are given an array containing positive and negative numbers. Suppose the array contains a number 'M' at a particular index. Now, if 'M' is positive we will move forward 'M' indices and if 'M' is negative move backwards 'M' indices. 
NOTE It should follow only one direction. (Forward or Backward)

Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
'''


def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        fast, slow = i, i

        # if slow or fast becomes '-1' this means we can't find cycle for this number
        while True:
            slow = find_next_index(arr, is_forward, slow)
            fast = find_next_index(arr, is_forward, fast)
            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)
            if slow == -1 or fast == -1 or slow == fast:
                break
            
        if slow != -1 and slow == fast:
            return True

    return False


def find_next_index(arr, exp_direction, cur_index):
    direction = arr[cur_index] >= 0
    if exp_direction != direction:
        return -1       # change in direction, return -1
    
    next_index = (cur_index + arr[cur_index]) % len(arr)

    # one element cycle, return -1
    if next_index == cur_index:
        return -1
    
    return next_index


if __name__ == "__main__":
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))
