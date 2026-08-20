from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        max_len = 0
        if grid[0][0] == 1:
            return -1
        q = deque([(0,0,1)])
        grid[0][0] = 1

        while q:
            cur = q.popleft()
            max_len = max(max_len, cur[2])
            if cur[0] == cur[1] == n-1:
                return max_len
            for dr, dc in directions:
                r, c = dr + cur[0], dc + cur[1]
                if (0 <= r < n and 0 <= c < n and grid[r][c] == 0):
                    grid[r][c] = 1
                    q.append((r,c, cur[2]+1))
        return -1
                





