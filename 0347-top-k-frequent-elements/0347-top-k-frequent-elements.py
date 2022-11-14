from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        listCount = Counter(nums)
        heapList = []
        listOfFrequent = []
        for i in listCount:
            heapq.heappush(heapList, (-listCount[i], i))
        for i in range(k):
            
            listOfFrequent.append((heapq.heappop(heapList))[1])
        return(listOfFrequent)
        
        
            
        