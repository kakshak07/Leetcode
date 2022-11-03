from collections import defaultdict

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        incomE = defaultdict(list)
        for i in range(len(edges)):
            incomE[edges[i]].append(i)
        max_sum = float("-inf")
        t = set()
        for j in incomE:
            max_sum = max(max_sum, sum(incomE[j]))
        for j in incomE:
            if sum(incomE[j])==max_sum:
                t.add(j)
        
        return t.pop()
        