class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        def chori(arr):
            chori = 0
            not_chori = 0
            for i in arr:
                chori, not_chori = not_chori + i, max(chori, not_chori)
            return max(chori, not_chori)
        
        
#         def chori(arr):
#             print(arr)
#             dp = [0] * len(arr)
            
#             dp[0] = arr[0]
#             dp[1] = max(arr[0], arr[1])
#             for i in range(2, len(arr)):
#                 dp[i] = max(dp[i-2] + arr[i] , arr[i-1])
#             # print(max(dp), arr)
#             return max(dp)
        return max(chori(nums[1:]), chori(nums[:-1]))
                