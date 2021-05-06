def minComparison(arr):
    mini, maxi = arr[0], arr[0]
    
    if arr[0] < arr[1]:
        mini = arr[0]
        maxi = arr[1]
    else:
        mini = arr[1]
        maxi = arr[0]
    
    for i in range(2, len(arr)):
        if arr[i] < mini:
            mini = arr[i]
        
        elif arr[i] > maxi:
            maxi = arr[i]

    return (mini, maxi)


if __name__ == '__main__':
    pair = minComparison([1000, 11, 445, 1, 330, 3000])
    print(f"MIN: {pair[0]}, MAX: {pair[1]}")

    # can also implement divide and conquer

