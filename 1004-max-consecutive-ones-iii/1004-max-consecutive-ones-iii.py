class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        flipped = 0
        answer = 0
        while end<len(nums):
            if nums[end] == 1:
                end += 1
            elif nums[end] == 0 and flipped<k:
                end += 1
                flipped += 1
            else:
                if nums[start] == 0:
                    flipped -= 1
                start += 1
            answer = max(answer, end-start)
        return answer
                