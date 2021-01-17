'''
Fibonacci numbers
'''

def calcFibonacciHelper(dp, num):
    if num < 2:
        return num
    
    if dp[num] == -1:
        dp[num] = calcFibonacciHelper(dp, num-1) + \
                    calcFibonacciHelper(dp, num-2)
    
    return dp[num]


def calcFibonacci(num):
    dp = [-1 for _ in range(num + 1)]
    return calcFibonacciHelper(dp, num)


if __name__ == "__main__":
    print("5th fibonacci number -> ", calcFibonacci(5))
    print("6th fibonacci number -> ", calcFibonacci(6))
    print("7th fibonacci number -> ", calcFibonacci(7))
