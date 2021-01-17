'''
Minimum jumps with fee
Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you take the step.
calculate the minimum fee required to reach the top of the staircase (beyond the top-most step)
At every step, you have an option to take either 1 step, 2 steps, or 3 steps. 
You should assume that you are standing at the first step.

Number of stairs (n) : 6
Fee: {1,2,5,2,1,2}
Output: 3
Explanation: Starting from index '0', we can reach the top through: 0->3->top
The total fee we have to pay will be (1+2).
'''

def find_min_fee_helper(fees, index):
    if index >= len(fees):
        return 0

    min1 = find_min_fee_helper(fees, index + 1)
    min2 = find_min_fee_helper(fees, index + 2)
    min3 = find_min_fee_helper(fees, index + 3)

    return fees[index] + min(min1, min2, min3)

def find_min_fee(fees):
    return find_min_fee_helper(fees, 0)


if __name__ == "__main__":
    print(find_min_fee([1,2,5,2,1,2]))
