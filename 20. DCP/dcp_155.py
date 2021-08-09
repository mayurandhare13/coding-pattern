def majority(nums: list):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate


if __name__ == '__main__':
    assert majority([1, 2, 1, 1, 1, 4, 0]) == 1
    assert majority([3, 2, 3]) == 3
    assert majority([2, 2, 1, 1, 1, 2, 2]) == 2
