class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, prev, curr = [0] * 10001, 0, 0
        
        for i in nums:
            points[i] += i
        print(points)
        for i in points:
            prev, curr = curr, max(prev+i, curr)
            # print(prev,curr)
        return curr