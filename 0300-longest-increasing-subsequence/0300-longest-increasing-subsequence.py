class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
#         arrNum = [1]*len(nums)
#         # arrNum[-1] = 1
        
#         for i in range(len(nums)-2,-1,-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i]<nums[j]:
#                     arrNum[i] = max(arrNum[i], 1 + arrNum[j])
#         return max(arrNum)
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            l, r = 0, size
            while l != r:
                m = l + (r - l) // 2
                if tails[m] < num:
                    l = m + 1
                else:
                    r = m
            tails[l] = num
            size = max(size, l + 1)
        return size