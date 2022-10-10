class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        w = gcd(*numsDivide)
        
        for i,a in enumerate(sorted(nums)):
            if w % a == 0: return i
            if a > w: break
        return -1
        