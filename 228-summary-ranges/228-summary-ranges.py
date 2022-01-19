class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res, i = [], 0
        while i < len(nums):
            tmp = nums[i]
            j = i
            while j < len(nums):
                if nums[j] == tmp:
                    tmp += 1
                else:
                    tmp -= 1
                    val = f"{nums[i]}->{tmp}" if nums[i] != tmp else f"{nums[i]}"
                    res.append(val)
                    i = j
                    break
                j += 1
            else:
                tmp -= 1
                val = f"{nums[i]}->{tmp}" if nums[i] != tmp else f"{nums[i]}"
                res.append(val)
                i = j
                    
        return res