from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        # BFS using queue
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        while q:
            cur = q.popleft()
            for dr, dc in directions:
                r, c = dr + cur[0], dc + cur[1]
                if (0 <= r < m and 0 <= c < n and grid[r][c] == 2147483647):
                    grid[r][c] = cur[2]+1
                    q.append((r,c,cur[2]+1))
        