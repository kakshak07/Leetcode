class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        
        mod = 1e9 + 7
            
        def solve(i, j, moves, dp):
            
            if (i < 0 or i >= m or j < 0 or j >= n) and moves >= 0:
                return 1
            
            if moves < 0:
                return 0
            
            if dp[i][j][moves] != -1: return dp[i][j][moves]
        
            down = solve(i + 1, j, moves - 1, dp)
            up = solve(i - 1, j, moves - 1, dp)
            left = solve(i, j - 1, moves - 1, dp)
            right = solve(i, j + 1, moves - 1, dp)
            
            total = down + up + left + right
            
            dp[i][j][moves] = int(total % mod)
            return int(total % mod)

        dp = [[[-1]*(maxMove + 1) for i in range(n)] for j in range(m)]
        return solve(startRow, startColumn, maxMove, dp)