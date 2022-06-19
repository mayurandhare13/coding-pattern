'''
Staircase

Given a stair with 'n' steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take `1` step, `2` steps, or `3` steps.

Number of stairs (n) : 4
Number of ways = 7
Explanation: Following are the seven ways we can climb:- 
{1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1}, {2,2}, {1,3}, {3,1}
'''

def count_ways(stairs):
    # 1. base case
    # we don't need to take anymore steps. we are at the last step
    if stairs == 0:
        return 1

    # we take 1 step to reach end. that is the only way
    if stairs == 1:
        return 1

    # we can take {1, 1} or {2} --> 2 ways to reach last step
    if stairs == 2:
        return 2

    # only possible options {1, 2, 3}
    n1 = count_ways(stairs - 1)
    n2 = count_ways(stairs - 2)
    n3 = count_ways(stairs - 3)

    return n1 + n2 + n3


if __name__ == "__main__":
    print(count_ways(3))
    print(count_ways(4))
    print(count_ways(5))
