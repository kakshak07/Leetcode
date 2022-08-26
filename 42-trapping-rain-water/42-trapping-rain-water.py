class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_level = 0
        water = 0
        
        while left < right:
            curr_level = min(height[left], height[right])
            max_level = max(max_level, curr_level)
            if height[left] > max_level:
                water = water + max(0, max_level - height[right])
                right -= 1
            else:
                water = water + max(0, max_level - height[left])
                left += 1
                
        return water