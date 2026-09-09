class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count += 1
                    stack = [(r,c)]
                    while stack:
                        cur_r, cur_c = stack.pop()
                        for dr, dc in directions:
                            nr, nc = cur_r + dr, cur_c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                stack.append((nr,nc))
        return count
                    
