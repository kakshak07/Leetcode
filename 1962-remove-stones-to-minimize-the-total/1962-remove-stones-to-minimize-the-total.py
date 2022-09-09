class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        
        
        for i in range(len(piles)):
            piles[i] = -piles[i]
        l = piles  
        heapq.heapify(l)
        for i in range(k):
            t = heapq.heappop(l)
            # w = (-t)//2 + t
            # q = t + w
            # print(t,w,q)
            heapq.heappush(l,(-t)//2 + t)
            # print(l)
        return(-sum(l))
        
        