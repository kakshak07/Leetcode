class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        m, n = len(img), len(img[0])
        
        # Pre-fill our output array so we can reference positions directly.
        # Can't use 'smooth_img = [[0]*n]*m' because that will point all rows to the same list in memory
        # and make them all the same as the last row
        smooth_img = []
        for row in range(m):
            smooth_img.append([0]*n)
        
		# Traverse img left to right, and top to bottom.
        for x in range(n):
            for y in range(m):
                # Set smoother boundaries. Right and Bottom are +2 due to exclusive range endpoints
                left, right, top, bottom = x-1, x+2, y-1, y+2
                if left < 0: left = 0
                if right > n: right = n
                if top < 0: top = 0
                if bottom > m: bottom = m
                
                # Apply smoother to cell img[y][x]
                summ, count = 0, 0
                for j in range(left, right):
                    for i in range(top, bottom):
                        count += 1
                        summ += img[i][j]
          
                smooth_img[y][x] = floor(summ/count)
        
        return smooth_img