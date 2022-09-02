class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        time = 0
        
        freshset = set()
        rottenset = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshset.add((i,j))
                if grid[i][j] == 2:
                    rottenset.add((i,j))
        while freshset:
            rotset = set()
            for i,j in freshset:
                if (i-1,j) in rottenset or (i,j-1) in rottenset or (i+1,j) in rottenset or (i,j+1) in rottenset:
                    rotset.add((i,j))
            if(len(rotset)==0):
                return(-1)
            freshset -=rotset
            print(freshset)
            rottenset = rottenset | rotset
            time = time + 1
        return(time)
            
        
        