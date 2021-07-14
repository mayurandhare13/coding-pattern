from math import pow
'''
Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc
'''

def powerSet(set):
    setSize = len(set)
    powerSetSize = int(pow(2, setSize))

    result = []

    # Run from counter 000..0 to 111..1
    for counter in range(powerSetSize):
        tmp = []
        for j in range(setSize):
            if counter & (1 << j) != 0:
                tmp.append(set[j])

        result.append(tmp)

    return result


def powerSet2(nums: list):
    result = []
    result.append([])

    for num in nums:
        _len = len(result)

        for i in range(_len):
            _set = list(result[i])
            _set.append(num)

            result.append(_set)

    return result


if __name__ == '__main__':
    assert powerSet([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    
    assert powerSet2([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
