class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        proxy = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if proxy[1]<intervals[i][0]:
                res.append(proxy)
                proxy = intervals[i]
            else:
                proxy = [min(proxy[0], intervals[i][0]), max(proxy[1], intervals[i][1])]
        res.append(proxy)
        return res
                
        