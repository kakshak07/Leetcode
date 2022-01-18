class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        count=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]!=0):
                    count=count+1
        for i in range(len(grid)):
            count=count+max(grid[i])
        for i in range(len(grid[0])):
            a=[]
            for j in range(len(grid)):
                a.append(grid[j][i])
            count=count+max(a)
        return(count)
                
                
        