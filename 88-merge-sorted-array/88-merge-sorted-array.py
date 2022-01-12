class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if nums2==[]:
            return nums1
        for i in range(m,len(nums1)):
            nums1[i]=nums2[i-m]
        nums1.sort()
        print(nums1)
