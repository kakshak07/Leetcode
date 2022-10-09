class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = {}
        
        def dfs(pos):
            if pos == len(days):
                return 0
            if pos in dp:
                return dp[pos]
            
            dp[pos] = float("inf")
            
            for day, cost in zip([1, 7, 30], costs):
                farthest = pos
                while farthest < len(days) and days[farthest] < days[pos] + day:
                    farthest += 1
                dp[pos] = min(dp[pos], cost + dfs(farthest))
            return dp[pos]
            
        return dfs(0)
        