class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0 or j == 0:
                    dp[i][j] = 1
        for i in range(1,len(dp)):
            for j in range(1, len(dp[i])):
                dp [i][j] = dp[i-1][j]  + dp[i][j-1]
        return dp[m-1][n-1]
        