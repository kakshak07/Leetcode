class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        
        for i in range(n):
            nums.append(start+2*i)
        
        if len(nums)>1:
            x = nums[0] ^ nums[1]
        else:
            return nums[0]
        for i in range(2,len(nums)):
            x = x ^ nums[i]
        return x
            
        