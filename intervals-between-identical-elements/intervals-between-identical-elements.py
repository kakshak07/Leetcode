class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        
        def cal(arr):
            ans = [0]*len(arr)
            prev = {}  # num to (prev index, number of num, total)
            for i, num in enumerate(arr):
                if num not in prev:
                    prev[num] = (i, 1, 0)
                else:
                    ans[i] += prev[num][2] + prev[num][1]*(i - prev[num][0])
                    prev[num] = (i, prev[num][1]+1, ans[i])
            return ans
        
        #print(cal(arr))
        return [i + j for i, j in zip(cal(arr), cal(arr[::-1])[::-1])]