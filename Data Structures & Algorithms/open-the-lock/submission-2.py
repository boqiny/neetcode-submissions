class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        q = deque(["0000"])
        visited = {"0000"}
        count = 0
        while q:
            count += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(4):
                    for d in (1, -1):
                        digit = (int(cur[i]) + d) % 10
                        nxt = cur[:i] + str(digit) + cur[i+1:]
                        if nxt == target:
                            return count
                        if nxt not in deadends and nxt not in visited:
                            q.append(nxt)
                            visited.add(nxt)
        return -1