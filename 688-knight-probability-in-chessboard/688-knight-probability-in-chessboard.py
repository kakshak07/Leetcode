class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dfs(i,j,move):
            if(move == k):
                return(1)
            res = 0 
            for x,y in [(i+2,j+1),(i+1,j+2),(i-1,j+2),(i-2,j+1),(i+2,j-1),(i+1,j-2),(i-1,j-2),(i-2,j-1)]:
                if 0<=x<n and 0<=y<n:
                    res += dfs(x,y,move+1)
            return(res/8)

        return dfs(row,column,0)