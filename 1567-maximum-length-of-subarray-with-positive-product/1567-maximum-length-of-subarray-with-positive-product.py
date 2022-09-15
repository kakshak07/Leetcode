class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for nums in nums:
            if nums > 0:
                pos = 1 + pos
                neg = 1 + neg if neg else 0
            elif nums < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos = neg = 0
            ans = max(ans, pos)
            print(ans, pos, neg)
        return ans