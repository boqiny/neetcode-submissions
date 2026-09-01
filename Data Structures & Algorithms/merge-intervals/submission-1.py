class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x : x[0])

        for i in range(len(intervals)):
            c, d = intervals[i]
            if not res:
                res.append([c,d])
                continue
            a, b = res[-1]
            if b >= c:
                res.pop()
                r = max(d,b)
                res.append([a,r])
            else:
                res.append([c,d])
        return res
