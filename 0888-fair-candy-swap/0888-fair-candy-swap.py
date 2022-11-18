class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        i = 0
        j = 0
        aliceSizes.sort()
        bobSizes.sort()
        disff = (sum(aliceSizes) - sum(bobSizes))//2
        
        while i<len(aliceSizes) and j < len(bobSizes):
            temp = aliceSizes[i] - bobSizes[j]
            if temp == disff:
                return ([aliceSizes[i], bobSizes[j]])
            if temp < disff:
                i += 1
            else:
                j += 1
        
        