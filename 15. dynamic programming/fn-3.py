'''
Number factors
Given a number 'n', implement a method to count how many possible ways there are to express 'n' as the sum of 1, 3, or 4.

n : 5
Number of ways = 6
Explanation: Following are the six ways we can express 'n' : 
{1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1}, {1,4}, {4,1}
'''

def count_ways(num):

    if num == 0:                # there is only 1 way
        return 1
    
    if num == 1 or num == 2:    # there is only 1 way
        return 1

    if num == 3:                # 3 --> {1, 1, 1} & {3}
        return 2

    # only possible options {1, 3, 4}
    n1 = count_ways(num - 1)
    n2 = count_ways(num - 3)
    n3 = count_ways(num - 4)

    return n1 + n2 + n3


if __name__ == "__main__":
    print("num 4 -> ", count_ways(4))
    print("num 5 -> ", count_ways(5))
    print("num 6 -> ", count_ways(6))
