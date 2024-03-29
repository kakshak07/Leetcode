class SmallestInfiniteSet:

    def __init__(self):
        self.h = [i for i in range(1,1001)]
        self.s = set(self.h)
        heapq.heapify(self.h)

    def popSmallest(self) -> int:
        elem = heapq.heappop(self.h)
        self.s.remove(elem)
        return(elem)
        

    def addBack(self, num: int) -> None:
        if(num not in self.s):
            self.s.add(num)
            heapq.heappush(self.h, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)