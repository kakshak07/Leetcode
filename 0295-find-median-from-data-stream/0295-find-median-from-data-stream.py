import heapq
class MedianFinder(object):

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -1 * num)
        
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            t = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, t)
        if len(self.small) > len(self.large) + 1:
            t = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, t)
        if len(self.small) + 1 < len(self.large):
            t = heapq.heappop(self.large)
            heapq.heappush(self.small , -1 * t)
        
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return -1* self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        else:
            # print(-1*self.small[0],self.large[0])
            return float((-1*float(self.small[0]) + float(self.large[0]))/2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()