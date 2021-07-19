def nonDecreasingArray(nums: list) -> bool:
    violations = False

    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            if violations:
                return False

            violations = True

            # try to have min element
            # 3, 7, 5,     6, 8, 9
            if i < 2 or nums[i-2] <= nums[i]:
                nums[i - 1] = nums[i]

            # 4, 5, 3
            else:
                nums[i] = nums[i - 1]
    
    return True


if __name__ == '__main__':
    assert nonDecreasingArray([10, 5, 7]) == True
    assert nonDecreasingArray([3, 4, 5, 3, 6, 8]) == True
    assert nonDecreasingArray([3, 4, 5, 3, 3, 8]) == False
