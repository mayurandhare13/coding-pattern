def mergeSort(enum: list, out: list):
    mid = len(enum) // 2
    if mid:
        left, right = mergeSort(enum[:mid], out), mergeSort(enum[mid:], out)
        merged = []
        m, n = len(left), len(right)
        i = j = 0
        nums_right_smaller = 0

        while i < m and j < n:
            if left[i][1] > right[j][1]:
                nums_right_smaller += 1
                merged.append(right[j])
                j += 1
            
            else:
                out[left[i][0]] += nums_right_smaller
                merged.append(left[i])
                i += 1
        
        while i < m:
            out[left[i][0]] += nums_right_smaller
            merged.append(left[i])
            i += 1
        
        while j < n:
            merged.append(right[j])
            j += 1
        
        enum = merged

    return enum


def smallerCounts(nums: list) -> list:
    smaller = [0] * len(nums)
    mergeSort(list(enumerate(nums)), smaller)
    return smaller

if __name__ == '__main__':
    assert smallerCounts([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
