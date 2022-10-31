class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        total = 0
        
        result = float("inf")
        
        while right<len(nums):
            total += nums[right]
            while total>=target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        if result == float("inf"):
            return 0
        return result
        