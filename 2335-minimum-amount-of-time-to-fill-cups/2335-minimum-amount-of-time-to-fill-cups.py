class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
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
                a = heapq.heappop(l)
                a=a+1
                if a!=0:
                    heapq.heappush(l,a)
                counter+=1
                # print(counter)
                continue
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
        