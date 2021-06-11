def productExceptSelf(nums):
    size = len(nums)

    ans, L, R = [0] * size, [0] * size, [0] * size

    L[0] = 1
    for i in range(1, size):
        L[i] = L[i - 1] * nums[i - 1]
    
    R[size - 1] = 1

    for i in range(size - 2, -1, -1):
        R[i] = R[i + 1] * nums[i + 1]
    
    for i in range(size):
        ans[i] = L[i] * R[i]

    return ans

if __name__ == '__main__':
    ans = productExceptSelf([1, 2, 3, 4, 5])
    print(ans)
    
    ans = productExceptSelf([3, 2, 1])
    print(ans)
