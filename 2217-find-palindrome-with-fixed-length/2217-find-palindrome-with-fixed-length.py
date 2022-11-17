class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        even = 1
        lenPalin = intLength
        if intLength%2 != 0:
            even = 0
            intLength += 1
        mid = intLength//2
        minStart = 10**(mid - 1)
        # print(minStart)
        listOp = []
        
        for i in queries:
            palinDr = str(minStart+i-1)
            
            if even==0:
                # print(palinDr[::-1])
                palinDr = palinDr + palinDr[::-1][1:]
            if even == 1:
                palinDr = palinDr + palinDr[::-1]
            # print(palinDr)
            if len(palinDr) == lenPalin:
                listOp.append(palinDr)
            else:
                listOp.append(-1)
        return listOp
                
        
        