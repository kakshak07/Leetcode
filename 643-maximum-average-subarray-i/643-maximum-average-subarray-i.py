import math
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    	M = d = 0
    	for i in range(len(nums)-k):
    		d += nums[i+k] - nums[i]
    		if d > M: M = d
    	return (sum(nums[:k])+M)/k
        