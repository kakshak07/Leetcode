import random
class Solution:

    def __init__(self, nums: List[int]):
        self.org = nums.copy()
        self.t = nums.copy()
    def reset(self) -> List[int]:
        self.t =self.org.copy()
        return self.t

    def shuffle(self) -> List[int]:
        
        random.shuffle(self.t)
        return self.t


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()