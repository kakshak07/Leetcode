class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def helper(p1, p2):
            if(p1>=len(nums1) or p2>=len(nums2)):
                return(0)
            if(nums1[p1] == nums2[p2]):
                return(max(helper(p1+1,p2), helper(p1, p2+1), 1+helper(p1+1,p2+1)))
            else:
                return(max(helper(p1+1,p2), helper(p1, p2+1)))
        return(helper(0,0))
        