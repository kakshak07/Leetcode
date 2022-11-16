class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j, color,w):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j]!=w:
                return
            image[i][j] = color
            dfs(i+1,j,color,w)
            dfs(i,j+1,color,w)
            dfs(i-1,j,color,w)
            dfs(i,j-1,color,w)
        w = image[sr][sc]
        if w!=color:
            dfs(sr,sc,color,w)
        return image
        