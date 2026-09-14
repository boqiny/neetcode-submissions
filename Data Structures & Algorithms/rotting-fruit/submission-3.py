class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        fresh_count = 0
        minutes = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2: 
                    q.append((i,j))
        if fresh_count == 0:
            return 0
            
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                r, c = cur[0],cur[1]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh_count -= 1
            minutes += 1
            if fresh_count == 0:
                return minutes
        return -1

