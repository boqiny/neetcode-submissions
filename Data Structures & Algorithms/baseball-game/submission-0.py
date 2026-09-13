class Solution:
    def calPoints(self, operations: List[str]) -> int:
        q = deque(operations)
        res = []
        while q:
            cur = q.popleft()
            if cur == "+":
                res.append(res[-1] + res[-2])
            elif cur == "C":
                res.pop()
            elif cur == "D":
                res.append(2 * res[-1])
            else:
                res.append(int(cur))
        return sum(res)
