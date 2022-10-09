class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]+[float(inf) for i in range(amount)]
        for i in range(1,amount+1):
            for j in coins:
                if(i-j>=0):
                    dp[i]=min(dp[i],dp[i-j]+1)
                    
        if(dp[-1]==float("inf")):
            return(-1)
        return(dp[-1])