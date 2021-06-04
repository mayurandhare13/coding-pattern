import random

def findCeil(arr, r, low, high):
    while low < high:
        mid = low + (high - low) // 2
    
        if r > arr[mid]:
            low = mid + 1
        else:
            high = mid
    
    if arr[low] >= r:
        return low
    
    return -1


def myRandom(arr, freq, prefix):
    n = len(arr)

    r = random.random()

    # find index of ceiling of `r` in prefix array
    idx = findCeil(prefix, r, 0, n - 1)

    return arr[idx]


def setup(arr, freq):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = freq[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + freq[i]
    
    return prefix


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    freq = [0.1, 0.5, 0.2, 0.2]

    prefix = setup(arr, freq)

    for i in range(10):
        print(myRandom(arr, freq, prefix))
