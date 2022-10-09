class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        amount = [a,b,c]
        l = []
        
        heapq.heapify(l)
        if amount[0]!=0:
            heapq.heappush(l,-amount[0])
        if amount[1]!=0:
            heapq.heappush(l,-amount[1])
        if amount[2]!=0:
            heapq.heappush(l,-amount[2])
        counter = 0
        
        while len(l):
            z=len(l)
            if z==1:
                break
            a = heapq.heappop(l)
            b = heapq.heappop(l)
            a = a+1
            b = b+1
            if a!=0:
                heapq.heappush(l,a)
            if b!=0:
                heapq.heappush(l,b)
            counter+=1
            
        return(counter)