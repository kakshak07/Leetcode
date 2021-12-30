class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        new=arr[:]
        for i in range(1,len(new)):
            new[i]^=new[i-1]
        res=[]
        for x,y in queries:
            if x-1<0: res.append(new[y])
            else: res.append(new[y]^new[x-1])
        return res