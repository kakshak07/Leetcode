class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        defDict = collections.defaultdict(int)
        answer = 0
        for i in nums1:
            for j in nums2:
                defDict[i+j] += 1
        for i in nums3:
            for j in nums4:
                answer += defDict[-i-j]
        return answer
            