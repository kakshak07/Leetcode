class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        t= []
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                t.append(nums1[i])
        t1= []
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                t1.append(nums2[i])
        return([list(set(t)),list(set(t1))])
        