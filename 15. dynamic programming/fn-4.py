'''
Minimum jumps to reach the end

Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element.
write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

Input = {1,1,3,6,9,3,0,1,3}
Output = 4
Explanation: Starting from index '0', 
we can reach the last index through: 0->1->2->3->8
'''

import math

def count_min_jumps_helper(jumps, index):
    if index >= len(jumps) - 1:
        return 0

    if jumps[index] == 0:
        return math.inf
    
    total_jumps = math.inf
    start, end = index + 1, index + jumps[index]
    while start < len(jumps) and start <= end:
        min_jumps = count_min_jumps_helper(jumps, start)
        if min_jumps != math.inf:
            total_jumps = min(total_jumps, min_jumps + 1)
        
        start += 1
    
    return total_jumps


def count_min_jumps(jumps):
    return count_min_jumps_helper(jumps, 0)


if __name__ == "__main__":
    print(count_min_jumps([2,1,1,1,4]))
    print(count_min_jumps([1,1,3,6,9,3,0,1,3]))
