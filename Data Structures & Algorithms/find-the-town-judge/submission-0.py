class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        indegree = [0] * (n + 1)    # 被多少人信任
        outdegree = [0] * (n + 1)   # 信任了多少人
        for ai, bi in trust:
            outdegree[ai] += 1
            indegree[bi] += 1
        
        for i in range(1, n+1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1