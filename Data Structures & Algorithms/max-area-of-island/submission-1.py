class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        m, n = len(grid), len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    count = 1
                    grid[i][j] = 0
                    while stack:
                        cur = stack.pop()
                        r, c = cur[0], cur[1]
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                count += 1 
                                grid[nr][nc] = 0
                                stack.append((nr,nc))
                    max_area = max(max_area, count)
        return max_area