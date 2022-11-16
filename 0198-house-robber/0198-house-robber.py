class Solution:
    def rob(self, nums: List[int]) -> int:
        
        t = [0 for i in nums]
        if len(nums)==1:
            return max(nums)
        if len(nums)>1:
            t[0], t[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # print(t[i], nums[i-2])
            t[i] = max(nums[i]+t[i-2], t[i-1])
            
        # print(t)
        return max(t)
                # dp = [0]*length # assign dp array
        # t[0], t[1] = nums[0], max(nums[0], nums[1])
        
#         for i in range(2, length):
#             dp[i] = max(dp[i-2]+nums[i], dp[i-1])
#         print(dp)
        
#         return max(dp)