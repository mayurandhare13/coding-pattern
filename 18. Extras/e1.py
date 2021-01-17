class Solution:
    def canJump(self, nums):
        return self.canJumpHelper(nums, 0)
    
    # works, but takes lot of time :(
    def canJumpHelper(self, nums, index):
        N = len(nums)
        
        if index >= N - 1:
            return True
        
        if nums[index] == 0:
            return False
        
        possible_jumps = index + nums[index]
        for i in range(possible_jumps, index , -1):
            if self.canJumpHelper(nums, i):
                return True
        
        return False


    def canJump2(self, nums):
        if len(nums) <= 1:
            return True
        
        possible_jumps = nums[0]
        c = 0
        while c <= possible_jumps:
            if possible_jumps >= len(nums) - 1:
                return True
            
            # at any moment, I could have c + nums[c] jump indices
            # or possible jumps from previous index option
            possible_jumps = max(possible_jumps, c + nums[c])
            c += 1
        
        return False
    

if __name__ == "__main__":
    s = Solution()
    print(s.canJump2([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))

    print(s.canJump2([2,3,1,1,4]))