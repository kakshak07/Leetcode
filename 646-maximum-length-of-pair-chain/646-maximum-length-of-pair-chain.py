class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()
        print(pairs)
        count = 1
        abc = pairs[0]
        
        for i in range(1, len(pairs)):
            if abc[1]<pairs[i][0]:
                count += 1
                abc = pairs[i]
            elif abc[1]>pairs[i][1]:
                abc = pairs[i]
        return(count)

