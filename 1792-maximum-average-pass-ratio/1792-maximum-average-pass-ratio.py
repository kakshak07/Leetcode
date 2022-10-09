class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        t = []
        heapq.heapify(t)
        
        for a,b in classes:
            heapq.heappush(t, (-(a+1)/(b+1)+a/b, a,b  ))
            
        while extraStudents>0:
            x,a,b = heapq.heappop(t)
            b=b+1
            a=a+1
            heapq.heappush(t, (-(a+1)/(b+1)+a/b, a,b  ))
            extraStudents = extraStudents - 1
        return sum([a/b for x,a,b in t])/len(classes)
        # ((a+1)/(b+1)-a/b, a,b  )