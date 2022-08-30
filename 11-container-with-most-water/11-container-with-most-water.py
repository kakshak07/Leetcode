class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        
        leftp = 0
        rightp = len(height)-1
        
        while(leftp<rightp):
            t = min(height[leftp],height[rightp])
            t = t*(rightp-leftp)
            if(t>max_area):
                max_area = t
            if(height[leftp]>height[rightp]):
                rightp = rightp-1
            else:
                leftp = leftp+1
        return(max_area)