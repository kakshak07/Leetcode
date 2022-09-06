class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        func_sum = 0
        arr_sum = sum(nums)
        for i,j in enumerate(nums):
            func_sum += i*j
        max_sum = func_sum
        
        for i in range(1, len(nums)):
            func_sum = func_sum + arr_sum - len(nums)*nums[-i]
            max_sum = max(max_sum, func_sum)
        return(max_sum)
        