def sumSubarrayMins(A):
    res = 0
    stack = []
    A = [float('-inf')] + A + [float('inf')]
    
    for i, n in enumerate(A):
        while stack and A[stack[-1]] > n:
            cur = stack.pop()
            res += A[cur] * (i - cur) * (cur - stack[-1])
        stack.append(i)
    
    print(stack)
    return res % (10**9 + 7)


def sumSubarrayMaxs(A):
    res = 0
    stack = []
    A = [float('inf')] + A + [float('-inf')]
    
    for i, n in enumerate(A):
        while stack and A[stack[-1]] < n:
            cur = stack.pop()
            res += A[cur] * (i - cur) * (cur - stack[-1])
        stack.append(i)
    
    return res % (10**9 + 7)
    

def getTotalImbalance(weight):
    totalMin = sumSubarrayMins(weight)
    totalMax = sumSubarrayMaxs(weight)
    
    return abs(totalMax - totalMin)
