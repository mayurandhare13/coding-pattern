'''
MAXIMUM Ribbon Cut
We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. Now we need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.
'''

import math

def count_ribbon_pieces_helper(ribbonLengths, total, index):
    if total == 0:
        return 0
    
    if index >= len(ribbonLengths):
        return -math.inf

    count1 = -math.inf
    if ribbonLengths[index] <= total:
        res = count_ribbon_pieces_helper(
                ribbonLengths, total - ribbonLengths[index], index
            )
        if res != -math.inf:
            count1 = 1 + res
    
    count2 = count_ribbon_pieces_helper(ribbonLengths, total, index + 1)

    return max(count1, count2)

def count_ribbon_pieces(lengths, total):
    result = count_ribbon_pieces_helper(lengths, total, 0)
    return -1 if result == -math.inf else result


if __name__ == "__main__":
    print(count_ribbon_pieces([2, 3, 5], 5))
    print(count_ribbon_pieces([2, 3], 7))
    print(count_ribbon_pieces([3, 5, 7], 13))
    print(count_ribbon_pieces([3, 5], 7))
