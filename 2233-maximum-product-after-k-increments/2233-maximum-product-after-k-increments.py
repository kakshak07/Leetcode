import heapq
class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        # print()
        for i in range(k):
            t = heapq.heappop(nums)
            t = t + 1
            heapq.heappush(nums,t)
        prod = 1
        for i in nums:
            prod = (prod * i)%(10**9 + 7)
        return prod
            
        