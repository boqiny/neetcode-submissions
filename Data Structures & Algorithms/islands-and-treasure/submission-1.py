class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        d = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                r, c = cur[0], cur[1]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                        grid[nr][nc] = d
                        q.append((nr,nc))
            d += 1
        

