class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if i%10 == nums[i]%10:
                return i
            
        return -1
        