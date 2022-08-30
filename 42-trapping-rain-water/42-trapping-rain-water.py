class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        left_max.append(height[0])
        curmax=height[0]
        for i in range(1,len(height)):
            if(curmax<height[i]):
                curmax=height[i]
            left_max.append(curmax)
        curmax=height[len(height)-1]
        right_max.append(curmax)
        for i in range(len(height)-2,-1,-1):
            if(curmax<height[i]):
                curmax=height[i]
            right_max.append(curmax)
        right_max = right_max[::-1]
        counter = 0
        # print(right_max)
        # print(left_max)
        for i in range(len(height)):
            t = min(right_max[i], left_max[i])-height[i]
            # print(t)
            if(t>0):
                counter+=t
        return(counter)