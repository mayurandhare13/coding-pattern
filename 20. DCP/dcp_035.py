def dutchFlag(arr: list):
    # all elements < low are 'R', and all elements > high are 'B'
    low, high = 0, len(arr) - 1
    i = 0

    while i <= high:
        if arr[i] == 'R':
            arr[low], arr[i] = arr[i], arr[low]
            low += 1
            i += 1
        
        elif arr[i] == 'G':
            i += 1
        
        else:
            arr[high], arr[i] = arr[i], arr[high]
            high -= 1
            # after the swap.. the char at index 'i' could be 'R', 'G' or 'B'


if __name__ == '__main__':
    arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    dutchFlag(arr)
    assert arr == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
