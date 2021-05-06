import math

'''
It could also be possible that two negative numbers lying at the left extreme end could also contribute to lead to a larger product if the third number in the triplet being considered is the largest positive number in the nums array.

(if Sorted) nums[0]×nums[1]×nums[n−1] or nums[n−3]×nums[n−2]×nums[n−1] will give the required result.
'''

def maximumProduct(nums: list[int]) -> int:
    min1, min2 = math.inf, math.inf
    max1, max2, max3 = -math.inf, -math.inf, -math.inf
    
    for n in nums:
        if n <= min1:
            min2 = min1
            min1 = n

        elif n < min2:
            min2 = n

        if n > max1:
            max3 = max2
            max2 = max1
            max1 = n

        elif n > max2:
            max3 = max2
            max2 = n

        elif n > max3:
            max3 = n

    return max(min1 * min2 * max1, 
                max3 * max2 * max1)


if __name__ == '__main__':
    print(maximumProduct([1,2,3,4]))
    print(maximumProduct([-10, -10, 5, 2]))
