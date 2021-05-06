import math

# k: eggs
# n: floors
def minDrops(k, n):
    # if base/first floor
    if n == 0 or n == 1:
        return n
    
    # if only one egg then we need all n floors trials
    if k == 1:
        return n
    
    mini = math.inf
    for i in range(1, n + 1):
        mini = min(
            mini, max(minDrops(k-1, i-1), minDrops(k, n-i))
        )
    
    return 1 + mini


if __name__ == '__main__':
    print(minDrops(1, 5))
    print(minDrops(2, 20))
    print(minDrops(3, 15))
