class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        abcd=[]
        for i in nums:
            # if int(i) not in abcd:
            abcd.append(-int(i))
        
        heapq.heapify(abcd)
        
        for i in range(k-1):
            print(-heapq.heappop(abcd))
        return(str(-heapq.heappop(abcd)))
        