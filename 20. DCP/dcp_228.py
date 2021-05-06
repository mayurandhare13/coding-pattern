'''
Inputs: 3 and 30
Lexicographically 30|3 < 3|30, output is 3 then 30
(x+y) > (x-y)
'''

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


def largestNumber(nums):
    nums = list(map(str, nums))
    A = sorted(map(str, nums), key=LargerNumKey)

    return '0' if A[0] == '0' else ''.join(A)

'''
class Comparable:
    def __init__(self, num):
        self.value = str(num)

    def __lt__(self, other):
        return self.value + other.value > other.value + self.value


class Solution:
    def solve(self, nums):
        nums = list(map(Comparable, nums))
        nums.sort()
        return "".join(n.value for n in nums).lstrip("0") or "0"
'''

if __name__ == '__main__':
    num = largestNumber([10, 7, 76, 415])
    print(num)
    num = largestNumber([3,30,34,5,9])
    print(num)
